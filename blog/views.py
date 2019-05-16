from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .forms import BlogForm
from .models import Blog
from django.views.generic. base import TemplateView

class MainpageView(TemplateView):
        template_name = 'blog/layout.html'

# Create your views here.
# 들어가자마자 보이는 페이지의 함수
def layout(request):
    return render(request, 'blog/layout.html')

#CREATE
def blogform(request, blog=None):
    if request.method =='POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date=timezone.now()
            blog.save()
            return redirect('home')
    else:
        form = BlogForm(instance=blog)
        return render(request, 'blog/new.html', {'form':form})
#READ
def home(request):
    blogs = Blog.objects
    return render(request, 'blog/home.html', {'blogs': blogs})
#UPDATE
def edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return blogform(request, blog)
#DELE
def remove(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('home')

def main(request):
    return render(request, 'blog/main.html')