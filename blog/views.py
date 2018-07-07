from django.shortcuts import render
from .models import Post
from django.utils import timezone
def post_list(reqest):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(reqest, 'blog/post_list.html' , {'posts':posts})

# Create your views here.
