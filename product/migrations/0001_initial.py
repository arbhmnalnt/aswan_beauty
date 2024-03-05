# Generated by Django 3.2 on 2024-03-04 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم التصنيف')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('nameEn', models.CharField(blank=True, max_length=100, null=True, verbose_name='اسم المنتج بالانجليزى')),
                ('nameAr', models.CharField(blank=True, max_length=100, null=True, verbose_name='اسم المنتج بالعربى')),
                ('smallDescription', models.CharField(blank=True, max_length=250, null=True, verbose_name='وصف قصير')),
                ('longDescription', models.TextField(blank=True, max_length=1000, null=True, verbose_name='الوصف الكامل')),
                ('featured', models.BooleanField(default=False, verbose_name='المنتج المميز')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True, verbose_name='اسم المنتج متوافق')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.category', verbose_name='التصنيف')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='اسم الوسم')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('stars', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='النجوم')),
                ('text', models.TextField(blank=True, max_length=250, null=True, verbose_name='اكتب تجربتك مع المنتج')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='product.product', verbose_name='المنتج')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='العميل')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='product.Tag', verbose_name='الوسوم'),
        ),
        migrations.CreateModel(
            name='prices4sizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('img', models.URLField(blank=True, null=True, verbose_name='رابط الصورة')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='السعر')),
                ('size', models.CharField(blank=True, max_length=15, null=True, verbose_name='اكتب المقاس')),
                ('color', models.CharField(blank=True, max_length=15, null=True, verbose_name='اللون')),
                ('weight', models.CharField(blank=True, max_length=15, null=True, verbose_name='الوزن / الحجم')),
                ('stock', models.SmallIntegerField(blank=True, null=True, verbose_name='الكمية المعروضة')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='product.product', verbose_name='المنتج')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]