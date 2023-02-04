from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render, HttpResponse
from app1.models import members
tasks = ['foo','bar','teo']

class newTaskForm(forms.Form):
    tas = forms.CharField(label='New Task :', widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label='Name :', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # name = forms.CharField(label='name :')
    # Address = forms.CharField(label='Address :')
m = {
    'num1':0,
    'num2':0,
    'result':0,
}
class maths(forms.Form):
    num1 = forms.CharField(label='Number 1', widget=forms.TextInput(attrs={'class': 'form-control'}))
    num2 = forms.CharField(label='Number 2', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
def  index(request):
    if request.method == "POST":
        fem = newTaskForm(request.POST)
        if fem.is_valid():
            task = fem.cleaned_data['tas']
            # n = fem.cleaned_data['name']
            # address = fem.cleaned_data['Address']
            tasks.append(task)
            return HttpResponseRedirect(reverse('app1:contact'))
        else:
            return render(request, 'app1/index.html',{
                'form':fem
            })
    return render(request, 'app1/index.html',{
        'form':newTaskForm()
    })

def contact(request):
    return render(request, 'app1/contact.html',{
        'task':tasks
    })
def  math(request):
    n1=0
    n2=0
    if request.method == "POST":
        fem = maths(request.POST)
        if fem.is_valid():
            # n1 = int(fem.cleaned_data['num1'])
            # n2 = int(fem.cleaned_data['num2']) 
            m['num1']  = int(fem.cleaned_data['num1'])
            m['num2'] = int(fem.cleaned_data['num2']) 
            m['result'] =m['num2']+m['num1']
            print(m['result'])
            # return HttpResponseRedirect(reverse('app1:math'))
        else:
            return render(request, 'app1/Math.html',{
                'M_form':fem,
                'r':0
            })
    return render(request, 'app1/Math.html',{
        'M_form':maths(),
        'r':m['result'],
        
    })

def table(request):
    data = members.objects.all()
    # for i in data:
    #     print(i['name'])
    # print(data.name)
    data2 = {
        'Ttable':data
    }
    return render(request,'app1/table.html',data2)