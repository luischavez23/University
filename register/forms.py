from django.forms import ModelForm
from django import forms
from .models import Course

class CourseForm(ModelForm):
    id_course = forms.CharField(max_length=6, label='ID', widget=forms.TextInput(attrs={'class':'form-control'}))
    name = forms.CharField(max_length=50, label='Course', widget=forms.TextInput(attrs={'class':'form-control'}))
    credit = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = Course
        fields = '__all__'