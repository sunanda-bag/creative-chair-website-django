# Generated by Django 3.2.3 on 2021-05-16 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('category', models.CharField(choices=[('C1', 'New'), ('C2', 'Best'), ('C3', 'Category 3')], max_length=2)),
                ('label', models.CharField(choices=[('L1', 'primary'), ('L2', 'secondary'), ('L3', 'danger')], max_length=2)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('sub_description', models.TextField()),
                ('images', models.ImageField(blank=True, null=True, upload_to='static/images')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='my_app.product')),
            ],
        ),
    ]
