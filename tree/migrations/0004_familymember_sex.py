# Generated by Django 4.2.13 on 2024-07-05 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0003_alter_familymember_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='familymember',
            name='sex',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=6),
            preserve_default=False,
        ),
    ]
