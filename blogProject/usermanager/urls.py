from django.conf.urls import url
from . import views

app_name = 'usermanager'

urlpatterns = [
	url(r'^register/$', views.register, name = 'register'),
	url(r'login/$', views.login, name = 'login'),
	url(r'^register/api/$', views.registerapi, name = 'registerapi'),
	url(r'login/api/$', views.loginapi, name = 'loginapi'),
]
