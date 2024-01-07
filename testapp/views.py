from django.shortcuts import render
from testapp.models import Student
from  testapp.forms import studentform
# Create your views here.
from django.http import HttpResponse

def vi(request):
    s={'abc':123}
    return render(request,'testapp/base.html',context=s)
def stuview(request):
    stulist=Student.objects.all()
    # stulist= Student.objects.filter(rno__gt=30)
    # stulist = Student.objects.filter(name__startswith='d')
    dic = {'stulist':stulist}
    return render(request,'testapp/base.html',context=dic)
def studentview(request):
    form = studentform()
    if request.method == 'POST':
        form = studentform(request.POST)
        if form.is_valid():
            print("form validation")
            print("name",form.cleaned_data['name'])
        form=studentform()
    return render(request,'testapp/fm.html',{'form':form})
