from django import forms
from .models import Post

class AppealForm(forms.ModelForm):
    class Meta:
        model = Post        # REQUIRED
        fields = '__all__'