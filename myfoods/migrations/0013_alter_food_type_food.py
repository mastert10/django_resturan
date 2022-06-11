# Generated by Django 4.0.4 on 2022-05-09 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfoods', '0012_alter_food_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='type_food',
            field=models.CharField(choices=[('pitza', 'پیتزا'), ('sandwich', 'ساندویچ'), ('dessert', 'دسر'), ('all', 'همه')], default='all', max_length=10, verbose_name='نوع غذا'),
        ),
    ]
