from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
	"""docstring for Category
		Класс, описывающий категории статьи
	"""
	name = models.CharField('Название категории', max_length=100, help_text='Введите категорию')

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']

class Post(models.Model):
	"""docstring for Post
		Класс, описывающий модель статьи в блоге
	"""
	title = models.CharField('Заголовок', max_length=150, help_text='Введите заголовок статьи')
	content = models.TextField('Контент', max_length=3000, help_text='Введите контент статьи')
	pub_date = models.DateTimeField('Опубликовано', null=True, blank=True, help_text='Дата публикации')
	category = models.ManyToManyField(Category, verbose_name='Категория', help_text='Выберите категорию статьи')
	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', args=[str(self.id)])
		
	class Meta:
		ordering = ['-pub_date']
