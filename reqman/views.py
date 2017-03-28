from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Request

def index(req):
    latest_request_list = Request.objects.order_by('-date_created')[:5]
    context = {'latest_request_list': latest_request_list}
    return render(req, 'reqman/index.html', context)

def detail(req, request_id):
    request = get_object_or_404(Request, pk = request_id)
    return render(req, 'reqman/detail.html', {'request': request})
