from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category

def index(request):
	category_list = Category.objects.order_by('-likes')
	context_dict = {'categories': category_list}

	return render(request, 'rango/index.html', context_dict)


def about(request):
	fun_facts = {'italicmessage': "the best dad ever! He should get father of the year!"}
	return render(request, 'rango/about.html', fun_facts)

