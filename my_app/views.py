from django.shortcuts import render, redirect
from .models import user_table

# Create your views here.

def retrieve(request):
    Context={
        'datas':user_table.objects.all()
    }
    return render(request,"retrieve.html",Context)

def create(request):
    if request.method=='POST':
        input_name = request.POST.get('name','')
        input_contact = request.POST.get('contact','')
        user = user_table(name=input_name,contact=input_contact)
        user.save()
        return redirect('retrieve_url')
    elif request.method=='GET':
        return render(request,"create.html")
    
def update(request,id):
    user_data = user_table.objects.get(id=id)
    if request.method=='POST':
        user_data.name = request.POST.get('name','')
        user_data.contact = request.POST.get('contact','')
        user_data.save()
        return redirect('retrieve_url')
    elif request.method=='GET':
        Context={
            'datas':user_data
        }
        return render(request,"update.html",Context)
    
def delete(request,id):
    user_table.objects.get(id=id).delete()
    return redirect('retrieve_url')
