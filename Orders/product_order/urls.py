from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('',views.index,name='index'),
     path('product_add/',views.product_add,name='product_add'),
     path('register',views.register,name='register'),
     path('login',views.login_view,name='login'),
     path('logout',views.logoutuser,name='logout'),
     path('blog_home',views.blog_home,name='blog_home'),
     path('<int:pk>/blog_detail',views.blog_detail,name='blog_detail'),
     path('<int:pk>/blog_result',views.blog_result,name='blog_result'),
     path('<int:pk>/blog_vote',views.blog_vote,name='blog_vote'),
     path('chats',views.chats,name='chats'),
     path('<int:pk>/chat_post_detail',views.chat_post_detail,name='chat_post_detail'),
     # path('<int:pk>/add_comment', views.add_comment, name='add_comment'),

     
    
]