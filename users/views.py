from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from moviepy.editor import *
import json

from users.functions import handle_uploaded_file  
from users.functions import merge_videos  
from users.forms import CreateForm  
from users.models import VideoLib



def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})
@login_required()
def index(request):  
    # /form_data = json.loads(request.data)
    # exit()
    if request.method == 'POST':  
        vid_lib = VideoLib()
        vid_lib.name = request.POST.get('name')
        vid_lib.mobile = request.POST.get('mobile')
        
        saved_path = handle_uploaded_file(request.FILES['file'])  

        print(saved_path)
        #vid_lib.file = saved_path
        
        vid_lib.save()
        # merge_videos()
        return redirect("/list")          
            
    else:  
        video = CreateForm()  
        return render(request,"users/index.html",{'form':video})
@login_required()
def show(request):  
    videos = VideoLib.objects.all()  
    return render(request,"users/show.html",{'videos':videos})    

def destroy(request, id):  
    video = VideoLib.objects.get(id=id)  
    video.delete()  
    return redirect("/list")        



@login_required()
def profile(request):
    return render(request, 'users/profile.html')

    
