from django.http import HttpResponse
from ..lighthousedjango import models

def success(request):
	return HttpResponse("that good succcc")
