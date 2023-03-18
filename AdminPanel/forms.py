from CustomUser.models import UserProfile
from Product.models import (
    Category,
    Product
)
from Blog.models import Blog
from django import forms
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name','en_name','meta_description','en_meta_description','full_description','en_full_description','image0','image1','image2','image3','image4','image5','image6','price','categories')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('cover','title','en_title','body','en_body','meta_description','en_meta_description',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description')
class PersonelForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('username', 'name', 'email', 'phone_number', 'address', 'postal_code', 'city',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                "autofocus"
            ] = True

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password("12345678")
        user.is_staff = True
        user.save()
        return user
