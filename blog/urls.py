from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('<int:id>/', views.blog_detail, name='blog_detail'),
    path('create/', views.post_create, name='post_create'),
    path('<int:id>/edit/', views.post_edit, name='post_edit'),
]
