# Generated by Django 4.0 on 2022-02-08 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.customeruser'),
        ),
    ]