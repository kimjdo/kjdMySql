#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
#     url(r'^$', views.post_list, name='post_list'),
#     url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit')
]
