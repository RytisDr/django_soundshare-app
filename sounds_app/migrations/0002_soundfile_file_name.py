# Generated by Django 3.0.6 on 2020-06-02 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sounds_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='soundfile',
            name='file_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
