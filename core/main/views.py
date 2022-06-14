from  asyncio.log import logger
from ipaddress import ip_address
from django.dispatch import receiver
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, View, FormView, TemplateView
from paypal.standard.forms import PayPalPaymentsForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# from django.urls import reversefrom  asyncio.log import logger
from ipaddress import ip_address
from django.dispatch import receiver
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, View, FormView, TemplateView
from paypal.standard.forms import PayPalPaymentsForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse
# from django.contrib.auth.models import User
from .models import HomeBackground, TureIdea, AboutAs, TinksForTourism, BookForHotels, CommentsCustomer, OurServices, NextTravel, SubscirbeNow, AboutusPage1st, AboutusPage2th, AboutusPage3th, BlogPage, BlogPageToSupport, UserContact
from .forms import  NewUserForm

# Create your views here.


class TouristPageListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        homes = HomeBackground.objects.all()
        tours = TureIdea.objects.all()
        abouts = AboutAs.objects.all()
        tinks = TinksForTourism.objects.all()
        books = BookForHotels.objects.all()
        commentsCustomer = CommentsCustomer.objects.all()
        ourServices1 = OurServices.objects.all()
        nextTravels = NextTravel.objects.all()
        subscirbe = SubscirbeNow.objects.all()
    
        return render(request, 'index.html', {'homes':homes, 'tours':tours, 'abouts': abouts, 'tinks':tinks, ' books': books, 'commentsCustomer':commentsCustomer, 'ourServices1':ourServices1, 'nextTravels':nextTravels, 'subscirbe':subscirbe})


class TouristPageDetailView(DetailView):
    template_name = 'index_detail.html'

    def get(self, request, id):
        home = HomeBackground.objects.get(pk=id)
        return render(request, self.template_name, {'home':home,})


class TouristPageToursDetailView(DetailView):
    template_name = 'index_detail_tours.html'

    def get(self, request, id):
        tour = TureIdea.objects.get(pk=id)
        return render(request, self.template_name, {'tour':tour})

class NextTravelDetailView(DetailView):
    template_name = 'index_nextTravel_detail.html'

    def get(self, request, id):
        nextTravel = NextTravel.objects.get(pk=id)
        return render(request, self.template_name, {'nextTravel': nextTravel})



class TouristTinksDetailView(DetailView):
    template_name = 'tinks_detail.html'

    def get(self, request, id):
        tink = TinksForTourism.objects.get(pk=id)
        return render(request, self.template_name, {'tink':tink})





def aboutus(request):
    aboutusPage1st = AboutusPage1st.objects.all()
    aboutusPage2th = AboutusPage2th.objects.all()
    aboutusPage3th = AboutusPage3th.objects.all()
    return render(request, 'aboutus.html', {'aboutusPage1st':aboutusPage1st, 'aboutusPage2th':aboutusPage2th, 'aboutusPage3th':aboutusPage3th})




class BlogListView(ListView):
    template_name = 'blog.html'

    def get(self, request):
        blogs = BlogPage.objects.all()
        blogPageToSupports = BlogPageToSupport.objects.all()
        return render(request, self.template_name, {'blogs':blogs, 'blogPageToSupports':blogPageToSupports})


class BlogDetailView(DetailView):
    template_name = 'blog_detail.html'

    def get(self, request, id):
        blogPageToSupport = BlogPageToSupport.objects.get(pk=id)
        return render(request, self.template_name, {'blogPageToSupport':blogPageToSupport})

# ------------ Stays.html---------------------------------------------
def hotels(request):
    return render(request, 'stays.html')


# ------------ flinghts.html-------------------------------------------

def flights(request):
    return render(request, 'flights.html')



# ------------ login.html-------------------------------------------

def login(request):
    return render(request, 'LOGIN.html')


#--------------------- AddUser ------------------------------------


# def add_user(request):
#     form = AddUser()
#     if request.method == 'POST':
#         form = AddUser(request.POST)
#         if form.is_valid():
#             form.save()
#             context = {'form':form}
#             return redirect('add_user_detail')
#         else:
#             form = AddUser()
#             context = {'form':form}
#     else:
#         form = AddUser()
#         context = {'form':form}
    
#     return render(request, 'index.html', context)


# def add_user_detail(request):
#     users1 = UserContact.objects.all()
#     return render(request, 'add_user_detail.html', {'users1':users1})


# --------------RGISTER-----------------------

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="LOGIN.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")