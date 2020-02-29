from django import forms
from .models import *


class TrainingCourseForm(forms.ModelForm):

    class Meta:
        model = Course
        exclude = [""]