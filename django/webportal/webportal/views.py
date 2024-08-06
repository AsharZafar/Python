from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    data= {'name':'Ashar','school':'fss'}
    return render(request,'index.html',data)

def about(request):

    return render(request,'about.html')
    
def contact(request):

    return render(request,'contact.html')
    