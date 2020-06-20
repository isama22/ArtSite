from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name="about"),
    path('fibers/', views.fibers_index, name="fibers_index"),
    path('fibers/<int:fiber_id>/', views.fibers_detail, name='fibers_detail'),

    path('figuratives/', views.figuratives_index, name="figuratives_index"),
    path('figuratives/<int:figurative_id>/', views.figuratives_detail, name='figuratives_detail'),

    path('digitals/', views.digitals_index, name="digitals_index"),
    path('digitals/<int:digital_id>/', views.digitals_detail, name='digitals_detail'),
]