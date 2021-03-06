# Generated by Django 4.0.4 on 2022-05-12 14:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myfoods', '0013_alter_food_type_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='chef',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myfoods.chefs', verbose_name='سرآشپز'),
        ),
        migrations.AlterField(
            model_name='food',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار'),
        ),
    ]
