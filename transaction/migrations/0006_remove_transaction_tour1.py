# Generated by Django 4.1.4 on 2022-12-30 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0005_transaction_tour1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='tour1',
        ),
    ]
