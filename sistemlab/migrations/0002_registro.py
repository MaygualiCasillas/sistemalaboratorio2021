# Generated by Django 3.2 on 2021-06-09 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemlab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num_control', models.CharField(max_length=9)),
                ('FE', models.DateTimeField()),
                ('FS', models.DateTimeField(blank=True, null=True)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
