from django.shortcuts import render, redirect
from .models import Message
# Create your views here.
def create(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    else:
        username = request.POST['name']
        message =  request.POST['message']
        mobile =  request.POST['mobile']
        email =  request.POST['email']

        userdata = Message.objects.create(name = username, message = message, email = email, mobile=mobile)
        userdata.save()
        return render(request, 'home.html')

def dashboard(request):
    data = Message.objects.all()
    return render(request, 'dashboard.html', {'datas': data})

def edit(request, sid):
    if request.method == 'GET':
        foredit = Message.objects.filter(id = sid)
        context = {}
        context['data'] = foredit
        return render(request, 'edit.html', context)
    else:
        username = request.POST['name']
        message =  request.POST['message']
        mobile =  request.POST['mobile']
        email =  request.POST['email']
        
        Message.objects.filter(id = sid).update(name = username, email = email, mobile = mobile, message= message )
        
        return redirect('/dashboard')
    
def delete(request, did):
    delete = Message.objects.filter(id= did)
    delete.delete()
    return redirect('/dashboard')