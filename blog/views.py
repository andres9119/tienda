from .models import Post
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm

def blog_index(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog_index.html', {'posts': posts})

def blog_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/blog_detail.html', {'post': post})

def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:blog_index')  # Asegúrate de que el nombre de la URL coincida
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

@user_passes_test(is_superuser)
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:blog_index')  # Asegúrate de que el nombre de la URL coincida
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})
