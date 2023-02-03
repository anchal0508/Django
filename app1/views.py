from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render, HttpResponse
tasks = ['foo','bar','teo']

class newTaskForm(forms.Form):
    tas = forms.CharField(label='New Task :', widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label='Name :', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # name = forms.CharField(label='name :')
    # Address = forms.CharField(label='Address :')

    
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