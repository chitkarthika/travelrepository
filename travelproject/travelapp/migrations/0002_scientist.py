# Generated by Django 4.2.7 on 2024-01-01 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='scientist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img2', models.ImageField(upload_to='pics')),
                ('dt', models.DateTimeField()),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField()),
            ],
        ),
    ]