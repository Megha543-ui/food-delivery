# Generated by Django 4.1.7 on 2023-04-09 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=35, unique=True)),
                ('Email', models.CharField(max_length=60)),
                ('Address', models.CharField(max_length=60)),
                ('City', models.CharField(max_length=10)),
                ('Zipcode', models.CharField(max_length=20)),
                ('Cardnumber', models.CharField(max_length=20)),
                ('Expmonth', models.CharField(max_length=20)),
                ('Cvv', models.CharField(max_length=20)),
            ],
        ),
    ]
