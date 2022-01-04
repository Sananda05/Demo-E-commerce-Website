from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import make_password
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
        c_password = request.POST['C_password'],

        encrypt_pass = make_password(str(password))

        print(password[0]+ "pass")
        

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

        elif (Valid_password_lowercase(str(password[0]))== False):
            alert="Password must contain a lowercase letter"
            return render(request, 'Views/Authentication/Registration.html' , {'alert':alert})

        elif (Valid_password_uppercase(str(password[0]))== False):
            alert="Password must contain a uppercase letter"
            return render(request, 'Views/Authentication/Registration.html' , {'alert':alert}) 

        elif (Valid_password_specialChar(str(password[0]))== False):
            alert="Password must contain a special character"
            return render(request, 'Views/Authentication/Registration.html' , {'alert':alert})
        elif(Valid_password_digit(str(password[0]))==True):
            alert="First digit cannot be a number"
            return render(request, 'Views/Authentication/Registration.html' , {'alert':alert})



        else:    

            if password[0] == c_password[0]:
                user = User.objects.create(first_name= f_name,last_name=l_name, username = username, email=email,password=encrypt_pass )
                user.save()
                print("user created")
                return redirect('/')
            else:
                alert="Password not matching"
                return render(request, 'Views/Authentication/Registration.html' , {'alert':alert})


    else:    
        return render(request, 'Views/Authentication/Registration.html')


def Valid_password_lowercase(password):

    if not any(char.islower() for char in password):
        return False
    

def Valid_password_uppercase(password):
    if not any(char.isupper() for char in password):
        return False                   

def Valid_password_specialChar(password):
    
    special_characters = """!@#$%^&*()-+?_=,<>/""" 

    if any(c in special_characters for c in password):
        return True
    else:
        return False

def Valid_password_digit(password):

    if (password[0].isdigit()):
        print(password[0])
        return True                      