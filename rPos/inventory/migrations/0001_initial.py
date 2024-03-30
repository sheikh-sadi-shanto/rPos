# Generated by Django 5.0.3 on 2024-03-30 08:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('additionalInfo', models.TextField(blank=True, max_length=256, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=100)),
                ('unit', models.PositiveIntegerField()),
                ('transportationCost', models.PositiveIntegerField()),
                ('otherCost', models.PositiveIntegerField()),
                ('invImage', models.ImageField(blank=True, null=True, upload_to='inventory/')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventorycategory')),
            ],
        ),
    ]