# Generated by Django 2.1.1 on 2018-09-23 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, editable=False)),
                ('name', models.CharField(max_length=20, verbose_name='名前')),
                ('latitude', models.DecimalField(decimal_places=6, default=0, max_digits=9, verbose_name='緯度')),
                ('longitude', models.DecimalField(decimal_places=6, default=0, max_digits=9, verbose_name='経度')),
                ('update', models.DateTimeField(verbose_name='更新日')),
            ],
        ),
    ]
