from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.news_list, name='news_list'),
    re_path(r'^news/(?P<pk>\d+)/$', views.news_detail, name='news_detail'),
	path('news/new/', views.news_new, name='news_new'),
	re_path(r'^news/(?P<pk>\d+)/edit/$', views.news_edit, name='news_edit'),
]