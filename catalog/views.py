from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.urls import reverse_lazy, reverse
from .forms import ProductForm, Category, ProductModeratorForm
from .services import get_products_by_category, CategoryService
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from catalog.models import Product


# Create your views here.

# @method_decorator(cache_page(60 * 15), name='dispatch')
class HomeListView(ListView):
    model = Product
    template_name = 'catalog/base.html'
    context_object_name = 'products'

    # def get_queryset(self):
    #     cache_kay = 'all_available_products'
    #     products = cache.get(cache_kay)
    #     if products is None:
    #         products = Product.objects.filter(is_available=True)
    #         cache.set(cache_kay, products, 60 * 15)
    #     return products


# def home(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'base.html', context=context)


def contacts(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'contacts.html')


class CatalogContactsView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')

    def post(self, request):
        #Получение данных из формы
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy("catalog:home")

    def get_form_class(self):
        if self.request.user.is_superuser:
            return ProductForm
        if self.request.user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        if self.request.user.has_perm("catalog.remove_any_product"):
            return ProductModeratorForm
        return ProductForm

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.has_perm(
            "catalog.can_unpublish_product"
        )

    def handle_no_permission(self):
        raise PermissionDenied


# @method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        queryset = cache.get('category_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('category_queryset', queryset, 60 * 15)
        return queryset


class ProductDeleteView(LoginRequiredMixin,DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:home')


class CategoryProductDetailView(DetailView):
    model = Category
    template_name = 'catalog/base.html'

    def get_context_data(self, **kwargs):
        # Получаем стандартный контекст данных из родительского класса
        context = super().get_context_data(**kwargs)
        # Получаем ID категория из объекта
        category_id = self.kwargs.get('pk')
        context['name'] = CategoryService.get_full_name(category_id)
        context['products'] = Product.objects.filter(category_id=category_id)
        return context


class CategoryProductView(ListView):
    model = Category
    template_name = 'catalog/category_products.html'


# def product_detail(request, pk):
#     product = get_object_or_404(Product, id=pk)
#     context = {'product': product}
#     return render(request, 'product_detail.html', context=context)