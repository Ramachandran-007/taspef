# Generated by Django 4.2.3 on 2025-01-04 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('joining_date', models.DateField()),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
