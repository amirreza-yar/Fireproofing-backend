from CustomUser.models import UserProfile
from Product.models import (
    Category,
    Product
)
from Blog.models import Blog
from django import forms
from ckeditor.widgets import CKEditorWidget
class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)

class ProductForm(forms.ModelForm):
    full_description = forms.CharField(widget=CKEditorWidget())
    en_full_description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Product
        fields = ('name','en_name','meta_description','en_meta_description','full_description','en_full_description','image0','image1','image2','image3','image4','image5','image6','price','categories','is_instock','is_recommended','discount_percentage','is_service')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields)
        for field in self.fields:
            if field in ['is_instock','is_recommended','is_service']:
                continue
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['image0'].widget.attrs['id'] = 'imageUpload'
        self.fields['image1'].widget.attrs['id'] = 'thumbUpload01'
        self.fields['image2'].widget.attrs['id'] = 'thumbUpload02'
        self.fields['image3'].widget.attrs['id'] = 'thumbUpload03'
        self.fields['image4'].widget.attrs['id'] = 'thumbUpload04'
        self.fields['image5'].widget.attrs['id'] = 'thumbUpload05'
        self.fields['image6'].widget.attrs['id'] = 'thumbUpload06'
        self.fields['image0'].widget.attrs['class'] = 'ec-image-upload'
        self.fields['image1'].widget.attrs['class'] = 'ec-image-upload'
        self.fields['image2'].widget.attrs['class'] = 'ec-image-upload'
        self.fields['image3'].widget.attrs['class'] = 'ec-image-upload'
        self.fields['image4'].widget.attrs['class'] = 'ec-image-upload'
        self.fields['image5'].widget.attrs['class'] = 'ec-image-upload'
        self.fields['image6'].widget.attrs['class'] = 'ec-image-upload'
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('cover','title','en_title','body','en_body','meta_description','en_meta_description',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['cover'].widget.attrs['id'] = 'thumbUpload06'
        self.fields['cover'].widget.attrs['class'] = 'ec-image-upload'
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description','en_name', 'en_description','parent')
class PersonelForm(forms.ModelForm):
    password1 = forms.CharField(
            label=("Password"),
            strip=False,
            widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
            # help_text=password_validation.password_validators_help_text_html(),
        )
    class Meta:
        model = UserProfile
        fields = ('username', 'name', 'email', 'phone_number', 'address', 'postal_code', 'city','category_access','blog_access','product_access','order_access')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                "autofocus"
            ] = True

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_staff = True
        if commit:
            user.save()
        return user
