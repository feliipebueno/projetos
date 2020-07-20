# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Tbtipoprocesso(models.Model):
    cod_tipoprocesso = models.AutoField(db_column='cod_TipoProcesso', primary_key=True)  # Field name made lowercase.
    de_tipoprocesso = models.CharField(db_column='de_TIpoProcesso', max_length=45, null=False)  # Field name made lowercase.
    sg_tipoprocesso = models.CharField(db_column='sg_TipoProcesso', max_length=45, null=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbtipoprocesso'
