from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import HomeBackground, TureIdea, AboutAs, TinksForTourism, BookForHotels, CommentsCustomer, OurServices, NextTravel, SubscirbeNow

# Create your views here.


class TouristPageListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        homes = HomeBackground.objects.all()
        tours = TureIdea.objects.all()
        abouts = AboutAs.objects.all()
        tinks = TinksForTourism.objects.all()
        books1 = BookForHotels.objects.all()
        commentsCustomer = CommentsCustomer.objects.all()
        ourServices1 = OurServices.objects.all()
        nextTravels = NextTravel.objects.all()
        subscirbe = SubscirbeNow.objects.all()
        return render(request, 'index.html', {'homes':homes, 'tours':tours, 'abouts': abouts, 'tinks':tinks, ' books1': books1, 'commentsCustomer':commentsCustomer, 'ourServices1':ourServices1, 'nextTravels':nextTravels, 'subscirbe':subscirbe })




# def tureIdea(request):
#     return render(request, 'index.html',  {})   

# def aboutAs(request):
#     abouts = AboutAs.objects.all()
#     return render(request, 'index.html', {'abouts':abouts})


# class TourIdeaListView(ListView):
#     template_name = 'index.html'
#     def get(self, request):
#         ideas = TureIdea.objects.all()
#         return render(request, self.template_name, {'ideas':ideas})





