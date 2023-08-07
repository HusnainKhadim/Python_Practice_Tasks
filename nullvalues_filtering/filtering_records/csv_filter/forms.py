from django import forms
from .models import *


class CsvUploadForm(forms.Form):
    csv_file = forms.FileField()
