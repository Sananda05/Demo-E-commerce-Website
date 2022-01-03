from django.shortcuts import render

# Create your views here.

def landingView (request):

    return render(request, 'Views/Landing.html')
    
def loginView (request):
    return render(request, 'Views/Authentication/Login.html')

def RegistrationView(request):
    return render(request, 'Views/Authentication/Registration.html')