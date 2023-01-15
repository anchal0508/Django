from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render, HttpResponse
tasks = ['foo','bar','teo']

class newTaskForm(forms.Form):
    task = forms.CharField(label='New Task :')
def  index(request):
    if request.method == "POST":
        fem = newTaskForm(request.POST)
        if fem.is_valid():
            task = fem.cleaned_data['task']
            tasks.append(task)
            return HttpResponseRedirect(reverse('app1:home'))
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