# Generated by Django 4.1.4 on 2022-12-30 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_transaction_tour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='tour',
        ),
    ]
