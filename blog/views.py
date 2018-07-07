from django.shortcuts import render
def post_list(reqest):
    return render(reqest, 'blog/post_list.html' , {})

# Create your views here.
