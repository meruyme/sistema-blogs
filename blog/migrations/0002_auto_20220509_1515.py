# Generated by Django 3.2.3 on 2022-05-09 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='conteudo',
            field=models.CharField(max_length=500, verbose_name='Conteúdo'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='nome_usuario',
            field=models.CharField(max_length=255, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='post',
            name='conteudo',
            field=models.TextField(verbose_name='Conteúdo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=300, verbose_name='Título'),
        ),
    ]