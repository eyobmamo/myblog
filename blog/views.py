from django.shortcuts import render

# Create your views here.
# because of template dose not exit error we change theis by the below
# def post_list(request):
#     return render(request,'blog/templates/blog/post_list.html',{})

def post_list(request):
    return render(request, 'blog/post_list.html', {})
