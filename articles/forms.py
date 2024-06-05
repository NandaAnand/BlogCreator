from django import forms
from . import models
from tinymce.widgets import TinyMCE

class CreateArticle(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = models.Article
        fields = ['title','body','slug','thumb']