from django.shortcuts import render

# Create your views here.

def forloop(request):

    D={'name':{'uday','venkesh','shyam'}}

    return render(request,'forloop.html',context=D)
