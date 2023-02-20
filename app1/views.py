from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render, HttpResponse
from app1.models import members
tasks = ['foo', 'bar', 'teo']


class newTaskForm(forms.Form):
    tas = forms.CharField(label='New Task :', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    name = forms.CharField(label='Name :', widget=forms.TextInput(
        attrs={'class': 'form-control'}))


    # name = forms.CharField(label='name :')
    # Address = forms.CharField(label='Address :')
m = {
    'num1': 0,
    'num2': 0,
    'result': 0,
}


def index(request):
    if request.method == "POST":
        fem = newTaskForm(request.POST)
        if fem.is_valid():
            task = fem.cleaned_data['tas']
            # n = fem.cleaned_data['name']
            # address = fem.cleaned_data['Address']
            tasks.append(task)
            return HttpResponseRedirect(reverse('app1:contact'))
        else:
            return render(request, 'app1/index.html', {
                'form': fem
            })
    return render(request, 'app1/index.html', {
        'form': newTaskForm()
    })


def contact(request):
    return render(request, 'app1/contact.html', {
        'task': tasks


    })
# v-------------------------- Math Formula --------------------------------------


class maths(forms.Form):
    num1 = forms.CharField(label='Number 1', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    op = forms.CharField(label='Operator', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    num2 = forms.CharField(label='Number 2', widget=forms.TextInput(
        attrs={'class': 'form-control'}))


def math(request):
    n1 = 0
    n2 = 0
    if request.method == "POST":
        fem = maths(request.POST)
        if fem.is_valid():
            # n1 = int(fem.cleaned_data['num1'])
            # n2 = int(fem.cleaned_data['num2'])
            m['num1'] = (fem.cleaned_data['num1'])
            m['num2'] = (fem.cleaned_data['num2'])
            f = (fem.cleaned_data['op'])
            v = m['num2']+f+m['num1']

            m['result'] = eval(v)
            print((m['result']))
            # return HttpResponseRedirect(reverse('app1:math'))
        else:
            return render(request, 'app1/Math.html', {
                'M_form': fem,
                'r': 0
            })
    return render(request, 'app1/Math.html', {
        'M_form': maths(),
        'r': m['result'],

    })


def table(request):
    data = members.objects.all()
    # for i in data:
    #     print(i['name'])
    print(f'{data} data is')
    data2 = {
        'Ttable': data
    }
    return render(request, 'app1/table.html', data2)


class newRegistration(forms.Form):
    name = forms.CharField(label='Name  :', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    lastName = forms.CharField(label='Last Name :', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    FatherName = forms.CharField(label='Father"s Name :', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    Address = forms.CharField(label='Address :', widget=forms.TextInput(
        attrs={'class': 'form-control'}))


def reg(request):

    if request.method == "POST":
        fem = newRegistration(request.POST)
        if fem.is_valid():
            Name = (fem.cleaned_data['name'])
            LastName = (fem.cleaned_data['lastName'])
            FatherName = (fem.cleaned_data['FatherName'])
            Address = (fem.cleaned_data['Address'])
            dt = members(name = Name, lastName = LastName, father = FatherName, address = Address)
            dt.save()
            
        else:
            return render(request, 'app1/reg.html', {
                'form': fem,
                
            })
    return render(request, 'app1/reg.html', {
        'form': newRegistration(),
         

    })
