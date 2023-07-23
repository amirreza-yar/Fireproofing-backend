from Product.models import Product,Category
from django import template
register = template.Library()

@register.simple_tag
def fillter_products_by_category(category_id):
    cat = Category.objects.get(id=category_id)
    return Product.objects.filter(categories=cat)

@register.simple_tag
def decode_string():
    
    return "کرمان".decode()