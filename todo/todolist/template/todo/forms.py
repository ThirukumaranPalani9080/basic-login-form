from django import forms
from .models import Todolist
  
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields="__all__"#</pre>