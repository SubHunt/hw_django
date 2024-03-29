# Generated by Django 4.2 on 2023-04-04 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('price', models.IntegerField(max_length=7)),
                ('image', models.CharField(max_length=100)),
                ('release_date', models.DateField(max_length=10)),
                ('lte_exists', models.BooleanField()),
            ],
        ),
    ]
