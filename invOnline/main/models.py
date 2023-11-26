from django.db import models

# Create your models here.
class MasterInventory(models.Model): # create model for inventory  and inventory list 
    name = models.CharField(max_length=100)# create new attribute/ clas vraible definign the type of feild i nthe datbase 
    
    def __str__(self):
        return self.name # allows us to return the name as a str
        
class InvItem(models.Model): # create model for items within inventory 
    masterInv = models.ForeignKey(MasterInventory, on_delete=models.CASCADE) #tells this cakss that master calss is the MasterInventory 
    productName = models.CharField(max_length=100) # define name attribute
    productStock = models.IntegerField() # defiene qty attribute 
    
    def __str__(self):
        return self.productName # allows us to return the name as a str