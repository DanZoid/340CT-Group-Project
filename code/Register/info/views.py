from django.http import HttpResponse
from django.template import loader
from .models import Modules, Marks


def index(request):
    all_marks = Marks.objects.all()
    template = loader.get_template('info/index.html')
    context = {
        'all_marks': all_marks,
    }
    return HttpResponse(template.render(context, request))
