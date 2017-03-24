from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^summary$',views.summary),
	url(r'^(?!\s*$).+',views.notfound)
]
