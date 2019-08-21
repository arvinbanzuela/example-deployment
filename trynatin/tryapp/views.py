from django.shortcuts import render

def index(request):
    my_dict = {'insert_here':'Hello world'}
    return render(request,'firstapp/index.html',context = my_dict)
# Create your views here.
