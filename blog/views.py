from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog(request):
    Blogs = Blog.objects.order_by('-date') [:2]
    return render(request,'blog/blog.html', {'Blogs': Blogs})

def individualblog(request,blog_id):
    individualblog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/individualblog.html',{'blogid':individualblog})

