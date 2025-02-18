from django import forms
from .models import Category, Blog


class CreateBlogForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    
    class Meta:
        model = Blog
        fields = ['category', 'title', 'image', 'body']

