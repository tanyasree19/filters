from django.shortcuts import render

# Create your views here.
def filters(request):
    import datetime
    dt=datetime.datetime.now()
    d={'name':'U are MY husband','count':1,'dt':dt}
    return render(request,'filters.html',d)

def userfilters(request):
    d={'name':'U are My husband'}
    return render(request,'userfilters.html',d)