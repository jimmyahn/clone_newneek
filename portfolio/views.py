from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from .form import PostForm
from .models import SnsData
from .models import Post


# Create your views here.
def post_list(request):
    posts=Post.objects.all()
    return render(request, 'portfolio/post_list.html', {'posts':posts})

def post_detail(request,pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request, 'portfolio/post_detail.html',{'post':post})


def post_new(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form=PostForm()
    return render(request, 'portfolio/post_edit.html',{'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'portfolio/post_edit.html', {'form': form})

def about(request):
    return render(request, 'portfolio/about.html')

def main(request):
    posts = Post.objects.all()
    parsed_data = SnsData.objects.all()
    return render(request, 'portfolio/main.html', {'posts':posts})
