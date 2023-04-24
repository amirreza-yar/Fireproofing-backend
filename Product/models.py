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
    en_name = models.CharField(max_length=200, blank=False)
    meta_description = models.TextField(blank=True)
    en_meta_description = models.TextField(blank=True)
    full_description = models.TextField(blank=True)
    en_full_description = models.TextField(blank=True)
    # en_full_description = RichTextField()
    # product_unicode = models.IntegerField()
    is_instock = models.BooleanField(default=True, null=False)
    rate = models.FloatField(null=False, default=0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    image0 = models.ImageField(upload_to=f'productImage/', blank=True,null=True)
    image1 = models.ImageField(upload_to=f'productImage/', blank=True,null=True)
    image2 = models.ImageField(upload_to=f'productImage/', blank=True,null=True)
    image3 = models.ImageField(upload_to=f'productImage/', blank=True,null=True)
    image4 = models.ImageField(upload_to=f'productImage/', blank=True,null=True)
    image5 = models.ImageField(upload_to=f'productImage/', blank=True,null=True)
    image6 = models.ImageField(upload_to=f'productImage/', blank=True,null=True)
    price = models.IntegerField(blank=False, validators=[MinValueValidator(0)])
    comments = models.ManyToManyField("ProductComment", related_name='+', blank=True)
    quantity_purchased = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    date_added = models.DateTimeField(auto_now=True)
    is_recommended = models.BooleanField(default=True)
    discount_percentage = models.IntegerField(default=0, validators=[MinValueValidator(0.0), MaxValueValidator(100)])
    is_service = models.BooleanField(default=False)
    # inventory = models.IntegerField()
    
    categories = models.ManyToManyField("Category", related_name='+', blank=True)
    
    @property
    def new_price(self):
        new_price = self.price - self.discount_percentage * self.price / 100
        return int(new_price)

    @property
    def add_to_quantity_purchased(self, value):
        self.quantity_purchased += value

    @property
    def rate_filled_star_counter(self):
        return [i for i in range(int(self.rate))]
    
    @property
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

class Category(models.Model):  
    name = models.CharField(max_length=33)
    description = models.TextField()
    status = models.BooleanField(default=True)

    @property
    def category_display(self):
        return self.name

    def __str__(self):
        return self.category_display

class Cart(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField("CartItem", related_name='+')
    discount = models.ForeignKey("DiscountCode", on_delete=models.SET_NULL, null=True, blank=True)
    # ordered = models.BooleanField(default=False)
    # ordered_date = models.DateTimeField(null=True)

    shipping_price = models.IntegerField(default=200, validators=[MinValueValidator(0)])

    @property
    def item_quantity(self):
        return len(self.items.all())

    @property
    def items_price(self):
        return sum([item.total_price for item in self.items.all()])

    @property
    def discount_price(self):

        if self.discount == None:
            return 0

        discount = self.discount.discount_price

        if discount[0]:
            return self.items_price * discount[1]
        else:
            return discount[1]
    
    @property
    def finished_price(self):
        return self.items_price + self.shipping_price - self.discount_price
    
    def __str__(self):
        return f"{self.customer}'s cart"

class CartItem(models.Model):
    # customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(0)])

    @property
    def total_price(self):
        return self.quantity * self.product.new_price

    def __str__(self):
        return f"Cart item {self.product}"

class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=1000, blank=True)
    postal_code = models.IntegerField(default=132, blank=True)
    additional_note = models.CharField(max_length=1000, blank=True)
    items = models.JSONField(blank=False)
    # items = models.ManyToManyField(Product,related_name='+')
    is_payed = models.BooleanField(default=False)
    class StatusChoises(models.TextChoices):
        PENDING = 'PN', _('در انتظار تایید')
        PREPARING = 'PR', _('در حال آماده سازی')
        SENDING = 'SN', _('در حال ارسال')
        RECIEVED = 'RC', _('تحویل داده شده')
        CANCELD = 'CD', _('لغو شده')
        
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

    code = models.CharField(max_length=6, unique=True, blank=False)
    
    # Add a default value for expire date, two weeks from now
    expire_date_default = dt.datetime.now() + dt.timedelta(weeks=2)
    expire_date = models.DateField(default=expire_date_default)

    is_a_percentage = models.BooleanField(default=True)
    discount_percentage = models.FloatField(default=0, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    discount_amount = models.IntegerField(default=0)

    @property
    def is_expired(self):
        if dt.datetime.now() > self.expire_date:
            return True
        else:
            return False

    @property
    def discount_price(self):
        if self.is_a_percentage:
            # Return True to indicate a percentage discount
            return (True, self.discount_percentage)
        else:
            # Return False to indicate a amount discount
            return (False, self.discount_amount)