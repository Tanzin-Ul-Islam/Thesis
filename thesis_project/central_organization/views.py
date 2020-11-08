from django.shortcuts import render
from django.http import HttpResponse
from central_organization.models import Central_model
# Create your views here.

def index(req):
    diction={}
    if req.method=='POST':
        store = Central_model()
        store.first_name = req.POST.get('firstname')
        store.last_name = req.POST.get('lastname')
        store.father_name = req.POST.get('fathername')
        store.mother_name = req.POST.get('mothername')
        store.dob = req.POST.get('dob')
        store.address = req.POST.get('address')
        store.finger_print = req.POST.get('fingerprint')
        store.blood_group = req.POST.get('bloodgroup')
        store.gender = req.POST.get('gender')
        store.maritual_state = req.POST.get('maritualstate')
        store.save()
        diction.update({'success':'Successfully submited'})
    return render(req,'central_organization/add_form.html', context=diction)

def finger_print_process(req):
    diction={'fingerprint':'success'}
    return render(req, 'central_organization/add_form.html', context=diction)