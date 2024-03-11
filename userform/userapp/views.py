from django.shortcuts import render
from .forms import userDetails
from .models import userForm
# Create your views here.
def userdetails(request):
    if request.method == 'POST':
        form = userDetails(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = userDetails()

    return render(request, 'index.html', {'form' : form})

def showUser(request):
    users = userForm.objects.all()
    return render(request, 'show.html', {'users':users})