from django.shortcuts import render
from .models import Index, BlogDetail, Image

# Create your views here.

def index(request):
    setting = Index.objects.latest("id")
    context = {
        "setting":setting
    }
    return render(request, "index.html", context)

def blog_detail(request):
    blog_detail = BlogDetail.objects.latest("id")
    context = {
        "setting":blog_detail,
    }
    return render(request, "blog-detail.html", context)

def image(request):
    image = Image.objects.latest("id")
    context = {
        "image": image,

    }
    return render(request, "image.html", context)