from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name='register'),
    path('tutorial', views.tutorial, name='tutorial'),
    path('order', views.order, name='order'),
    path('recommendation', views.recommendation, name='recommendation'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('aboutus', views.aboutus, name='aboutus'),
]
