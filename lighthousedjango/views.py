from lighthousehack2018.lighthousedjango.models import Event
from django.http import HttpResponse, JsonResponse
from . import models


def success(request):
	return HttpResponse("that good succcc")
