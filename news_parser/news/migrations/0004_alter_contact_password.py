# Generated by Django 5.1.3 on 2024-12-02 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_contact_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]