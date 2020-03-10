from django.shortcuts import render
from django.http import HttpResponse


from .models import Post, Comments

from .forms import CommentsForm
# Create your views here.


def photo_list(request):
    posts = Post.objects.all()
    return render(request, 'fivehun/index.html', context={'posts': posts})


def photo_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    comment = Comments.objects.filter()

    if request.method == "POST":
        form = CommentsForm(request.POST)
        form.save()
    else:
        form = CommentsForm()

    return render(request, 'fivehun/photo_detail.html', context={'post': post, 'comments': comment, 'form': form})