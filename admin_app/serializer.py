from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import *


class UsertableSerializer(ModelSerializer):
    class Meta:
        model = Usertable
        fields = ['username', 'password', 'type']

class Farmerserializer(ModelSerializer):
    class Meta:
        model = farmer
        fields=['name','address','place','mob_no','K_bhavan','farmLocation']
class ProductsSerializer1(ModelSerializer):
         # Add a SerializerMethodField to retrieve the category name
     product_category = SerializerMethodField()
     class Meta:
        model=product
            #  loginid=models.ForeignKey(Usertable,on_delete=models.CASCADE,null=True,blank=True)
 
        fields=['loginid','name','image','price','Quantity','Details','product_category']
     def get_product_category(self, obj):
        # Safely return the category name or None if no category is assigned
            return obj.category.category_name if obj.category else None
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




