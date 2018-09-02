from django.db import models
from django.contrib import admin

# Create your models here.

class Genre(models.Model):

	name = models.CharField(max_length=200, help_text='Введите жанр')

	def __str__(self):
		return self.name

class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
	summary = models.TextField(max_length=1000, help_text='Введите краткое описание книги')
	isbn = models.CharField('ISBN', max_length=13, help_text='Введите 13 символов ISBN')
	genre = models.ManyToManyField(Genre, help_text='Выберите жанр для книги')

	def __str__(self):
		"""
		Строка представления объекта Модели
		"""
		return self.title

	def get_absolute_url(self):
		return reverse('book-detail', args=[str(self.id)])

import uuid

class BookInstance(models.Model):
	
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Уникальный идентификатор экземпляра Книги')
	book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
	imprint = models.CharField(max_length=200)
	due_back = models.DateField(null=True, blank=True)

	LOAN_STATUS = (
		('m', 'В наличии'),
		('o', 'Читают'),
		('a', 'Доступно'),
		('r', 'Ожидается'),
	)

	status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d', help_text='Доступность книги')

	class Meta:
		ordering = ["due_back"]

	def __str__(self):
		return '%s (%s / Возврат:%s / UID:%s)' % (self.book.title, self.get_status_display(), self.due_back, self.id)

class Author(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_of_birth = models.DateField(null=True, blank=True)
	date_of_death = models.DateField('Died', null=True, blank=True)

	def get_absolute_url(self):
		return reverse('author-detail', args=[str(self.id)])

	def __str__(self):
		return '{0}, {1}'.format(self.last_name, self.first_name)

"""
Creates an objects of Book and display it in AuthorAdmin
"""
class BookInline(admin.TabularInline):
	model = Book

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
	inlines = [BookInline] # Dispay Book objects by current Author

"""
Creates an objects of BookInstance and display it in BookAdmin
"""
class BookInstanceInline(admin.TabularInline):
	model = BookInstance

class BookAdmin(admin.ModelAdmin):
	list_display=('title', 'author', 'display_genre')
	inlines = [BookInstanceInline] # Dispay BookInstance objects by current Book

	def display_genre(self, obj):
		"""
		Creates a string for the Genre. This is required to display genre in Admin.
		"""
		return ', '.join([ genre.name for genre in obj.genre.all()[:3]])
	display_genre.short_description = 'Genre'

class BookInstanceAdmin(admin.ModelAdmin):
	list_filter = ('status', 'due_back')
	fieldsets = (
		(None, {
			'fields': ('book', 'imprint', 'id')

			}),
		('Availability', {
			'fields': ('status', 'due_back')
			}),
		)

