# Generated by Django 4.1 on 2022-08-31 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.DateField(null=True),
        ),
    ]