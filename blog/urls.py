from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/nouveau/', views.article_create, name='article_create'),
    path('article/<int:pk>/modifier/', views.article_update, name='article_update'),
    path('article/<int:pk>/supprimer/', views.article_delete, name='article_delete'),
]
