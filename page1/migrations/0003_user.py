# Generated by Django 2.1.7 on 2019-03-31 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0002_auto_20190330_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]
