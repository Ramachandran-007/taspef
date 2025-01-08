# Generated by Django 4.2.3 on 2025-01-04 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='occupation',
        ),
        migrations.AddField(
            model_name='member',
            name='subscription',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
