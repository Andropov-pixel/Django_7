"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from operator import index

from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (ProductDetailView, CatalogContactsView, HomeListView, ProductCreateView,
                           ProductDeleteView, ProductUpdateView, CategoryProductView, CategoryProductDetailView)

app_name = CatalogConfig.name


urlpatterns = [
    path('', HomeListView.as_view(), name="home"),
    path('contacts/', CatalogContactsView.as_view(), name='contacts'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('category/', CategoryProductView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryProductDetailView.as_view(), name='category_products'),
]