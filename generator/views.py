from django.shortcuts import render
import random

def home(request):
    return render(request,'generator/home.html')

def about(request):
    return render(request,'generator/about.html')

def generated(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0987654321'))
    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*?><'))
    length = int(request.GET.get('length',8))
    thepassword  = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request,'generator/generated.html', {'password':thepassword})
