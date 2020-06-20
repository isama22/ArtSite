from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),

    path('fibers/', views.fibers_index, name="fibers_index"),
    path('fibers/<int:fiber_id>/', views.fibers_detail, name='fibers_detail'),
    path('fibers/create/', views.FibersCreate.as_view(), name='fibers_create'),
    path('fibers/<int:pk>/update/', views.FiberUpdate.as_view(), name='fibers_update'),
    path('fibers/<int:pk>/delete/', views.FiberDelete.as_view(), name='fibers_delete'),

    path('figuratives/', views.figuratives_index, name="figuratives_index"),
    path('figuratives/<int:figurative_id>/', views.figuratives_detail, name='figuratives_detail'),
    path('figuratives/create/', views.FigurativesCreate.as_view(), name='figuratives_create'),
    path('figuratives/<int:pk>/update/', views.FigurativeUpdate.as_view(), name='figuratives_update'),
    path('figuratives/<int:pk>/delete/', views.FigurativeDelete.as_view(), name='figuratives_delete'),

    path('digitals/', views.digitals_index, name="digitals_index"),
    path('digitals/<int:digital_id>/', views.digitals_detail, name='digitals_detail'),
    path('digitals/create/', views.DigitalsCreate.as_view(), name='digitals_create'),
    path('digitals/<int:pk>/update/', views.DigitalUpdate.as_view(), name='digitals_update'),
    path('digitals/<int:pk>/delete/', views.DigitalDelete.as_view(), name='digitals_delete'),

    path('accounts/signup/', views.signup, name='signup'),

    path('fibers/<int:fiber_id>/add_photo/', views.add_photo, name='add_photo'),
]