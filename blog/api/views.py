# from rest_framework.http import Response
from django.http import JsonResponse

def blogs(request):
    return JsonResponse(data={
        'message': 'Success!'
    }, )
