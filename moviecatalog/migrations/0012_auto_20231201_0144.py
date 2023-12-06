# Generated by Django 3.2.13 on 2023-12-01 01:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moviecatalog', '0011_auto_20231128_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='email@gmail.com', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='Name', max_length=25),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='pic',
            field=models.ImageField(default='/static/images/placeholder.png', null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.OneToOneField(default='username123', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
