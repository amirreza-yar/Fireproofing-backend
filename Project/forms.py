from django import forms
from .models import ProjectComment

class MakeComment(forms.ModelForm):

    class Meta:
        model = ProjectComment
        fields = ('commenter_name', 'commenter_email', 'comment',)