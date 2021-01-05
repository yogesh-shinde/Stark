# Generated by Django 2.2.6 on 2021-01-05 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210105_1313'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adminmodel',
            options={'verbose_name': 'Admin Model', 'verbose_name_plural': 'Admin Model'},
        ),
        migrations.AlterModelOptions(
            name='usermodel',
            options={'verbose_name': 'User Model', 'verbose_name_plural': 'User Model'},
        ),
        migrations.AlterModelTable(
            name='adminmodel',
            table='admin_model',
        ),
        migrations.AlterModelTable(
            name='usermodel',
            table='user_model',
        ),
    ]