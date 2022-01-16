# Generated by Django 4.0.1 on 2022-01-16 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_company_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Mail',
                'verbose_name_plural': 'Mails',
            },
        ),
        migrations.RemoveField(
            model_name='company',
            name='email',
        ),
        migrations.AddField(
            model_name='company',
            name='mail',
            field=models.ManyToManyField(related_name='email_company', to='website.Mail'),
        ),
    ]
