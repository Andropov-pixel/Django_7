from django.urls import path

from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from catalog.apps import CatalogConfig
from catalog.views import CatalogContactsView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('home/', BlogListView.as_view(), name='home'),
    path('create_blog/', BlogCreateView.as_view(), name='create_blog'),
    path('home/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('home/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete')
]