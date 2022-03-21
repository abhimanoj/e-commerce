#!/usr/bin/env python
 
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt 
from .models import *
from .constant import products
    

# Create your views here.
def cart_view(request):

    """
    View all cart items..
    """ 

    items_code = []
    if 'saved' in request.session:

        items_code = request.session['saved']

    all_products = ProductsTable.objects.filter(code__in=items_code)
        
    return render(request, 'cart.html', {'products':all_products})
    

# Create your views here.
def listing_view(request): 

    """
    Show all products listing..
    """

    all_products = ProductsTable.objects.all()
    
    if len(all_products) == 0:

        """
        Inserting Default data for items.
        """
        for items in products:
            ProductsTable.objects.create(
                **items
            )
        
        all_products = ProductsTable.objects.all()
        
    
    return render(request, 'products.html',{'products':all_products})
    

@csrf_exempt
def ajax_call_add_item_into_cart(request):

    if request.method == 'POST': 
        code = request.POST.get('code')
        action = request.POST.get('action', None)

        if action == 'ADD':
                

            if not 'saved' in request.session or not request.session['saved']:
                request.session['saved'] = [code]
            else:
                saved_list = request.session['saved']
                saved_list.append(code)
                request.session['saved'] = saved_list


        elif action == 'EMPTY':
            request.session['saved'] = ""
       
        if action == 'DELETE_ITEM':
                
            saved_list = request.session['saved']
            saved_list.remove(code)

            request.session['saved'] = saved_list

    return HttpResponse(True)


