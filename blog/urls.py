from django.urls import path
from django.contrib import admin
from . import views
from .views import TagIndexView, PostList, PostDetail

admin.autodiscover()

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/<slug:the_slug>/',PostDetail.as_view(), name='post_detail'),
    path('post/new/', views.post_new, name = 'post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('contact', views.contact, name='contact'),
    path('success', views.success, name='success'),
    path('about', views.about, name='about'),
    path('tag/<slug:slug>', TagIndexView.as_view(), name='tagged'),
]