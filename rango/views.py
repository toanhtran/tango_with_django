from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "handsome man!"}
    return render(request, 'rango/index.html', context_dict)


def about(request):
	fun_facts = {'italicmessage': "the best dad ever! He should get father of the year!"}
	return render(request, 'rango/about.html', fun_facts)

