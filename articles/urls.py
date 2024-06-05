
from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    url(r'^$',views.article_list, name = "list"),
    url(r'^my_articles/$',views.article_my_list, name = "mylist"),
    url(r'^create/$', views.article_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
     url(r'^(?P<id>\d+)/edit/$', views.article_edit, name='edit'),
     url(r'^(?P<id>\d+)/delete/$', views.article_delete, name='delete'),
     path('upload_image/', views.upload_image, name='upload_image'),
    
]