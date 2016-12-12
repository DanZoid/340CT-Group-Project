from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse

from upload.models import Document
from upload.forms import docform
                
def upload(request):                                                    #This part of the code controls the upload function
    if request.method == 'POST':
        form = docform(request.POST, request.FILES)                     #Creates a POST method for the upload system 
        if form.is_valid():                                             #If the form is valid proceed with the upload
            dan = Document (newfile=request.FILES['newfile %y %m d%'])  #This takes the file add Newfile to the tag with the year, month, and day     
            dan.save()                                                  #Set the save location as located within Settings.py Django
        return HttpResponseRedirect(reverse('upload'))                  #Once complete this would send the user back to the Upload.html 
    else:
        form = docform()                                                #Else this would create a blank form for the user to attempt upload
    return render(request, 'upload.html', )                             #This will then return the user back to the html webpage

