from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegisterForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

	class Meta:
		model = User
        #表单对应的字段名，是这个类里面有的。
		fields = ['username', 'email']

	def clean_password2(self):
 		cd = self.cleaned_data
 		if cd['password'] != cd['password2'] :
 			raise forms.ValidationError(u"校验密码错误")
 		return cd['password2']

	def clean_username(self):
 		username = self.cleaned_data['username']
 		users = User.objects.filter(username = username).count()
 		if users:
 			raise forms.ValidationError(u'用户名已经存在！')
 		return username

	def clean_email(self):
 		email = self.cleaned_data['email']
 		email_count = User.objects.filter(email = email).count()
 		if email_count:
 			raise forms.ValidationError(u'邮箱已经存在！')
 		return email

class LoginForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username']

	def clean_username(self):
		username = self.cleaned_data['username']
		users = User.objects.filter(username = username).count()
		if not users:
			raise forms.ValidationError(u'用户名不存在！')
		return username

	def clean_password(self):
		cd = self.cleaned_data
		users = User.objects.filter(username = cd.get('username')).count()
		if users:
			user = authenticate(username=cd['username'], password=cd[password])
			if not user:
				raise forms.ValidationError(u'密码不正确！')
		return cd['password']