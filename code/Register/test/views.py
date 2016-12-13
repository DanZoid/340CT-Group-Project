from django.contrib.auth import authenticate, login #Pulling Built in Django Authentication and Login function
from django.contrib.auth import logout #Pulling Built in Django Logout function 
from django.shortcuts import render #Pulls render function so users can render webpage 
from .forms import UserForm #From the current directory import function UserForm from forms.py 

def index(request): #If this is a POST request, process the form data 
        return render(request, 'test/index.html') #When function index is called render file within test folder called index.html


def logout_user(request): #If this is a POST request, process the form data 
    logout(request)  
    form = UserForm(request.POST or None) #Display form UserForm from class within forms.py 
    context = { 
        "form": form, #Calling the value in the dictionary of form to be called before rendering the template 
    }
    return render(request, 'test/index.html', context) #Render the html page index.html within test folder 


def login_user(request): #If this is a POST request, process the form data
    if request.method == "POST": #Create a form instance and populate it with data from the request  
        username = request.POST['username'] #Check whether username is valid
        password = request.POST['password'] #Check whether password is valid
        user = authenticate(username=username, password=password) #Authenticate the username and password entered to form to database entries   
        if user is not None: #Backend authenticated credentials
            if user.is_active: #If the user account is active in db 
                login(request, user) # Log the user in
                return render(request, 'test/index.html') #Then return user to index.html 
        else:
            return render(request, 'test/login.html', {'error_message': 'Invalid login'}) #Else show an invalid login error message
    return render(request, 'test/login.html') #Return User to login.html 


def register(request): #If this is a POST Request, process the form data 
    form = UserForm(request.POST or None) #Display the form UserForm that is specified in forms.py 
    if form.is_valid(): #All fields of the model are required, make sure all fields are filled in correctly and not left blank
        user = form.save(commit=False) #Save a new user from the form's data 
        username = form.cleaned_data['username'] #The validated username data will be in the form.cleaned_data dictionary
        password = form.cleaned_data['password'] #The validated password will be stored in the form.cleaned_data dictionary
        user.set_password(password) #Set the user's password to the password that was entered into the form
        user.save() #Save the user 
        user = authenticate(username=username, password=password) #Check to see whether a user already exists with the username and password
        if user is not None: #Backend authenticated credentials
            if user.is_active: #If user is active in the backend once registered successfully 
                login(request, user) #Refers to django.contrib.auth login, login user
                return render(request, 'test/index.html') #Return user to index.html
    context = {
        "form": form, #Calling the value in the dictionary of form to be called before rendering the template
    }
    return render(request, 'test/register.html', context)

