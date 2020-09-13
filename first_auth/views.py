from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string

from django.http import HttpResponse
from first_auth.forms import signinform
from django.contrib import messages
from django.contrib.auth import authenticate
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from django.contrib.auth.models import User,auth
from django.shortcuts import get_object_or_404

from pkgutil import get_data




from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import readers,story


from django.db.models import F


# def home(request):
#     return render(request,'story_list.html')



def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print("POST")
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=password)
            print("valid")
            username = form.cleaned_data.get('username')
            read=readers(username=username)
            read.save()
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'extra.html')
    else:
        form = UserCreationForm()
        print("no")
    return render(request, 'sign_up.html', {'form': form})








# class showstories(ListView):
#     template_name = 'story_list.html'
#     context_object_name = 'stories_list'
    

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return story.objects.all()


class home(ListView):
    template_name = 'story_list.html'
    context_object_name = 'stories_list'
    

    def get_queryset(self):
        """Return the last five published questions."""
        return story.objects.all()


class story_details(DetailView):
    
    #stry=get_object_or_404(story,pk=story_id)
    #print("A")
    
    #stry1=stry.current_view+1
    #str1=story(current_view=story.current_view)
    #stry.current_view.set(stry1)
    model=story
    
    template_name='story_details.html'


    def get_object(self, queryset=None):

        context=super().get_object(queryset=queryset)
        context.current_view.add(self.request.user)
        return context
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     cats=story.objects.all()
    #     context = super().get_context_data(**kwargs)
        
    #     return context


   


def count_reader(request,story_id):
    
    comp=get_object_or_404(story,pk=story_id)
    b=comp.current_view.remove(request.user)
    total1=comp.total1()   
    
    # a=story(total_read=User.username)
    a=comp.total_read.add(request.user)
    total=comp.total()
    #print(total)
    comp.save()
  
    
    
    return render(request,'extra.html')




def logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return render(request,'logout.html')




# Create your views here.
