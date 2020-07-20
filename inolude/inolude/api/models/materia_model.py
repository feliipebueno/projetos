# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Tbmateria(models.Model):
    cod_tipomateria = models.AutoField(db_column='cod_TipoMateria', primary_key=True)  # Field name made lowercase.
    de_tipomateria = models.CharField(db_column='de_TipoMateria', max_length=45, null=False)  # Field name made lowercase.
    sg_tipomateria = models.CharField(db_column='sg_TipoMateria', max_length=45, null=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbmateria'
