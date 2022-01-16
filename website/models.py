from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Order(models.Model):
    lastname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    modele = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    fuel_type = models.CharField(max_length=255)
    chassis_number = models.CharField(max_length=255)
    part = models.TextField()
    place_delivery = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.lastname


class Part(models.Model):
    designation = models.CharField(max_length=255)
    picture = models.FileField(upload_to="part_file", blank=True, null=True)
    reference = models.CharField(max_length=255)
    chassis_number = models.CharField(max_length=255)
    brand = models.ForeignKey(
        "website.Brand", related_name="brand_part", on_delete=models.CASCADE
    )
    modele = models.CharField(max_length=255)
    fuel_type = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    featured = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Part"
        verbose_name_plural = "Parts"

    def __str__(self):
        return self.designation


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    suject = models.CharField(max_length=255)
    message = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = models.FileField(upload_to="logo_file", blank=True, null=True)
    address = models.CharField(max_length=255)
    contact = models.ManyToManyField("website.Phone", related_name="contact_company")
    mail = models.ManyToManyField("website.Mail", related_name="email_company")
    maps = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class Configuration(models.Model):
    about_title = models.CharField(max_length=255)
    about_description = HTMLField()
    about_picture = models.FileField(
        upload_to="Configuration_file", blank=True, null=True
    )
    about_picture_instruction = models.FileField(
        upload_to="Configuration_file", blank=True, null=True
    )
    about_instruction = HTMLField()
    banner_picture_home = models.FileField(upload_to="Configuration_file")
    banner_picture_part = models.FileField(upload_to="Configuration_file")
    banner_instruction = models.CharField(max_length=255)
    footer_instuction = HTMLField()
    footer_picture = models.FileField(upload_to="Configuration_file", blank=True, null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Configuration"
        verbose_name_plural = "Configurations"

    def __str__(self):
        return self.about_title


class Phone(models.Model):
    number = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Phone"
        verbose_name_plural = "Phones"

    def __str__(self):
        return self.number


class Fact(models.Model):
    title = HTMLField()
    number = models.IntegerField(default=0)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Fact"
        verbose_name_plural = "Facts"

    def __str__(self):
        return self.title


class Socialicon(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Social icon"
        verbose_name_plural = "Social icons"

    def __str__(self):
        return self.name


class Social(models.Model):
    icon = models.ForeignKey(
        "website.Socialicon", related_name="icon_networks", on_delete=models.CASCADE
    )
    link = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Social"

    def __str__(self):
        return f"{self.icon}"


class Reference(models.Model):
    name = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Reference"
        verbose_name_plural = "References"

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.name


class Mail(models.Model):
    email = models.EmailField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Mail"
        verbose_name_plural = "Mails"

    def __str__(self):
        return self.email