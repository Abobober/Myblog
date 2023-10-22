from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['pub_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'
    login_url = "/login"  
    redirect_field_name = "login"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.published_date = timezone.now()
        post.save()
        return redirect('post_detail', pk=post.pk)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'
    login_url = "/login"  
    redirect_field_name = "login"

    
    def test_func(self):
        return self.get_object().author == self.request.user

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    login_url = "/login"  
    redirect_field_name = "login"

    def get_success_url(self):
        return reverse_lazy('post_list')

class LoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('post_list')

class LogoutView(LogoutView):
    template_name = 'blog/post_list.html'

    def get_success_url(self):
        return reverse_lazy('post_list')
    






#def post_list(request):
#    posts = Post.objects.all()
#    posts = Post.objects.order_by('pub_date')
#    return render(request, 'blog/post_list.html', {'posts' : posts})

#def post_detail(request, pk):
 #   post = get_object_or_404(Post, pk=pk)
#    return render(request, 'blog/post_detail.html', {'post': post})

#def post_new(request):
#    if request.method == "POST":
#        form = PostForm(request.POST)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.author = request.user
#            post.published_date = timezone.now()
#          post.save()
#            return redirect('post_detail', pk=post.pk)
#    else:
#        form = PostForm()
#    return render(request, 'blog/post_edit.html', {'form': form})

#def post_edit(request, pk):
#    post = get_object_or_404(Post, pk=pk)
#    if request.method == "POST":
#        form = PostForm(request.POST, instance=post)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.author = request.user
#            post.pub_date = timezone.now()
#            post.save()
#            return redirect('post_detail', pk=post.pk)
#    else:
#        form = PostForm(instance=post)
#    return render(request, 'blog/post_edit.html', {'form': form})
