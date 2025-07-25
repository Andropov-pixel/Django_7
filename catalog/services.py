from .models import Product, Category


def get_products_by_category(category_id):
    return Product.objects.filter(category_id=category_id)


class CategoryService:
    @staticmethod
    def get_full_name(category_id):
        # Получаем полное имя студента по его ID
        category = Category.objects.get(id=category_id)
        return category.name