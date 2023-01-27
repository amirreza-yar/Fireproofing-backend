from django import forms
from .models import Order, ProductComment, CartItem, DiscountCode

class GetDestinationDetails(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('postal_code', 'address',)

class MakeComment(forms.ModelForm):

    class Meta:
        model = ProductComment
        fields = ('commenter_name', 'commenter_email', 'comment',)

class AddToCart(forms.ModelForm):

    class Meta:
        model = CartItem
        fields = ('quantity',)

class DiscountCodeForm(forms.ModelForm):

    class Meta:
        model = DiscountCode
        fields = ('code',)