# Generated by Django 3.2.13 on 2023-11-20 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviecatalog', '0006_alter_quizresults_permafavgenre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizresults',
            name='permaFavGenre',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
