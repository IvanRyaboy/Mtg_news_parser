# Generated by Django 5.1.3 on 2024-12-02 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_remove_contact_subscription_contact_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='password',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
