# Generated by Django 2.2 on 2021-08-04 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210804_1915'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quan', models.IntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cartlist')),
                ('prodt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.products')),
            ],
        ),
    ]
