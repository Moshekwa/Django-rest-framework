# Generated by Django 4.2.16 on 2024-11-18 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('salary', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
