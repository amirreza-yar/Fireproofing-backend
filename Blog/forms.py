from django import forms
from .models import BlogComment

class MakeComment(forms.ModelForm):

    class Meta:
        model = BlogComment
        fields = ('commenter_name', 'commenter_email', 'comment',)