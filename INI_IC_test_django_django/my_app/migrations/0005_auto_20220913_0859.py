# Generated by Django 3.2 on 2022-09-13 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_auto_20220913_0848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testcfp4',
            name='Test22_id',
        ),
        migrations.AlterField(
            model_name='testcfp4',
            name='Testcfp4_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
