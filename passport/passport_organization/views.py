from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(req):
    return render(req, 'passport_organization/fingerprint_form.html')

def finger_print(req):
    diction={'fingerprint':'success'}
    return render(req, 'passport_organization/fingerprint_form.html', context=diction)

def apply_passport(req):
    diction={}
    if req.method == 'POST':
        a=req.POST.get('fingerprint')
        diction.update({'a':a})
        return render(req, 'passport_organization/apply_passport_form.html', context=diction)

# def store(req):
