from django.db import models


class Product(models.Model):
    nombre=models.CharField(max_length=255)
    precio=models.FloatField()
    stock = models.IntegerField()
    image_url=models.CharField(max_length=255)
# Create your models here.


class Offer(models.Model):
    codigo=models.CharField(max_length=10)
    descuento=models.FloatField()
    descripcion = models.CharField(max_length=255)

class Account:

    def __init__(self,owner,balance):

        self.owner=owner
        self.balance=balance
    def __str__(self):
        return f"Account owner: {self.owner} \n balance : {self.balance}"


    def deposit(self,amount):
        self.balance+=amount
        print("Deposit accepted ")

    def withdraw(self,withdrawal):

        if (self.balance>=withdrawal):
            self.balance -= withdrawal
            print("withdrawal accepted")
        else:
            print("not enough funds")