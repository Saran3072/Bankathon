# Generated by Django 4.2.4 on 2023-08-14 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0016_jobposting_description_enhance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposting',
            name='description_enhance',
            field=models.TextField(default=None, null=True),
        ),
    ]
