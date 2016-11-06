from django.http import Http404
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rnet.interface import get_list
import re

def main(request):
    return render(request, 'index.html')

@csrf_exempt
def search(request):
    procedure = re.split("\\s+",request.POST['s'])[0].strip()
    if not (procedure in ['CHEST','KNEE','NECK']):
        procedure = ""
    dd = {
        'CHEST': 'http://www.jjc.edu/admissions/PublishingImages/radiology.jpg',
        'KNEE': 'https://www.mypacs.net/repos/mpv3_repo/viz/full/0/3/253/3405443.jpg',
        'NECK': 'http://vitalim.ca/wp-content/uploads/neck-soft-tissues-260x300.png',
        '': 'http://www.jjc.edu/admissions/PublishingImages/radiology.jpg',
    }
    ll = get_list(request.POST['s'], procedure)[:5]
    for i in range(len(ll)):
        ll[i].append(dd[procedure])

    return JsonResponse(ll,safe=False)
