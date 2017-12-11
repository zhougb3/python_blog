from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from blog.models import Post
from .models import Comment
from .form import CommentForm
# Create your views here.

def post_comment(request, post_pk):
	post = get_object_or_404(Post, pk=post_pk)
	if request.method == 'POST':
		if request.session.get('username', False):
			form = CommentForm(request.POST)
			if form.is_valid():
				comment = form.save(commit=False)
				comment.post = post
				comment.user = User.objects.filter(username= request.session['username'])[0]
				comment.save()
				return redirect(post)
	return redirect('/login')
