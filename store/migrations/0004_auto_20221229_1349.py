# Generated by Django 3.1.2 on 2022-12-29 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20221229_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='picture',
            field=models.ImageField(upload_to='pictures'),
        ),
    ]
