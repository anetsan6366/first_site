from django.shortcuts import render
from .models import Category, Post, Comment
from .forms import CommentForm


def blog_index(request):
    blogs = Post.objects.all().order_by('-created_on')
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog_index.html', context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()
    context = {
        "post": post,
        'comments': comments,
        "form": form,
    }
    return render(request, "blog_details.html", context)


def blog_category(request, category):
    blogs = Post.objects.filter(
        categories__name__contains=category).order_by('-created_on')
    context = {
        "category": category,
        "blogs": blogs
    }
    return render(request, "blog_category.html", context)