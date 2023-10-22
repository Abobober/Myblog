from django.urls import path
from . import views
from .views import PostDetailView, PostListView, PostCreateView, PostUpdateView
from django.contrib.auth import views as auth_views

urlpatterns = [
path('', PostListView.as_view(), name='post_list'),
path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
path('post/new/', PostCreateView.as_view(), name='post_new'),
path('post/edit/<int:pk>/', PostUpdateView.as_view(), name='post_edit'),
path('login/', views.LoginView.as_view(), name='login'),
path('logout/', views.LogoutView.as_view(), name='logout'),
path('<pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
#path('', views.post_list, name='post-list'),
#path('<int:pk>/', views.post_detail, name='post_detail'),
#path('post/new/', views.post_new, name='post_new'),
#path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
#path('login/', auth_views.LoginView.as_view(), name='login'),
]