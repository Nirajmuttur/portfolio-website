# Generated by Django 3.0.3 on 2020-02-04 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('des', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='skill',
            name='develop',
            field=models.CharField(max_length=200),
        ),
    ]