from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.contrib.auth.models import User
from blog.models import Post
# Create your models here.
@python_2_unicode_compatible
class Comment(models.Model):
	created_time = models.DateTimeField(auto_now_add=True)
	text = models.TextField()
	user = models.ForeignKey(User)
	post = models.ForeignKey(Post)

	def __str__(self):
		return self.text[:20]