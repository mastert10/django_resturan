# Generated by Django 4.0.4 on 2022-05-01 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfoods', '0011_food_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.ManyToManyField(related_name='foods', to='myfoods.category', verbose_name='دسته بندی'),
        ),
    ]