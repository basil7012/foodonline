# Generated by Django 3.2.9 on 2021-12-23 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique='true')),
                ('slug', models.SlugField(max_length=250, unique='true')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique='true')),
                ('slug', models.SlugField(max_length=250, unique='true')),
                ('img', models.ImageField(upload_to='product')),
                ('desc', models.TextField()),
                ('stock', models.IntegerField()),
                ('available', models.BooleanField(default=False)),
                ('price', models.IntegerField()),
                ('catog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ('name',),
            },
        ),
    ]
