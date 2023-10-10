from django.urls import path
from . import views
from .views import PostDetailView

urlpatterns = [
path('', views.post_list, name='post-list'),
path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
#path('<int:pk>/', views.post_detail, name='post_detail'),
path('post/new/', views.post_new, name='post_new'),
path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]