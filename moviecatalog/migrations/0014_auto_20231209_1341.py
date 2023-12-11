# Generated by Django 3.2.13 on 2023-12-09 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviecatalog', '0013_alter_userprofile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='generofav',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pic',
            field=models.ImageField(default='images/defaultpfp.png', null=True, upload_to='images/'),
        ),
    ]