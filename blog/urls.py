from django.urls import path
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/',views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name = 'post_new'),
    path('signup', views.subscriber_new, name = 'sub_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('contact', views.contact, name='contact'),
    path('success', views.success, name='success'),
]