# Generated by Django 4.1.1 on 2022-12-02 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_adduser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adduser',
            name='subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
