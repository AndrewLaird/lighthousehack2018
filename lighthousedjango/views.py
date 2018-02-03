from django.http import HttpResponse, JsonResponse

def success(request):
	return HttpResponse("that good succcc")
