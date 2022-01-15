# Generated by Django 4.0.1 on 2022-01-15 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant', models.CharField(max_length=200, verbose_name='Растение')),
                ('n', models.IntegerField()),
                ('p', models.IntegerField()),
                ('k', models.IntegerField()),
                ('ca', models.IntegerField()),
                ('mg', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Substances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(max_length=200, verbose_name='Удобрение')),
                ('n', models.IntegerField()),
                ('p', models.IntegerField()),
                ('k', models.IntegerField()),
                ('ca', models.IntegerField()),
                ('mg', models.IntegerField()),
            ],
        ),
    ]
