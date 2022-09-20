# Generated by Django 4.0.5 on 2022-09-08 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailaddress', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=1)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pmallocation.members')),
            ],
        ),
    ]
