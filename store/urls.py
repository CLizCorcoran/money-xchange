from django.urls import path
from store import views

urlpatterns = [
    path("", views.home, name="home"),
    path("stock/<name>", views.stock_info, name="stock_info"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact")
]