from . import views
from django.urls.conf import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('', views.home, name='home'),
]

