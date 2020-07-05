from django.urls.conf import path,include
from . import views

app_name='blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path ('<int:blog_id>/', views.individualblog, name='individualblog')

]