from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Post
from .forms import PostForm


# Create your views here.
def news_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'news/news_list.html', {'posts': posts})

def news_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.counter += 1
    post.save()
    return render(request, 'news/news_detail.html', {'post': post})

def news_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.counter = 0
            post.save()
            return redirect('news_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'news/news_edit.html', {'form': form})

	
def news_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.counter = 0
            post.save()
            return redirect('news_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'news/news_edit.html', {'form': form})

def news_statistics(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-counter')
    return render(request, 'news/news_statistics.html', {'posts': posts})