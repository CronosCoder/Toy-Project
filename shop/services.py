from shop.models import Product

class ProductService:
    model_class = Product

    def all(self, **kwargs):
        return self.model_class.objects.filter(**kwargs)

    def create_product(self, data):
        return self.model_class.objects.create(**data)
