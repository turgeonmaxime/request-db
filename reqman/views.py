from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Request, Analyst, Database, Stakeholder
from .forms import RequestForm

# Main page
def index(req):
    latest_request_list = Request.objects.order_by('-date_created')[:5]
    context = {'latest_request_list': latest_request_list}
    return render(req, 'reqman/index.html', context)

# Individual detail page
def detail(req, request_id):
    request = get_object_or_404(Request, pk = request_id)
    return render(req, 'reqman/detail.html', {'request': request})

def analyst(req, analyst_id):
    request = get_object_or_404(Analyst, pk = analyst_id)
    return render(req, 'reqman/analyst.html', {'analyst': request})

def db(req, db_id):
    request = get_object_or_404(Database, pk = db_id)
    return render(req, 'reqman/db.html', {'db': request})

def stake(req, stake_id):
    request = get_object_or_404(Stakeholder, pk = stake_id)
    return render(req, 'reqman/stake.html', {'stake': request})

# List of instances
def analyst_list(req):
    analyst_list = Analyst.objects.all()
    context = {'analyst_list': analyst_list}
    return render(req, 'reqman/analyst_list.html', context)

def db_list(req):
    db_list = Database.objects.all()
    context = {'db_list': db_list}
    return render(req, 'reqman/db_list.html', context)

def stake_list(req):
    stake_list = Stakeholder.objects.all()
    context = {'stake_list': stake_list}
    return render(req, 'reqman/stake_list.html', context)

# Forms
def request_new(req):
    # if this is a POST request we need to process the form data
    if req.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RequestForm(req.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('reqman:detail', args=(request.id,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RequestForm()

    return render(req, 'reqman/request.html', {'form': form})

