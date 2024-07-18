from django.urls import path
from blog.views import *

#create requests here

app_name='blog'

urlpatterns=[
    path('',bloghome,name='bloghome'),
    path('post/<int:id>',post,name='post'),
    path('postlike/<int:id>',post_likes,name='postlike'),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
    path('dashboard',dashboard,name='dashboard'),
    path('user_login',user_login,name='login'),
    path('user_signup',user_signup,name='signup'),
    path('user_logout',user_logout,name='logout'),
    path('newpost',newpost,name='newpost'),
    path('updatepost/<int:id>',updatepost,name='updatepost'),
    path('deletepost/<int:id>',deletepost,name='deletepost'),
    path('setsess',setsess,name='setsess'),
    path('getsess',getsess,name='getsess'),
    path('delsess',delsess,name='delsess'),
]
