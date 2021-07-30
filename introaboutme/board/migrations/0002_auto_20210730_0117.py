# Generated by Django 3.2.5 on 2021-07-30 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='취미')),
                ('banner_image', models.ImageField(blank=True, upload_to='%Y/%m/%d', verbose_name='이미지')),
            ],
            options={
                'verbose_name': '김소정이 좋아하는 취미',
                'verbose_name_plural': '김소정이 좋아하는 취미',
                'db_table': 'hobby',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='장소')),
                ('description', models.CharField(max_length=64, verbose_name='위치')),
                ('banner_image', models.ImageField(blank=True, upload_to='%Y/%m/%d', verbose_name='이미지')),
            ],
            options={
                'verbose_name': '김소정이 좋아하는 맛집',
                'verbose_name_plural': '김소정이 좋아하는 맛집',
                'db_table': 'location',
            },
        ),
        migrations.CreateModel(
            name='Me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='찍은 장소')),
                ('description', models.CharField(max_length=64, verbose_name='컨셉')),
                ('banner_image', models.ImageField(blank=True, upload_to='%Y/%m/%d', verbose_name='이미지')),
            ],
            options={
                'verbose_name': '김소정이 담겨있는 사진',
                'verbose_name_plural': '김소정이 담겨있는 사진',
                'db_table': 'me',
            },
        ),
        migrations.AlterModelOptions(
            name='music',
            options={'verbose_name': '김소정이 좋아하는 음악', 'verbose_name_plural': '김소정이 좋아하는 음악'},
        ),
        migrations.AlterField(
            model_name='music',
            name='description',
            field=models.CharField(max_length=64, verbose_name='가수'),
        ),
        migrations.AlterField(
            model_name='music',
            name='title',
            field=models.CharField(max_length=64, verbose_name='곡'),
        ),
        migrations.AlterModelTable(
            name='music',
            table='music',
        ),
    ]
