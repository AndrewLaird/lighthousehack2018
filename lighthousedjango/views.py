from django.http import HttpResponse, JsonResponse
#from ..lighthousedjango import models


def success(request):
	return HttpResponse("that good succcc")
