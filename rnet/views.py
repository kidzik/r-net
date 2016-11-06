from django.http import Http404
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rnet.interface import get_list

def main(request):
    return render(request, 'index.html')

@csrf_exempt
def search(request):
    ll = get_list(request.POST['s'])
    return JsonResponse(ll,safe=False)
