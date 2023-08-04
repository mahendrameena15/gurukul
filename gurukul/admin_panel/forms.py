from django import forms 
from .models import Course,Category
import re
import json
class CourseForm(forms.ModelForm): 
    class Meta:
        model = Course
        fields = '__all__'
      
    def clean_author(self):
        author = self.cleaned_data['author']
        pattern = r"^[A-Za-z ]+$"
        if not re.match(pattern, author):
            raise forms.ValidationError("Name should contain only letters.")
        return author
class CategoryForm(forms.ModelForm): 
    class Meta:
        model = Category
        fields = '__all__'
      
    def clean_author(self):
        author = self.cleaned_data['author']
        pattern = r"^[A-Za-z ]+$"
        if not re.match(pattern, author):
            raise forms.ValidationError("Name should contain only letters.")
        return author


    # def clean_meta(self):
    #     meta = self.cleaned_data['meta']
    #     try:
    #         json.loads(meta)
    #     except json.JSONDecodeError:
    #         raise forms.ValidationError("Invalid JSON data for Meta. Please provide a valid JSON string.")
    #     return meta

    # def clean_seo(self):
    #     seo = self.cleaned_data['seo']
    #     try:
    #         json.loads(seo)
    #     except json.JSONDecodeError:
    #         raise forms.ValidationError("Invalid JSON data for SEO. Please provide a valid JSON string.")
    #     return seo


   