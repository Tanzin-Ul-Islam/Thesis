from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from central_organization.models import Central_model
# Create your views here.
def passport_index(req):
    diction = {}
    if req.method == 'POST':
        id = req.POST.get('id')
        data = Central_model.objects.get(pk=id)
        if data.finger_print == req.POST.get('fingerprint'):
            diction.update({'data':data})
            return render(req, 'passport_organization/apply_passport_form.html', context=diction)
        else :
            diction.update({'message':"Fingerprint did not matched!!!"})
            return render(req, 'passport_organization/fingerprint_form.html', context= diction)
        # if data[] == req.POST.get('fingerprint'):
        #     diction.update({'data':data})
        #     return render(req, 'passport_organization/apply_passport_form.html', context = diction)
        # else:
        #     diction.update({'message':'Finger Print did not matched!!!'})
        #     return render(req, 'passport_organization/fingerprint_form.html', context = diction)
    return render(req, 'passport_organization/fingerprint_form.html')

def finger_print(req):
    diction={'fingerprint':'hello_success'}
    return render(req, 'passport_organization/fingerprint_form.html', context = diction)

