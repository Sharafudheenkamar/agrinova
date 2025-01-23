from rest_framework.serializers import ModelSerializer
from .models import *


class UsertableSerializer(ModelSerializer):
    class Meta:
        model = Usertable
        fields = ['username', 'password', 'type']

class Farmerserializer(ModelSerializer):
    class Meta:
        model = farmer
        fields=['name','address','place','mob_no','K_bhavan','farmLocation']
class ProductsSerializer(ModelSerializer):
     class Meta:
        model=product
            #  loginid=models.ForeignKey(Usertable,on_delete=models.CASCADE,null=True,blank=True)
 
        fields=['loginid','name','image','price','Quantity','Details']

class  RequestsSerializer(ModelSerializer):
     class Meta:
        model=requesttable
        fields='__all__'
class  RequestsSerializer1(ModelSerializer):
     class Meta:
        model=requesttable
        fields=['status']
class  NotificationsSerializer(ModelSerializer):
    class Meta:
        model=notification
        fields='__all__'
    


class ComplaintSerializer(ModelSerializer):
    class Meta:
        model=complaint
        fields='__all__'
class ComplaintSerializer1(ModelSerializer):
    class Meta:
        model=complaint
        fields=['loginid','complaint']



class LabourSerializer(ModelSerializer):
    class Meta:
        model = labour
        fields = ['loginid','name','date', 'hour', 'task']
    

class ComplaintSerializer(ModelSerializer):
    class Meta:
        model = complaint
        fields = ['loginid','complaint','reply']




