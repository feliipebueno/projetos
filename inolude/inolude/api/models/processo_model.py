# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from api.validators import file_size


class Tbprocesso(models.Model):
    cod_processo = models.AutoField(db_column='cod_Processo', primary_key=True)  # Field name made lowercase.
    nu_processo = models.BigIntegerField(db_column='nu_Processo',null=False)  # Field name made lowercase.
    dt_processo = models.DateField(db_column='dt_Processo',null=False)  # Field name made lowercase.
    ar_processo = models.FileField(upload_to="media/", db_column='ar_Processo', max_length=45, null=False,validators=[file_size])  # Field name made lowercase.
    vl_processo = models.FloatField(db_column='vl_Processo', null=False)  # Field name made lowercase.
    cod_tipoprocesso = models.ForeignKey('Tbtipoprocesso', models.DO_NOTHING, db_column='cod_TipoProcesso', null=False)  # Field name made lowercase.
    cod_materia = models.ForeignKey('Tbmateria', models.DO_NOTHING, db_column='cod_Materia', null=False)  # Field name made lowercase.
    cod_forma = models.ForeignKey('Tbforma', models.DO_NOTHING, db_column='cod_Forma', null=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbprocesso'
