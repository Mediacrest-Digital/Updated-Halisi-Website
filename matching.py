from apps.website.models import Package, Service
import difflib
packages = Package.objects.filter(service__isnull=True)
services = Service.objects.all()
service_names = [s.name for s in services]
for package in packages:
    closest_match = difflib.get_close_matches(package.name, service_names, n=1, cutoff=0.6)
    if closest_match:
        matched_service = services.get(name=closest_match[0])
        package.service = matched_service
        package.save()