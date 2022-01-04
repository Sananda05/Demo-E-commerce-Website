from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def landingView (request):

    return render(request, 'Views/Landing.html')
    
def loginView (request):
    return render(request, 'Views/Authentication/Login.html')

def RegistrationView(request):

    if request.method == "POST":

        f_name = request.POST['fname'],
        l_name = request.POST['lname'],
        username = request.POST['name'],
        email = request.POST['email'],
        password = request.POST.get('password'),
        c_password = request.POST['C_password']

        print(password)

        if User.objects.filter(username=username).exists():

            alert="Username is already taken"
            return render(request, 'Views/Authentication/Registration.html' , {'alert':alert})

        if User.objects.filter(email=email).exists():

            alert="Email is already taken"
            return render(request, 'Views/Authentication/Registration.html' , {'alert':alert})    


        if len(password[0])<8:
            print(len(password[0]))
            alert="Password length cannot be less than 8"
            return render(request, 'Views/Authentication/Registration.html' , {'alert':alert})
        else:    

            if password[0] == c_password[0]:
                user = User.objects.create(first_name= f_name,last_name=l_name, username = username, email=email,password=password )
                user.save()
                print("user created")
                return redirect('/')
            else:
                alert="Password not matching"
                return render(request, 'Views/Authentication/Registration.html' , {'alert':alert})


    else:    
        return render(request, 'Views/Authentication/Registration.html')