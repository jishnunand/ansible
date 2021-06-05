import datetime
import json

from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404, HttpResponse

from .models import Bill

def index(request, *args, **kwargs):
    items = Bill.objects.all().order_by('-bill_date')
    return render(request, 'index.html', {'data': items})

def uploadfile(request, *args, **kwargs):
    if request.method == 'POST':
        return HttpResponse('post succesfully')
    else:
        return HttpResponse('get succesfully')

def view(request, *args, **kwargs):
    id = kwargs.get('id', None)
    if id:
        try:
            p = Bill.objects.get(bill_no=id)
        except Bill.DoesNotExist:
            raise Http404
    else:
        raise Http404
    return render(request, 'list.html', {'data': p})

def delete(request, *args, **kwargs):
    id = kwargs.get('id', None)
    if id:
        try:
            p = Bill.objects.get(bill_no=id)
            p.delete()
        except Bill.DoesNotExist:
            raise Http404
    else:
        raise Http404
    return redirect('/')


def add_new(request):
    if request.method == 'POST':
        bill_date = datetime.datetime.now()
        data_input = json.loads(request.POST.get('data',{}))
        print(data_input)
        try:
            patient_name = data_input['patient_name']
            patient_age = data_input['patient_age']
            item = data_input['item']
            amount_for_one = data_input['amount_for_one']
            tax = data_input['tax']
            discount = data_input['discount']
            balance = data_input.get('balance', None)
            address = data_input.get('address', None)
            bill_date_str = data_input.get('bill_date', None)
            number_of_item = data_input.get('number_of_item', 1)
            if bill_date_str:
                bill_date = datetime.strptime(bill_date_str,'%d-%m-%Y')
        except Exception as key_error:
            result = {'Error':'missing key: %s' %str(key_error)}
            return JsonResponse({'recived':result})
        try:
            bill_object = Bill(patient_name=patient_name,patient_age=patient_age,
                               item=item, amount_for_one=amount_for_one, tax=tax,
                               discount=discount, number_of_item=number_of_item,
                               address=address, bill_date=bill_date)
            bill_object.save()
        except Exception as model_update_error:
            result = {'Error':str(model_update_error)}
            return JsonResponse({'recived':result})
        return JsonResponse({'msg':'added succesfully'})
    else:
        return render(request, 'add.html')
