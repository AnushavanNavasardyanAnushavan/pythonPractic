from django.contrib import admin
from .models import HomeBackground, TureIdea, AboutAs, TinksForTourism, BookForHotels, CommentsCustomer, OurServices, NextTravel, SubscirbeNow, AboutusPage1st, AboutusPage2th, AboutusPage3th, BlogPage, BlogPageToSupport, UserContact

# Register your models here.
admin.site.register(HomeBackground)
admin.site.register(TureIdea)
admin.site.register(AboutAs)
admin.site.register(TinksForTourism)
admin.site.register(BookForHotels)
admin.site.register(CommentsCustomer)
admin.site.register(OurServices)
admin.site.register(NextTravel)

# ------------ Aboutus Page --------------------
admin.site.register(SubscirbeNow)
admin.site.register(AboutusPage1st)
admin.site.register(AboutusPage2th)
admin.site.register(AboutusPage3th)

# ------------ Blog Page --------------------
admin.site.register(BlogPage)
admin.site.register(BlogPageToSupport)


# ------------ LOGIN  Page --------------------
admin.site.register(UserContact)

















