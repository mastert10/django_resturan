# Generated by Django 4.0.4 on 2022-04-30 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfoods', '0006_alter_food_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chefs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')),
                ('slug', models.SlugField(verbose_name='ادرس اشپز')),
                ('age', models.IntegerField(verbose_name='سن')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='chef',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myfoods.chefs'),
        ),
    ]
