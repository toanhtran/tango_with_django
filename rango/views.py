from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category
from rango.models import Page

def index(request):
	category_list = Category.objects.order_by('-likes')
	context_dict = {'categories': category_list}

	return render(request, 'rango/index.html', context_dict)


def about(request):
	fun_facts = {'italicmessage': "the best dad ever! He should get father of the year!"}
	return render(request, 'rango/about.html', fun_facts)

def category(request, category_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages 
        context_dict['category'] = category

    except Category.DoesNotExist:
         
        pass

    # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)
