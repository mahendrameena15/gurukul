from django import forms 
from admin_panel.models import Student_Admission,ContactMessage
import re
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber
class AdmissionForm(forms.ModelForm): 
    class Meta:
        model = Student_Admission
        fields = '__all__'
    def clean_student_name(self):
        student_name = self.cleaned_data['student_name']
        pattern = r"^[A-Za-z]+$"
        if not re.match(pattern, student_name):
            raise forms.ValidationError("Name should contain only characters (letters).")
        return student_name
    def clean_parent_name(self):
        parent_name = self.cleaned_data['parent_name']
        pattern = r"^[A-Za-z]+$"
        if not re.match(pattern, parent_name):
            raise forms.ValidationError("Name should contain only characters (letters).")
        return parent_name

    def clean_email(self):
        email = self.cleaned_data['email']
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise forms.ValidationError('Enter a valid email address.')
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        phone_regex= r'^\d{10}$'
        if not phone_number.isdigit(): 
            raise forms.ValidationError('Phone number must contain only digits.')
        elif not re.match(phone_regex,phone_number):
            raise forms.ValidationError('Enter a valid 10 digit phone number.')
        return phone_number

    def clean_percentage_scored(self):
        percentage_scored = self.cleaned_data['percentage_scored']
        if percentage_scored < 0 or percentage_scored > 100:
            raise forms.ValidationError('Percentage score must be between 0 and 100.')
        return percentage_scored

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = '__all__'
   
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        pattern = r"^[A-Za-z]+$"
        if not re.match(pattern, first_name):
            raise forms.ValidationError("Name should contain only characters (letters).")
        return first_name
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        pattern = r"^[A-Za-z]+$"
        if not re.match(pattern, last_name):
            raise forms.ValidationError("Name should contain only characters (letters).")
        return last_name
   
    def clean_email(self):
        email = self.cleaned_data['email']
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise forms.ValidationError('Enter a valid email address.')
        return email
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        phone_regex= r'^\d{10}$'
        if not phone_number.isdigit(): 
            raise forms.ValidationError('Phone number must contain only digits.')
        elif not re.match(phone_regex,phone_number):
            raise forms.ValidationError('Enter a valid 10 digit phone number.')
        return phone_number
    def clean_message(self):
        message = self.cleaned_data['message']
        return message

    # @classmethod
    # def get_value_from_text_class(cls,text):
    #     for v,d in cls.class_passed_in_2023_choice:
    #         if d == text:
    #             return v
    #     return None
    # @classmethod
    # def get_value_from_text_language(cls,text):
    #     for v,d in cls.language_medium_choice:
    #         if d == text:
    #             return v
    #     return None


    # name = forms.CharField(max_length=100, required=True)
    # parent_name = forms.CharField(max_length=100, required=True)
    # date_of_birth = forms.DateField(required=True)
    # email = forms.EmailField(required=True)
    # state = forms.CharField(max_length=100, required=True)
    # district = forms.CharField(max_length=100, required=True)
    # address = forms.CharField(max_length=200, required=True)
    # phone_number = forms.CharField(max_length=10, required=True)
    # class_passed_in_2023 = forms.ChoiceField(choices=[('5th', '5th'), ('6th', '6th'), ('7th', '7th'), ('8th', '8th'), ('9th', '9th'), ('10th', '10th')], required=True)
    # percentage_scored = forms.IntegerField(required=True)
    # language_medium = forms.ChoiceField(choices=[('English', 'English'), ('Hindi', 'Hindi'), ('Marathi', 'Marathi'), ('Bengali', 'Bengali'), ('Odia', 'Odia'), ('Other', 'Other')], required=True)
    # reason_for_choice = forms.CharField(max_length=200, required=True,widget=forms.Textarea)