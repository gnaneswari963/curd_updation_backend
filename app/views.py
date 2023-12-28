from django.shortcuts import render
from app.models import *

# Create your views here.
def update_access_record(request):
    qlar=AccessRecord.objects.filter(name='gnan').update(author='krishna')
    qlar=AccessRecord.objects.filter(author='xyz').update(name='gnan')
    
    QLAR=AccessRecord.objects.all()
    d={'ar':QLAR}
    return render(request,'update_access_record.html',context=d)

def update_or_create(request):
   
    wo=Webpage.objects.get(name='nani')
    qlar=AccessRecord.objects.update_or_create(name='mokshi',defaults={'author':'son'})
    qlar=AccessRecord.objects.update_or_create(author='abc',defaults={'name':wo})
    wo=Webpage.objects.get(name='nani')
    qlar=AccessRecord.objects.update_or_create(author='qqq',date='2000-09-22',defaults={'name':wo})
    QLAR=AccessRecord.objects.all()
    d={'ar':QLAR}
    return render(request,'update_or_create.html',context=d)