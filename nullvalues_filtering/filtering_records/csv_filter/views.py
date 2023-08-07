import csv
import os

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
from .forms import CsvUploadForm
import pandas as pd


def home(request):
    return render(request, 'csv_filter/home.html')


def filter_csv(request):
    if request.method == 'POST':
        form = CsvUploadForm(request.POST, request.FILES)
        if form.is_valid():

            csv_file = request.FILES['csv_file']
            if csv_file.name.endswith('.csv'):

                data_frame = pd.read_csv(csv_file)

                # Dropping null values
                data_frame = data_frame.dropna()

                # Saving the new csv file
                new_file=data_frame.to_csv( index=False)

                fs = FileSystemStorage()
                file_name = 'notnull_values_records.csv'
                content_file = ContentFile(new_file)
                fs.save(file_name, content_file)

                return render(request, 'csv_filter/success.html',{'new_file_name':file_name})
            else:
                return render(request, 'csv_filter/error.html',
                              {'error_message': 'Invalid file format. Only CSV files are allowed.'})
    else:
        form = CsvUploadForm()

    return render(request, 'csv_filter/upload.html', {'form': form})


def only_null(request):
    if request.method == 'POST':
        form = CsvUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            if csv_file.name.endswith('.csv'):
                # Reading a csv file
                data_frame = pd.read_csv(csv_file)

                # Filtering null values
                data_frame = data_frame[data_frame.isnull().any(axis=1)]

                # Saving the new csv file
                new_file=data_frame.to_csv(index=False)

                fs = FileSystemStorage()
                file_name = 'onlynull_values.csv'
                content_file = ContentFile(new_file)
                fs.save(file_name, content_file)

                return render(request, 'csv_filter/success.html',{'new_file_name':file_name})
            else:
                return render(request, 'csv_filter/error.html',
                              {'error_message': 'Invalid file format. Only CSV files are allowed.'})
    else:
        form = CsvUploadForm()

    return render(request, 'csv_filter/onlynull.html', {'form': form})


def download_csv(request, file_name):
    file_path = os.path.join('media/',file_name)
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response
