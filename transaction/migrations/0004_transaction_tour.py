# Generated by Django 4.1.4 on 2022-12-30 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_mytours_total_price'),
        ('transaction', '0003_remove_transaction_tour'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='tour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.tours'),
        ),
    ]
