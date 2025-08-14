from django.shortcuts import render
from apps.website.models import *
# Create your views here.


def IndexView(request):
    services = Service.objects.all().order_by("created_at")[:4]
    listservices = Service.objects.all()
    specialty_service = listservices.filter(name__iexact="Specialty Services").first()

    context = {
        "services": services,
        "listservices": listservices,
        "specialty_service": specialty_service,
    }
    return render(request, "website/index.html", context)

def AboutUsView(request):
    services = Service.objects.all().order_by("created_at")[:6]
    context = {
        "services": services
    }
    return render(request, "website/about.html", context)

def AllServicesView(request):
    services = Service.objects.all().order_by("created_at")
    context = {
        "services": services
    }
    return render(request, "website/services.html", context)

def ServiceDetails(request, pk=None, name=None):
    service = Service.objects.get(sid=pk)
    services = Service.objects.all().order_by("created_at").exclude(sid=pk)
    package = getattr(service, 'package', None)
    context = {
        "services": services,
        "service": service,
        "package": package
    }
    return render(request, "website/service.html", context)

def PackagesView(request):
    services = Service.objects.all().order_by("created_at")
    packages = Package.objects.all()
    context = {
        "services": services,
        "packages": packages
    }
    return render(request, "website/packages.html", context)


def CareersView(request):
    services = Service.objects.all().order_by("created_at")
    careers = Career.objects.all()
    context = {
        "services": services,
        "careers": careers
    }
    return render(request, "website/careers.html", context)


def ContactUsView(request):
    services = Service.objects.all().order_by("created_at")
    context = {
        "services": services
    }
    return render(request, "website/contact_halisi.html", context)


