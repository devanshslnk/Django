# from django.shortcuts import render
# from django.http import HttpResponse
# from django.shortcuts import render
# from .models import Album

# def index(request):

	# all_album=Album.objects.all()
	# html=''
	# for a in all_album:
	# 	url=("/"+str(a.id)+"/")
	# 	html+='<a href="'+url+'">'+a.album_name+'</a><br>'

	
	# return HttpResponse(html)
	# template=loader.get_template('music/index.html')
	
	#----------------------------------------------------------------------
	#OR

	# all_album=Album.objects.all()
	# context={"all_album":all_album,}
	# return render(request,'music/index.html',context)


# def details(request,album_id):
	#----------------------------------------------------------------------
	# all_album=Album.objects.filter(id=album_id)
	# html=''                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
	# for a in all_album:
	# 	url=("/"+str(a.id)+"/")
	# 	html+='<h1>'+a.arstist+'</h1><br>'
	#-------------------------------------------------------------------------
	# OR
	
	# all_album=Album.objects.get(id=album_id)
	# return render(request,"music/details.html",{"all_album":all_album,})
	#--------------------------------------------------------------------------

	

# Create your views here.



from django.views import generic
from .models import Album,Song
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic  import View
from django.http import HttpResponseRedirect
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django import forms



class IndexView(generic.ListView):
	template_name="music/index.html"
	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	model=Album
	template_name="music/details.html"

class AlbumCreate(CreateView):
	model=Album
	fields=['arstist','album_name','album_code']
	# form_class=

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')

    else:
        form = UserRegistrationForm()

    return render(request, 'music/register.html', {'form' : form})