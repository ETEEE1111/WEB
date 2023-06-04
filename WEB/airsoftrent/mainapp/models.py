# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Authorisation(models.Model):
    authorisation_id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=35)
    password = models.CharField(max_length=15)
    level_of_access = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'authorisation'
    
    def __str__(self) :
        return self.login


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)
    fullname_head = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'company'


class Equipment(models.Model):
    equipment_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    name_of_set = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'equipment'


class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    fullname_instructor = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=12)
    experience = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'instructor'


class Manager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    fullname_manager = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'manager'


class Marketer(models.Model):
    marketer_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    fullname_marketer = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=12)
    date_of_birth = models.DateField()

    class Meta:
        managed = False
        db_table = 'marketer'


class Offer(models.Model):
    offer_id = models.AutoField(primary_key=True)
    services = models.ForeignKey('Services', models.DO_NOTHING)
    manager = models.ForeignKey(Manager, models.DO_NOTHING)
    instructor = models.ForeignKey(Instructor, models.DO_NOTHING)
    time = models.DateField()
    fullname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'offer'


class Polygon(models.Model):
    polygon_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    name_polygon = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'polygon'


class Services(models.Model):
    services_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    polygon = models.ForeignKey(Polygon, models.DO_NOTHING)
    equipment = models.ForeignKey(Equipment, models.DO_NOTHING)
    name_of_services = models.CharField(max_length=30)
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'services'


class Set(models.Model):
    equipment = models.ForeignKey(Equipment, models.DO_NOTHING)
    type = models.ForeignKey('Type', models.DO_NOTHING)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'set'


class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'type'
