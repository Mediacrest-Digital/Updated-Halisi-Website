import uuid
from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Service(models.Model):
    sid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to="services", null=True)
    mainBanner = models.ImageField(upload_to="services", null=True)
    description = HTMLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Package(models.Model):
    pid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to="packages", blank=True, null=True)
    pdfFile = models.FileField(upload_to="packages/files", null=True, blank=True)
    description = HTMLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    service = models.OneToOneField(
        Service,
        on_delete=models.CASCADE,
        related_name="package",
        null=True,
        blank=True
    )

    def __str__(self):
        return str(self.name)



class Career(models.Model):
    cid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, null=True)
    description = HTMLField(blank=True, null=True)
    requirements = HTMLField(blank=True, null=True)
    application_process = HTMLField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


