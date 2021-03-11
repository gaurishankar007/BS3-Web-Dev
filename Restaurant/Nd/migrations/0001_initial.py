# Generated by Django 3.1.6 on 2021-03-11 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=10)),
                ('person', models.IntegerField()),
                ('reserved_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]