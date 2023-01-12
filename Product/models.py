from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField

import json
import datetime as dt
from random import choices as random_choices

class Product(models.Model):
    name = models.CharField(max_length=200, blank=False)
    meta_description = models.TextField(blank=True)
    # full_description = models.TextField(blank=True)
    full_description = RichTextField()
    # product_unicode = models.IntegerField()
    is_instock = models.BooleanField(default=True, null=False)
    rate = models.FloatField(null=False, default=0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    image = models.ImageField(upload_to=f'productImage/', blank=True)
    price = models.IntegerField(blank=False, validators=[MinValueValidator(0)])
    comments = models.ManyToManyField("ProductComment", related_name='+', blank=True)
    quantity_purchased = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    # @property
    def add_to_quantity_purchased(self, value):
        self.quantity_purchased += value

    @property
    def rate_filled_star_counter(self):
        return [i for i in range(int(self.rate))]
    property
    def rate_unfilled_star_counter(self):
        return [i for i in range(5 - int(self.rate))]


    def get_absolute_url(self):
        return reverse('productDetail', kwargs={'pk' : self.pk})
    
    def add_to_cart(self):
        return reverse("addToCart", kwargs={'pk': self.pk})

    def remove_form_cart(self):
        return reverse("removeFromCart", kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.name

class ProductComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    user_rate = models.FloatField(null=True, default=5, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    commenter_name = models.CharField(max_length=200)
    commenter_email = models.EmailField()
    comment = models.TextField()
    # date = models.DateField(auto_now=True)

    @property
    def rate_filled_star_counter(self):
        return [i for i in range(int(self.user_rate))]

    @property
    def rate_unfilled_star_counter(self):
        return [i for i in range(5 - int(self.user_rate))]

class Cart(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField("CartItem", related_name='+')
    # ordered = models.BooleanField(default=False)
    # ordered_date = models.DateTimeField(null=True)

    shipping_price = models.IntegerField(default=200, validators=[MinValueValidator(0)])

    @property
    def items_price(self):
        return sum([item.total_price for item in self.items.all()])
    
    @property
    def finished_price(self):
        return self.items_price + self.shipping_price
    
    def __str__(self):
        return f"{self.customer}'s cart"

class CartItem(models.Model):
    # customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(0)])

    @property
    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"Cart item {self.product}"

class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=1000, blank=True)
    postal_code = models.IntegerField(default=132, blank=True)
    additional_note = models.CharField(max_length=1000, blank=True)
    items = models.JSONField(blank=False)

    class StatusChoises(models.TextChoices):
        PENDING = 'PN', _('در انتظار تایید')
        PREPARING = 'PR', _('در حال آماده سازی')
        SENDING = 'SN', _('در حال ارسال')
        RECIEVED = 'RC', _('تحویل داده شده')
        
    status = models.CharField(
        max_length=2,
        choices=StatusChoises.choices,
        default=StatusChoises.PENDING
    )

    @property
    def get_status(self):
        return self.get_status_display()

    items_price = models.IntegerField(blank=False, validators=[MinValueValidator(0)])
    shipping_price = models.IntegerField(blank=False, validators=[MinValueValidator(0)])
    finished_price = models.IntegerField(blank=False, validators=[MinValueValidator(0)])
    discount_code = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    ordered_date = models.DateTimeField(default=dt.datetime.now())
    phone_number = models.IntegerField()

    @property
    def loaded_json_items(self):
        return json.loads(self.items)

    # @property
    # def finished_price(self):
    #     return self.items_price + self.shipping_price - self.discount_amount

class DiscountCode(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Add a default value for expire date, two weeks from now
    expire_date_default = dt.datetime.now() + dt.timedelta(weeks=2)
    expire_date = models.DateField(default=expire_date_default)

    # discount_code = 

    def generate_random_code(self):
        # Create a 6-length code
        discount_code = str()
        for char in random_choices("0123456789QWERTYUIOPASDFGHJKLZXCVBNM", k=6):
            discount_code += char
        return discount_code