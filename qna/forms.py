from django import forms
from .models import Question, Answer
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']
