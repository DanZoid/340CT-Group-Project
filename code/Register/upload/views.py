from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse

from upload.models import Document
from upload.forms import docform

def upload(request):
    if request.method == 'POST':
        form = docform(request.POST, request.FILES)
        if form.is_valid():
            dan = Document (newfile=request.FILES['newfile'])
            dan.save()
        return HttpResponseRedirect(reverse('upload'))
    else:
        form = docform()

    return render(request, 'upload.html', )

