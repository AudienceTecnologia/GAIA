# Generated by Django 3.2.6 on 2021-08-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0008_auto_20210826_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dia_de_aula_disponivel',
            name='Dia_Semana',
            field=models.CharField(blank=True, choices=[('Segunda', 'Segunda'), ('Terça', 'Terça'), ('Quarta', 'Quarta'), ('Quinta', 'Quinta'), ('Sexta', 'Sexta'), ('Sábado', 'Sábado'), ('Domingo', 'Domingo')], max_length=255, null=True),
        ),
    ]