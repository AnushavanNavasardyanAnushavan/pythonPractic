from django.urls import path
from .views import register_request, login_request,logout_request, TouristPageListView, TouristPageDetailView, TouristPageToursDetailView, BlogListView, BlogDetailView, NextTravelDetailView, TouristTinksDetailView, aboutus, hotels, flights, login

urlpatterns = [
    path('', TouristPageListView.as_view(), name='index'),
    path('/<int:id>', TouristPageDetailView.as_view(), name='index_detail'),
    path('/<int:id>/', TouristPageToursDetailView.as_view(), name='index_detail_tours'),
    path('index_nextTravel_detail/<int:id>', NextTravelDetailView.as_view(), name='next_travel_detail'),
    path('tinks_detail/<int:id>', TouristTinksDetailView.as_view(), name='tinks_detail'),

    path('blog/', BlogListView.as_view(), name='blog_page'),
    path('blog/<int:id>', BlogDetailView.as_view(), name='blog_page_detail'),

    path('aboutus/', aboutus, name='aboutus'),

# ------------ Stays.html---------------------------------------------
    path('hotels/', hotels, name='stays'),

# ------------ flinghts.html-------------------------------------------
   path('flights/', flights, name='flights'),


# ------------regitracia--> login.html, register.html, views-------------------------------------------
    path('register', register_request, name='register'),
    path('login', login_request, name='login'),
    path('logout', logout_request, name = 'logout'),
]