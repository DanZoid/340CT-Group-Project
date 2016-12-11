from django.shortcuts import render
from django.shortcuts import render_to_response

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # defines the base directory of the project to make file locations work on different environments.


def files(request):
    path=os.path.join(BASE_DIR, 'media/media')  # path to media directory
    file_list =os.listdir(path) #lists all files in the location of the file path
    log = open(os.path.join(BASE_DIR, 'resultspage/output.txt'), "w") #opens a text document that can be written to
    for file in file_list: #allows a list of files to be printed as below
        print(file, file=log) #prints the list of files to a txt document as a log
        print(file) #prints the list of files as an output



    return render(request, 'file_view.html', {'FileList': file_list})  #returns the html page for the app


 
