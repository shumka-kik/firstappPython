from django.shortcuts import render
from django.views.generic.detail import DetailView
from . models import Post, Category

# Create your views here.
def base(request):
	return render(request, 'firstapp/base.html')


def page1(request):
	name = 'Alexander'
	second_name = 'Chuvashov'
	age = 28
	weight = 62
	return render(request, 'firstapp/page1.html',
		context={'name':name, 'second_name':second_name, 'age':age, 'weight':weight})

def page2(request):
	name = 'Alexander'
	second_name = 'Chuvashov'
	age = 28
	weight = 62
	return render(request, 'firstapp/page2.html',
		context={'name':name, 'second_name':second_name, 'age':age, 'weight':weight})

def post_list(request):
	posts = Post.objects.all()
	return render(request, 'firstapp/post_list.html', {'posts': posts})

class PostDetailView(DetailView):
	model = Post

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context
