# Generated by Django 3.2.8 on 2021-10-12 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='companyName',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='laptop',
            name='cpu',
            field=models.CharField(default='NA', max_length=255),
        ),
        migrations.AddField(
            model_name='laptop',
            name='laptopName',
            field=models.CharField(default='NA', max_length=255),
        ),
        migrations.AddField(
            model_name='laptop',
            name='ram',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='laptop',
            name='storage',
            field=models.IntegerField(default=0),
        ),
    ]
