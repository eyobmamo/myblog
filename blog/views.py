from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.
# because of template dose not exit error we change theis by the below
# def post_list(request):
#     return render(request,'blog/templates/blog/post_list.html',{})


# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html', {})




def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {"posts":posts})
