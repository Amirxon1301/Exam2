# Generated by Django 5.0 on 2023-12-29 05:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=39)),
                ('yosh', models.PositiveIntegerField()),
                ('ish_vaqti', models.CharField(max_length=30)),
                ('user', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Haydovchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=30)),
                ('kiritilgan_sana', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Mijoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=30)),
                ('manzil', models.CharField(max_length=40)),
                ('qarz', models.PositiveIntegerField()),
                ('user', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Suv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brend', models.CharField(max_length=30)),
                ('narx', models.PositiveIntegerField()),
                ('litr', models.PositiveIntegerField()),
                ('batafsil', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Buyurtma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.DateField()),
                ('miqdor', models.PositiveIntegerField()),
                ('umumiy_narx', models.PositiveIntegerField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.admin')),
                ('haydovchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.haydovchi')),
                ('mijoz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mijoz')),
                ('suv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.suv')),
            ],
        ),
    ]
