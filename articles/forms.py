from dataclasses import fields
import imp
from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        
    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.filter(title_icontains=title)
        if qs.exists():
            self.add_error('title', f'{title} is already in use.')
        return data
        
class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    
    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     title = cleaned_data.get('title')
    #     return title
    
    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == 'the office':
            self.add_error('title', 'This title is taken')
        if 'office' in content or 'office' in title.lower():
            self.add_error('content', 'Office cannot be in content')
            raise forms.ValidationError('Office is not allowed')
        return cleaned_data