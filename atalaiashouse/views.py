from django.shortcuts import render
from django.http import JsonResponse
from .forms import cadastro
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
def index(request):
    return render(request, "index.html")

def cadastro_novo(request, index):
    form = cadastro.objects.all()
    if request.method == "POST":
        form = cadastro(request.POST)
        if form.is_valid():
            cadastro = form.save(commit=False)
            cadastro.save()
            return HttpResponse('Recebemos o pedido de sua Encomenda')
    else:
        form = cadastro()

    return render(request, "index.html", {"form": form})
       

    print(request)
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = name(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = name()

    return render(request, "name.html", {"form": form})

