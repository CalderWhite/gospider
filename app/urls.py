from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^get_summary',views.get_summary),
	url(r'^',views.index)
]
