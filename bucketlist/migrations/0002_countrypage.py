# Generated by Django 3.0.8 on 2020-08-13 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bucketlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('pub_date', models.DateField()),
                ('c_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bucketlist.Countries')),
            ],
        ),
    ]
