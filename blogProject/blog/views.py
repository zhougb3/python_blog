from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post, Category
from comments.form import CommentForm
from comments.models import Comment
import markdown
# Create your views here.

def index(request):
	post_list = Post.objects.all().order_by('-created_time')
	return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.body = markdown.markdown(post.body,extensions=['markdown.extensions.extra','markdown.extensions.codehilite','markdown.extensions.toc',])
	comment_list = post.comment_set.all()
	return render(request, 'blog/detail.html', context={'post': post, 'form':CommentForm(), 'comment_list':comment_list})

def archives(request, year, month):
	post_list = Post.objects.filter(created_time__year=year,created_time__month=month).order_by('-created_time')
	return render(request, 'blog/index.html', context={'post_list': post_list})

def category(request, pk):
	cate = get_object_or_404(Category, pk=pk)
	post_list = Post.objects.filter(category=cate).order_by('-created_time')
	return render(request, 'blog/index.html', context={'post_list': post_list})

def about(request):
	return render(request, 'about.html')