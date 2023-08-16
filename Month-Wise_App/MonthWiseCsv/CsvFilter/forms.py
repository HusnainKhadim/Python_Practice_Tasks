from django import forms


class CsvProcessForm(forms.Form):
    csv_file = forms.FileField(label='Upload Csv File', required=True)
    start_date = forms.DateField(label='Start Date', widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    end_date = forms.DateField(label='End Date', widget=forms.DateInput(attrs={'type': 'date'}), required=True)
