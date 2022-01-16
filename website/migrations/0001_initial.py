# Generated by Django 4.0.1 on 2022-01-11 20:03

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("date_add", models.DateTimeField(auto_now_add=True)),
                ("date_update", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Brand",
                "verbose_name_plural": "Brands",
            },
        ),
        migrations.CreateModel(
            name="Configuration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("about_title", models.CharField(max_length=255)),
                ("about_description", tinymce.models.HTMLField()),
                (
                    "about_picture",
                    models.FileField(
                        blank=True, null=True, upload_to="Configuration_file"
                    ),
                ),
                (
                    "about_picture_instruction",
                    models.FileField(
                        blank=True, null=True, upload_to="Configuration_file"
                    ),
                ),
                ("about_instruction", tinymce.models.HTMLField()),
                (
                    "banner_picture_home",
                    models.FileField(upload_to="Configuration_file"),
                ),
                (
                    "banner_picture_part",
                    models.FileField(upload_to="Configuration_file"),
                ),
                ("banner_instruction", models.CharField(max_length=255)),
                ("footer_instuction", tinymce.models.HTMLField()),
                ("date_add", models.DateTimeField(auto_now_add=True)),
                ("date_update", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Configuration",
                "verbose_name_plural": "Configurations",
            },
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("suject", models.CharField(max_length=255)),
                ("message", models.TextField()),
                ("date_add", models.DateTimeField(auto_now_add=True)),
                ("date_update", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Contact",
                "verbose_name_plural": "Contacts",
            },
        ),
        migrations.CreateModel(
            name="Fact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", tinymce.models.HTMLField()),
                ("number", models.IntegerField(default=0)),
                ("date_add", models.DateTimeField(auto_now_add=True)),
                ("date_update", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Fact",
                "verbose_name_plural": "Facts",
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("lastname", models.CharField(max_length=255)),
                ("firstname", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=255)),
                ("brand", models.CharField(max_length=255)),
                ("modele", models.CharField(max_length=255)),
                ("year", models.CharField(max_length=255)),
                ("fuel_type", models.CharField(max_length=255)),
                ("chassis_number", models.CharField(max_length=255)),
                ("part", models.TextField()),
                ("place_delivery", models.CharField(max_length=255)),
                ("date_add", models.DateTimeField(auto_now_add=True)),
                ("date_update", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Order",
                "verbose_name_plural": "Orders",
            },
        ),
        migrations.CreateModel(
            name="Phone",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.CharField(max_length=255)),
                ("date_add", models.DateTimeField(auto_now_add=True)),
                ("date_update", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Phone",
                "verbose_name_plural": "Phones",
            },
        ),
        migrations.CreateModel(
            name="Reference",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("date_add", models.DateTimeField(auto_now_add=True)),
                ("date_update", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Reference",
                "verbose_name_plural": "References",
            },
        ),
        migrations.CreateModel(
            name="Socialicon",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("icon", models.CharField(max_length=255)),
                ("date_add", models.DateTimeField(auto_now_add=True)),
                ("date_update", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Social icon",
                "verbose_name_plural": "Social icons",
            },
        ),
        migrations.CreateModel(
            name="Social",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("link", models.CharField(max_length=255)),
                ("date_add", models.DateTimeField(auto_now_add=True)),
                ("date_update", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
                (
                    "icon",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="icon_networks",
                        to="website.socialicon",
                    ),
                ),
            ],
            options={
                "verbose_name": "Social",
                "verbose_name_plural": "Social",
            },
        ),
        migrations.CreateModel(
            name="Part",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("designation", models.CharField(max_length=255)),
                (
                    "picture",
                    models.FileField(blank=True, null=True, upload_to="part_file"),
                ),
                ("reference", models.CharField(max_length=255)),
                ("chassis_number", models.CharField(max_length=255)),
                ("modele", models.CharField(max_length=255)),
                ("fuel_type", models.CharField(max_length=255)),
                ("year", models.CharField(max_length=255)),
                ("featured", models.BooleanField(default=False)),
                ("date_add", models.DateTimeField(auto_now_add=True)),
                ("date_update", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="brand_part",
                        to="website.brand",
                    ),
                ),
            ],
            options={
                "verbose_name": "Part",
                "verbose_name_plural": "Parts",
            },
        ),
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "logo",
                    models.FileField(blank=True, null=True, upload_to="logo_file"),
                ),
                ("address", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("maps", models.TextField()),
                ("date_add", models.DateTimeField(auto_now_add=True)),
                ("date_update", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
                (
                    "contact",
                    models.ManyToManyField(
                        related_name="contact_company", to="website.Phone"
                    ),
                ),
            ],
            options={
                "verbose_name": "Company",
                "verbose_name_plural": "Companys",
            },
        ),
    ]