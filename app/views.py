from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='data is our assumtion'
    d={'assumtion':data}
    return render(request,'data_render.html',context=d)

def login(request):
    data='data is our username'
    n={'username':data,'age':3}
    return render(request,'login.html',context=n)
