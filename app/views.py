from django.shortcuts import render

# Create your views here.
def bhavani(request):
    d={'name':'reddy','age':6}
    return render(request,'bhavani.html',context=d)