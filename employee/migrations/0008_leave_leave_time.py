# Generated by Django 2.1.5 on 2019-02-05 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_auto_20190205_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='leave_time',
            field=models.CharField(default=0, max_length=128),
        ),
    ]