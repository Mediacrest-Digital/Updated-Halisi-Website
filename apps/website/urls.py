from django.urls import path
from apps.website.views import *

app_name = "website"

urlpatterns = [
    path( "", IndexView, name="index", ),
    path( "about_us", AboutUsView, name="about_us"),
    path( "services", AllServicesView, name="services", ),
    path( "service/<str:pk>", ServiceDetails, name="service", ),
    path( "packages", PackagesView, name="packages", ),
    path( "careers", CareersView, name="careers", ),
    path( "contact_halisi", ContactUsView, name="contact_halisi"),
]



