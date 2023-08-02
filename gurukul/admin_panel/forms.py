from django import forms 
from .models import Course
import re
class CourseForm(forms.ModelForm): 
    class Meta:
        model = Course
        fields = '__all__'
    def clean_author(self):
        author = self.cleaned_data['author']
        pattern = r"^[A-Za-z]+$"
        if not re.match(pattern, author):
            raise forms.ValidationError("Name should contain only characters (letters).")
        return author

   