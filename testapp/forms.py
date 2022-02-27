from django.forms import ModelForm
from testapp.models import addimg,addimg1

class addim(ModelForm):
    class Meta:
        model = addimg1
        fields = ['im','is_pri']