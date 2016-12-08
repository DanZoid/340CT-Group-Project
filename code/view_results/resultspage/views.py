from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
import os

def files(request):
    path="C:\\"  # path to directory
    file_list =os.listdir(path) #lists all files in the location of the file path
    return render_to_response('file_view.html', {'Files': file_list}) #outputs the list of files