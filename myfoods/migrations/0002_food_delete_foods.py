# Generated by Django 4.0.4 on 2022-04-23 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfoods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام غذا')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('thumbnail', models.ImageField(upload_to='images/', verbose_name='عکس')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('rate', models.IntegerField(verbose_name='امتیاز')),
                ('time', models.TimeField(verbose_name='زمان لازم')),
                ('pub_date', models.DateField(verbose_name='تاریخ انتشار')),
            ],
        ),
        migrations.DeleteModel(
            name='Foods',
        ),
    ]
