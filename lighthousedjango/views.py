from django.http import HttpResponse


def success(request):
	return HttpResponse("that good succcc")
