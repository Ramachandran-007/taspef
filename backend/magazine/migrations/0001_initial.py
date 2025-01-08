# Generated by Django 4.2.3 on 2025-01-06 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('pdf_file', models.FileField(upload_to='magazine_pdfs/')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='magazine_covers/')),
            ],
        ),
    ]