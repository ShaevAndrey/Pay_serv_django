"""test_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from pay_service.views import bay, item, get_all_items, bay_items

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bay/<int:id>/', bay),
    path('bay_items/', bay_items),
    path('item/<int:id>/', item),
    path('get_all_items/', get_all_items),
]
