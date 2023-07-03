from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import *
# Create your views here.
def home(request):
    if request.method=='POST':
        food_name=request.POST.get('search')
        try:
            reciepe=Reciepe_Details.objects.filter(food_name=food_name)
            context={'reciepe':reciepe}   
            return render(request,'reciepe/search_result.html',context=context)
        except:
            context={'info':"No Results"}
            
            return render(request,'reciepe/search_result.html',context=context)
    
    else:
        try:
            reciepe=Reciepe_Details.objects.filter(user_name=request.user)
            context={'reciepe':reciepe}   
            return render(request,'reciepe/home.html',context=context)
        except:
            return render(request,'reciepe/home.html')
        
    
    

def login_page(request):
    if request.method=='POST':
        username= request.POST.get('Username')
        password= request.POST.get('Password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print(user)
            print(request.POST)
            return redirect('home')
        
        print(user)

    return render(request,'reciepe/login.html')

def register_page(request):
    
    if request.method == 'POST': 
        form=UserCreationForm(request.POST)  
        if form.is_valid():  
            form.save()
            return redirect('home')
    else:
        form=UserCreationForm()
        context={
        'form':form
    }
 
    return render(request,'reciepe/register.html',context=context)

def logout_page(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login')
def add_reciepe_page(request):
    if request.method=='POST':
        form=Add_Reciepe_Form(request.POST,request.FILES)
        if form.is_valid():
            add_recipe = form.save(commit=False)
            add_recipe.user_name = request.user
            add_recipe.save()
            
            return redirect('home')
    
    else:
        form=Add_Reciepe_Form()
        context={
        'form':form
    }

    return render(request,'reciepe/add_reciepe.html',context=context)


def delete_item(request,pk):
    food_name=Reciepe_Details.objects.get(pk=pk)
    food_name.delete()
    return redirect('home')