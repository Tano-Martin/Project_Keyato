from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.

# Changer le titre de l'administration
admin.site.site_header = "Keyato Administration"


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "lastname",
        "firstname",
        "email",
        "phone",
        "brand",
        "modele",
        "year",
        "fuel_type",
        "chassis_number",
        "place_delivery",
        "date_add",
        "date_update",
        "status",
    )
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = [
        "firstname",
        "email",
        "phone",
        "brand",
        "modele",
        "year",
        "fuel_type",
        "chassis_number",
        "place_delivery",
        "status",
    ]


@admin.register(models.Part)
class PartAdmin(admin.ModelAdmin):
    list_display = (
        # "view_image",
        "designation",
        "reference",
        "chassis_number",
        "brand",
        "modele",
        "year",
        "fuel_type",
        "featured",
        "date_add",
        "date_update",
        "status",
    )
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = [
        # "designation",
        "reference",
        "chassis_number",
        "brand",
        "modele",
        "year",
        "fuel_type",
        "featured",
        "status",
    ]

    # def view_image(self, obj):
    #     return mark_safe(
    #         f'<img src="{obj.picture.url}" style="height:100px; width:120px">'
    #     )

    # view_image.short_description = "Preview parts images"


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "suject", "date_add", "date_update", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["email", "suject", "status"]


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "view_logo",
        "name",
        "address",
        "date_add",
        "date_update",
        "status",
    )
    date_hierarchy = "date_add"
    list_per_page = 10
    filter_horizontal = ["contact", "mail"]
    list_editable = ["name", "address", "status"]

    def view_logo(self, obj):
        return mark_safe(
            f'<img src="{obj.logo.url}" style="height:100px; width:120px">'
        )

    view_logo.short_description = "Preview logo images"


@admin.register(models.Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = (
        "view_banner_picture_home",
        "view_banner_picture_part",
        "view_about_picture",
        "view_about_picture_instruction",
        "view_footer_picture",
        "about_title",
        "banner_instruction",
        "about_instruction",
        "date_add",
        "date_update",
        "status",
    )
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]

    def view_banner_picture_home(self, obj):
        return mark_safe(
            f'<img src="{obj.banner_picture_home.url}" style="height:100px; width:120px">'
        )

    view_banner_picture_home.short_description = "Preview banner home images"

    def view_banner_picture_part(self, obj):
        return mark_safe(
            f'<img src="{obj.banner_picture_part.url}" style="height:100px; width:120px">'
        )

    view_banner_picture_part.short_description = "Preview banner part images"

    def view_about_picture(self, obj):
        return mark_safe(
            f'<img src="{obj.about_picture.url}" style="height:100px; width:120px">'
        )

    view_about_picture.short_description = "Preview about images"

    def view_about_picture_instruction(self, obj):
        return mark_safe(
            f'<img src="{obj.about_picture_instruction.url}" style="height:100px; width:120px">'
        )

    view_about_picture_instruction.short_description = (
        "Preview about instruction images"
    )

    def view_footer_picture(self, obj):
        return mark_safe(
            f'<img src="{obj.footer_picture.url}" style="height:100px; width:120px">'
        )

    view_footer_picture.short_description = "Preview footer images"
    
    
@admin.register(models.Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ("number", "date_add", "date_update", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]


@admin.register(models.Fact)
class FactAdmin(admin.ModelAdmin):
    list_display = ("title", "number", "date_add", "date_update", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["number", "status"]


@admin.register(models.Socialicon)
class SocialiconAdmin(admin.ModelAdmin):
    list_display = ("name", "icon", "date_add", "date_update", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["icon", "status"]


@admin.register(models.Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ("link", "date_add", "date_update", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]


@admin.register(models.Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ("name", "date_add", "date_update", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "date_add", "date_update", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]


@admin.register(models.Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ("email", "date_add", "date_update", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]