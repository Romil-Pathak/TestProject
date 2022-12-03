# Generated by Django 4.1.1 on 2022-12-02 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_adduser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adduser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=20),
        ),
    ]
