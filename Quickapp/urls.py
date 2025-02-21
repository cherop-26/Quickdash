
from django.contrib import admin
from django.urls import path
from Quickapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
path('gallery/',views.gallery,name='gallery'),
    path('about/',views.about,name='about'),
    path('form/',views.form,name='form'),
    path('product/',views.product,name='product'),
    path('services/',views.services,name='services'),
]
