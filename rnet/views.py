from django.http import Http404
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def main(request):
    return render(request, 'index.html')

@csrf_exempt
def search(request):
    res = [
        ['http://www.jjc.edu/admissions/PublishingImages/radiology.jpg','result1','impression'],
        ['http://www.jjc.edu/admissions/PublishingImages/radiology.jpg','result2','impression'],
        ['http://www.jjc.edu/admissions/PublishingImages/radiology.jpg','result3','impression'],
    ]
    return JsonResponse(res,safe=False)
