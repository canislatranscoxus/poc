from django.shortcuts import render

# Create your views here.

def home( request ):
    #
    #animals = Animal.objects.all
    #return render( request, "home.html", { "animals" : animals } )
    return render( request, "home.html" )

    