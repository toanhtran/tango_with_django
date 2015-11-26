from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "Full Stack Developer for PowerToFly!"}
    return render(request, 'rango/index.html', context_dict)


def about(request):
	fun_facts = {'italicmessage': "This is my year! Anything I put my mind to I accomplish."}
	return render(request, 'rango/about.html', fun_facts)

