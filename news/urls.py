from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.news_list, name='news_list'),
    re_path(r'^news/(?P<pk>\d+)/$', views.news_detail, name='news_detail'),
	#path('post/new/', views.post_new, name='post_new'),
	#re_path(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]