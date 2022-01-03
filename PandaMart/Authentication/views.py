from django.shortcuts import render

# Create your views here.

def landingView (request):

    return render(request, 'Views/Landing.html')
    
def loginView ():
    pass

def RegistrationView():
    pass