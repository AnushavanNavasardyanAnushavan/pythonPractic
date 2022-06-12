from django.db import models

# Create your models here.

class HomeBackground(models.Model):
    homeBackgroundName = models.CharField('Home header', max_length=50, null=True, blank=True)
    homeBackgroundComment = models.CharField('Home comment', max_length=50, null=True, blank=True)
    homeBackgroundAbout = models.TextField('About home', null=True, blank=True)
    homeBackgroundImg = models.ImageField('Home Background image', upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.homeBackgroundName

    class Meta:
        verbose_name = 'HomeBackground'
        verbose_name_plural = 'HomeBackgrounds'


class TureIdea(models.Model):
    name = models.CharField('turs name', max_length=50)
    comment = models.CharField('turs comment', max_length=50)
    img = models.ImageField('turs image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TureIdea'
        verbose_name_plural = 'TureIdeas'


class AboutAs(models.Model):
    name = models.CharField('About our naem', max_length=50)
    comment = models.CharField('About our team', max_length=50)
    img = models.ImageField('About our image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'AboutAs'
        verbose_name_plural = 'AboutTeam'


class TinksForTourism(models.Model):
    name = models.CharField('Tink naem', max_length=50)
    about = models.CharField('About tink', max_length=50)
    price = models.FloatField('tink price')
    img = models.ImageField('About our image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tink'
        verbose_name_plural = 'Tinks'


class BookForHotels(models.Model):
    name = models.CharField('Book naem', max_length=50,)
    about = models.CharField('About book', max_length=50)
    img = models.ImageField('Book image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

class CommentsCustomer(models.Model):
    customerName = models.CharField('Customer name', max_length=50)
    customerProfession = models.CharField('Customer Profession', max_length=50)
    customerComment = models.CharField('Customer Comment', max_length=250)
    customerImg = models.ImageField('customer image', upload_to='media')

    def __str__(self):
        return self.customerName 

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

class OurServices(models.Model):
    name = models.CharField('Services naem', max_length=50)
    about = models.CharField('About services', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class NextTravel(models.Model):
    name = models.CharField('Next travel name', max_length=50)
    about = models.CharField('About next travel', max_length=50)
    img = models.ImageField('BTravel image', upload_to='media')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Travel'
        verbose_name_plural = 'Travels'

class SubscirbeNow(models.Model):
    about = models.CharField('About next travel', max_length=50)


    def __str__(self):
        return self.about


