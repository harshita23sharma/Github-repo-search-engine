from django.http import HttpResponse

from django.template import loader
from django.template.loader import get_template
# def index(request):
#     latest_question_list = ['a','b','c']
#     template = loader.get_template('product/index.html')
#     context = {
#         'latest_question_list': 'string',
#     }
#     return HttpResponse(template.render(context, request))

from my_backend.load_search import find_file
from django.shortcuts import render
from django.http import HttpResponseRedirect

from product.forms import NameForm
from product.forms import SelectForm
import os,sys
import config
# from tests.unit_tests import run_all_tests
INDEX = '/product/templates/product/index.html'
def name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = NameForm(request.POST)
        result = str(form["your_product"].value())
        q_param = form["your_product"].value()
        resultt , search_r = find_file(q_param)
        # check whether it's valid:
        if form.is_valid():
            # print(form["your_product"].value())
            return render(request, "selected.html" , {'resultt':resultt,'search_results' : search_r})        
    else:
        form = NameForm()

    return render(request, 'selected.html', {'form': form})

def results(request):  
    return render(request, 'results.html')

def index(request):
    # TEMPLATE_PATH =os.path.join(os.getcwd(), INDEX)
    print("os.getcwd... ",os.getcwd())
    TEMPLATE_PATH = os.getcwd() + INDEX
    template = get_template(TEMPLATE_PATH)
    context = {
        'key': 'value',
    }
    return HttpResponse(template.render(context, request))

def selected(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = SelectForm(request.POST)
        resultt = (form["selected_choice"].value())
        print(form["selected_choice"].value())
        # check whether it's valid:
        if form.is_valid():
            print("debug_inside")
        else:
            print("debug !form is_valid")
    
        return render(request, "selected.html" , {'form' : form,'resultt':resultt})
# def test(request):
#     if request.method == 'GET':
#         unit_tests.run_all_tests()


    
