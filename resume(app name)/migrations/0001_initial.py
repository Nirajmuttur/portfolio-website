# Generated by Django 3.0.3 on 2020-02-04 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('std', models.TextField()),
                ('result', models.CharField(max_length=20)),
            ],
        ),
    ]
