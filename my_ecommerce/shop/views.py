from django.template import loader
from django.http import HttpResponse

# Create your views here.
def shop(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())