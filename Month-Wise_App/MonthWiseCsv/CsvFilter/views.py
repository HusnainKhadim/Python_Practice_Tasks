import os

from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import *
import pandas as pd


def welcome(request):
    return render(request, "CsvFilter/Welcome_Page.html")


def upload(request):
    # Template to be render
    template_name = 'CsvFilter/process_csv.html'

    if request.method == 'POST':
        form = CsvProcessForm(request.POST, request.FILES)

        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            # Convert the dates to the desired format (dd/mm/yy)
            start_date_str = start_date.strftime('%d/%m/%y')
            end_date_str = end_date.strftime('%d/%m/%y')

            df = pd.read_csv(csv_file)

            df['Created Date'] = pd.to_datetime(df['Created Date'], format='mixed')

            filtered_df = df.loc[(df['Created Date'] >= start_date_str) & (df['Created Date'] <= end_date_str)]

            # Saving the new csv file
            new_file = filtered_df.to_csv(index=False)

            fs = FileSystemStorage()
            file_name = 'date_within_range.csv'
            content_file = ContentFile(new_file)
            fs.save(file_name, content_file)

            return render(request, 'CsvFilter/success.html', {'new_file_name': file_name})

    form = CsvProcessForm()

    return render(request, template_name, {'form': form})


def download_csv(request, file_name):
    file_path = os.path.join('', file_name)
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response
