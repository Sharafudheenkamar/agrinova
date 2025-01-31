from django.db import models

# Create your models here.
class Usertable(models.Model):
     username =models.CharField(max_length=100,null=True,blank=True)
     password =models.CharField(max_length=100,null=True,blank=True)
     type =models.CharField(max_length=100,null=True,blank=True)
     statusl=models.CharField(max_length=100,default='rejected',null=True,blank=True)

     
class policy(models.Model):
     loginid=models.ForeignKey(Usertable,on_delete=models.CASCADE,null=True,blank=True)
     PolicyTitle =models.CharField(max_length=100,null=True,blank=True)
     Category =models.CharField(max_length=100,null=True,blank=True)
     date =models.DateTimeField(auto_now_add=True,null=True,blank=True)
     Details =models.CharField(max_length=1000,null=True,blank=True)
     policyfile=models.FileField(upload_to='policyfile',null=True,blank=True)

class feedback(models.Model):
     loginid=models.ForeignKey(Usertable,on_delete=models.CASCADE,null=True,blank=True)
     feedback =models.CharField(max_length=100,null=True,blank=True)
     date =models.DateTimeField(auto_now_add=True,null=True,blank=True)
     reply =models.CharField(max_length=100,null=True,blank=True)
     
class complaint(models.Model):
     loginid=models.ForeignKey(Usertable,on_delete=models.CASCADE,null=True,blank=True)
     complaint =models.CharField(max_length=100,null=True,blank=True)
     date =models.DateTimeField(auto_now_add=True,null=True,blank=True)
     reply =models.CharField(max_length=100,null=True,blank=True)
     status =models.CharField(max_length=100,null=True,blank=True)
class Category(models.Model):
     category_name = models.CharField(max_length=100,null=True,blank=True)
class product(models.Model):
     loginid=models.ForeignKey(Usertable,on_delete=models.CASCADE,null=True,blank=True)
     name =models.CharField(max_length=100,null=True,blank=True)
     date =models.DateTimeField(auto_now_add=True,null=True,blank=True)
     category= models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
     image =models.FileField(upload_to="bsns_product",null=True,blank=True) 
     price =models.CharField(max_length=100,null=True,blank=True)
     Quantity = models.CharField(max_length=100,null=True,blank=True)
     Details =models.CharField(max_length=100,null=True,blank=True)

class requesttable(models.Model):
     loginid=models.ForeignKey(Usertable,on_delete=models.CASCADE,null=True,blank=True)
     # name =models.CharField(max_length=100,null=True,blank=True)
     date =models.DateTimeField(auto_now_add=True,null=True,blank=True)
     quantity = models.IntegerField(default=1)
     productid =models.ForeignKey(product,on_delete=models.CASCADE)
     status = models.CharField(max_length=100,null=True,blank=True)

#admin_app/models.py
class MarketTrend(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    last_week_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    this_week_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    demand = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp of last update

    def __str__(self):
        return f"{self.category.category_name} - {self.updated_at}"

class cart(models.Model):
    loginid = models.ForeignKey(Usertable, on_delete=models.CASCADE, null=True, blank=True)
    productid = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)  # Add quantity field

     

class labour(models.Model):
     loginid=models.ForeignKey(Usertable,on_delete=models.CASCADE,null=True,blank=True)
     date =models.DateTimeField(null=True,blank=True)
     name =models.CharField(max_length=100,null=True,blank=True)
     hour =models.CharField(max_length=10,null=True,blank=True)
     status =models.CharField(max_length=100,null=True,blank=True)
     task =models.CharField(max_length=100,null=True,blank=True)

class farmer(models.Model):
     loginid=models.ForeignKey(Usertable,on_delete=models.CASCADE,null=True,blank=True)
     name =models.CharField(max_length=100,null=True,blank=True)
     address =models.CharField(max_length=100,null=True,blank=True)
     place =models.CharField(max_length=100,null=True,blank=True)
     mob_no =models.CharField(max_length=100,null=True,blank=True)
     K_bhavan =models.CharField(max_length=100,null=True,blank=True)
     farmLocation = models.CharField(max_length=255, null=True, blank=True) 

class business(models.Model):
     loginid=models.ForeignKey(Usertable,on_delete=models.CASCADE,null=True,blank=True)
     name =models.CharField(max_length=100,null=True,blank=True)
     address =models.CharField(max_length=100,null=True,blank=True)
     place =models.CharField(max_length=100,null=True,blank=True)
     mob_no =models.CharField(max_length=10,null=True,blank=True)
     businessName =models.CharField(max_length=100,null=True,blank=True)
     businessType =models.CharField(max_length=100,null=True,blank=True)
      
#//////////////// bussiness side start /////////////////////
class notification(models.Model):
     notification =models.CharField(max_length=100,null=True,blank=True)
     date =models.DateTimeField(auto_now_add=True,null=True,blank=True)

class Bcomplaint(models.Model):
     loginid=models.ForeignKey(Usertable,on_delete=models.CASCADE,null=True,blank=True)
     name =models.CharField(max_length=100,null=True,blank=True)
     email =models.CharField(max_length=100,null=True,blank=True)
     Category =models.CharField(max_length=100,null=True,blank=True)
     Details =models.CharField(max_length=1000,null=True,blank=True)
     date =models.DateTimeField(auto_now_add=True,null=True,blank=True)
     docfile =models.FileField(upload_to='bcomplalint',null=True,blank=True) 

     
class ChatHistory(models.Model):

    user_query = models.TextField()  # User's query
    chatbot_response = models.TextField()  # Chatbot's response
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp of the interaction

    def __str__(self):
        return f"Chat at {self.timestamp}"




     
     
