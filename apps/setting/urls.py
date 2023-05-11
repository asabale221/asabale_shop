from django.urls import path
from .views import index, blog_detail, image


urlpatterns = [
    path('', index, name = "index"),
    path('blog_detail/', blog_detail, name = "blog_detail"),          
    path('image/', image, name = "image"),        
]