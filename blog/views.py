from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .forms import PostForm
# Create your views here.

def main(request):
    posts = Post.objects
    return render(request, 'posts.html', {'posts':posts}) #인자 3개 : request, template, context

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = PostForm()
    return render(request, 'create.html', {'form':form})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'detail.html', {'post':post})

def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = PostForm(instance=post)
    return render(request, 'update.html', {'form':form})

def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('main')