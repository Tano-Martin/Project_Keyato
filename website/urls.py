"""keyato URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("part/", views.part, name="part"),
    path("part_detail/<int:id_part>", views.part_detail, name="part_detail"),
    path("contact/", views.contact, name="contact"),
    path("order/<int:id_part>", views.order, name="order"),
    path("contactPost/", views.contactPost, name="contactPost"),
    path("orderPost/", views.orderPost, name="orderPost"),
]
