
# Create your views here.
from django.shortcuts import render, redirect

data = {
    'name': 'Ram',
    'age': 20,
    'city': 'Delhi',
}

def welcome(request):
    return render(request, 'crud_app/index.html')

def create(request):
    if request.method == 'POST':
        key = request.POST['key']
        value = request.POST['value']
        data[key] = value
        return redirect('/read')
    return render(request, 'crud_app/create.html')

def read(request):
    return render(request, 'crud_app/read.html', {'data': data})

def update(request):
    if request.method == 'POST':
        key = request.POST['key']
        value = request.POST['value']
        if key in data:
            data[key] = value
        return redirect('/read')
    return render(request, 'crud_app/update.html')

def delete(request):
    if request.method == 'POST':
        key = request.POST['key']
        if key in data:
            del data[key]
        return redirect('/read')
    return render(request, 'crud_app/delete.html')
