from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.http import Http404, HttpResponse,JsonResponse,HttpResponseBadRequest

from .serializer import ComplaintSerializer, ComplaintSerializer1, Farmerserializer, LabourSerializer, NotificationsSerializer, ProductsSerializer, ProductsSerializer1, RequestsSerializer, UsertableSerializer
from .form import *
from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# /////////////////////////// ADMIN //////////////////////////////////
class Login(View):
     def get(self,request):
         return render(request,'admintemp/login.html')
     def post(self,request):
          # Get the username and password from the POST request
          username = request.POST.get('username')
          password = request.POST.get('password')
          print(username,password)
          try:
               obj = Usertable.objects.get(username=username, password=password)
               request.session['user_id']=obj.id
               if obj.type == 'admin':
                    return render(request,'admintemp/adminhome.html')
               elif obj.type == 'user':
                     return render(request, 'userdashboard.html')
               elif obj.type == 'business':
                     return redirect('product12')
               
               else:
                    return HttpResponse('''<script>alert('invalid username or password'); window.location.href='/login/'</script>''')
          except Usertable.DoesNotExist:
                return HttpResponse('''<script>alert('invalid username or password'); window.location.href='/login/'</script>''')
                return redirect('login') 

class Adminhome(View):
    def get(self,request):
         return render(request,'admintemp/adminhome.html')
    

# class Registration(View):
#     def get(self, request):
#         return render(request, 'admintemp/registration.html')
    
class Registration(View):
    def get(self, request):
        return render(request, 'admintemp/registration.html')

    def post(self, request):
        # Handle form submission
        user_type = request.POST.get('userType')
        full_name = request.POST.get('fullName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        place = request.POST.get('place')
        address = request.POST.get('address')
        password = request.POST.get('password')

        # Create a user in the Usertable
        user = Usertable.objects.create(
            username=email,
            password=password,  # Hash the password
            type=user_type,
        )

        # Handle farmer and merchant-specific data
        if user_type == 'farmer':
            k_bhavan = request.POST.get('kBhavanId')
            farm_location = request.POST.get('farmLocation')

            farmer.objects.create(
                loginid=user,
                name=full_name,
                address=address,
                mob_no=phone,
                place=place,
                K_bhavan=k_bhavan,
                farmLocation=farm_location,
            )

        elif user_type == 'business':
            business_name = request.POST.get('businessName')
            business_type = request.POST.get('businessType')

            business.objects.create(
                loginid=user,
                name=full_name,
                address=address,
                mob_no=phone,
                place=place,
                businessName=business_name,
                businessType=business_type,
            )

        # Display a success message and redirect
        messages.success(request, 'Registration successful!')
        return redirect('login')  # Replace with the appropriate success page URL

 
class Approval(View):
     def get(self,request):
          form =  farmer.objects.all()
          return render(request,'admintemp/approval.html',{'form': form})

class Acceptfarmer(View):
         def get(self,request,id):
          
          c=farmer.objects.filter(id=id).first()
          print(c)
          d=Usertable.objects.filter(id=c.loginid.id).first()
          print(d)
          d.statusl='approved'
          d.save()
          print(f"Saving: {d}")
          form =  farmer.objects.all()
          return render(request,'admintemp/approval.html',{'form': form})
class Rejectfarmer(View):
         def get(self,request,id):
          c=farmer.objects.filter(id=id).first()
          d=Usertable.objects.get(id=c.loginid.id)
          print(d)
          d.statusl='rejected'
          d.save()
          form =  farmer.objects.all()
          return render(request,'admintemp/approval.html',{'form': form})
        



class Complaint(View):
     
     def get(self,request):
          form = complaint.objects.all()
          return render(request,'admintemp/complaintbox.html' , {'form': form})

class complaintReply(View):
    def get(self, request, id):
        # Fetch the feedback object using the ID
        c = get_object_or_404(complaint, pk=id)
        return render(request, 'admintemp/complaintreply.html', {'c': c})
    def post(self,request,id):
         c = get_object_or_404(complaint, pk=id)
         c.reply=request.POST['replyMessage']
         c.status=request.POST['resolutionStatus']
         c.save()
         return redirect('Complaint12')

# //////////////////////////////// labour  ////////////////////////////////////
# class policy_List(View):
#     def get(self, request):
#         form = policy.objects.all()
#         return render(request, 'admintemp/policy_list.html', {'form': form})

     
class Labour(View):
     def get(self,request):
          form =  labour.objects.all()
          return render(request,'admintemp/labourreport.html' , {'form': form})



# //////////////////////////////// POLICY CREAD ////////////////////////////////////

class policy_add(View):
     def get(self,request):
          return render(request,'admintemp/policy_add.html')
     def post(self,request):
          form =policyform(request.POST, request.FILES)
          if form.is_valid():
              form.save()
          return redirect('Policy_List')

class policy_List(View):
    def get(self, request):
        form = policy.objects.all()
        return render(request, 'admintemp/policy_list.html', {'form': form})

class policy_Edit(View):
    def get(self,request,id):
        new = policy.objects.get(pk=id)
        return render(request, 'admintemp/policy_edit.html', {'form': new})
    def post(self,request,id):
        new = policy.objects.get(pk=id)
        form = policyform(request.POST, request.FILES, instance=new)
        if form.is_valid(): 
            form.save()
            return redirect('Policy_List')
     #    return render(request, 'admintemp/policy_Edit.html', {'form': form})

class policy_Delete(View):
    def get(self, request,id):
        new = policy.objects.get(pk=id)
        new.delete()
        return HttpResponse('''<script>alert('delete successfully'); window.location.href='/Policy_List/'</script>''')
    
      
 
# //////////////////////////////// Ending POLICY CRUD ////////////////////////////////////

#////////////////////// Feedback ///////////////////////////////////
class Feedback(View):
    def get(self, request):
        # Fetch all feedback records
        c = feedback.objects.all()
        return render(request, 'admintemp/feedback.html', {'c': c})

class FeedbackReply(View):
    def get(self, request, id):
        # Fetch the feedback object using the ID
        c = get_object_or_404(feedback, pk=id)
        return render(request, 'admintemp/feedback_reply.html', {'c': c})
    def post(self,request,id):
         c = get_object_or_404(feedback, pk=id)
         c.reply=request.POST['replyMessage']
         c.save()
         return redirect('Feedback12')


         

#//////////////// Feedback end /////////////////////////////////


#//////////////// bussiness side start /////////////////////
#//////////////// Notification /////////////////////////////////
class Notification(View):
     def get(self,request):
          n = notification.objects.all()
          return render(request,'bussiness/notification.html',{'form': n})

#//////////////// Product /////////////////////////////////
class Product(View):
     def get(self,request):
          p = product.objects.all()
          return render(request,'bussiness/bussinesshome.html',{'form': p})

#//////////////// complaint crad /////////////////////////////////
class bussinesscomplaint(View):
     def get(self,request):
          return render(request,'bussiness/b_complaint.html')
     def post(self,request):
          form =bcomplaintform(request.POST, request.FILES)
          if form.is_valid():
              form.save()
          return redirect('complaint_List')

class b_complaintlist(View):
    def get(self, request):
        form =Bcomplaint.objects.all()
        return render(request, 'bussiness/complaint_list.html', {'form': form})

class complaint_Edit(View):
    def get(self,request,id):
        new = Bcomplaint.objects.get(pk=id)
        return render(request, 'bussiness/complaint_edit.html', {'form': new})
    def post(self,request,id):
        new =Bcomplaint.objects.get(pk=id)
        form =bcomplaintform(request.POST, request.FILES, instance=new)
        if form.is_valid():
            form.save()
            return redirect('complaint_List')
     

class complaint_Delete(View):
    def get(self, request,id):
        new = Bcomplaint.objects.get(pk=id)
        new.delete()
        return HttpResponse('''<script>alert('delete successfully'); window.location.href='/complaint_List/'</script>''')
#//////////////// complaint crad  end/////////////////////////////////

class Cart(View):
     def get(self,request):
          c = cart.objects.filter(loginid__id=request.session.get('user_id')).all()
          return render(request,'bussiness/cart.html',{'form': c})  

class DeleteCartItem(View):
    def post(self, request, cart_item_id):
        cart_item = get_object_or_404(cart, id=cart_item_id)
        cart_item.delete()
        return redirect('cart12')


class Addtocart(View):
    def post(self, request, productid):
        # Get the logged-in user
        user_id = request.session.get('user_id')
        if not user_id:
            return HttpResponseBadRequest("User not logged in.")

        login_user = get_object_or_404(Usertable, id=user_id)
        product_item = get_object_or_404(product, id=productid)

        # Get the quantity from the POST request, defaulting to 1
        quantity = int(request.POST.get('quantity', 1))

        # Retrieve or create the cart item
        cart_item, created = cart.objects.get_or_create(
            loginid=login_user,
            productid=product_item,
            defaults={'quantity': quantity}
        )

        # If the cart item already exists, update the quantity to match the submitted value
        if not created:
            cart_item.quantity = quantity
            cart_item.save()

        return redirect('cart12')



class request_list(View):
    def get(self,request):
      r= requesttable.objects.all() 

      return render(request,'bussiness/request.html',{'form': r}) 

class DeleteRequestItem(View):
    def post(self, request, request_item_id):
        request_item = get_object_or_404(requesttable, id=request_item_id)
        request_item.delete()
        return redirect('request_list')  

class Addtorequest(View):
    def post(self, request, productid):
        # Get the logged-in user
        user_id = request.session.get('user_id')
        if not user_id:
            return HttpResponseBadRequest("User not logged in.")

        login_user = get_object_or_404(Usertable, id=user_id)
        product_item = get_object_or_404(product, id=productid)

        # Get the quantity from the POST request, defaulting to 1
        try:
            quantity = int(request.POST.get('quantity', 1))
            if quantity < 1:
                return HttpResponseBadRequest("Invalid quantity.")
        except ValueError:
            return HttpResponseBadRequest("Invalid quantity.")

        # Retrieve or create the request item
        request_item, created = requesttable.objects.get_or_create(
            loginid=login_user,
            productid=product_item,
            defaults={'quantity': quantity}
        )

        if not created:
            # Increment the quantity if the item already exists
            request_item.quantity += quantity
            request_item.save()

        return redirect('request_list')



class UpdateQuantity(View):
    def post(self, request, product_id):
        # Get the product
        product_instance = get_object_or_404(product, id=product_id)
        # Get the new quantity from the POST data
        try:
            new_quantity = int(request.POST.get('quantity', 1))
        except ValueError:
            return JsonResponse({'error': 'Invalid quantity value'}, status=400)
        # Update the product's quantity
        product_instance.Quantity = new_quantity
        product_instance.save()
        # this sae creted for checkingf
        return JsonResponse({'message': 'Quantity updated successfully', 'new_quantity': product_instance.Quantity})


# ////////////////////////////// API ////////////////////////////////////////////

class CreateUserView(APIView):
    def post(self, request):
        print(request.data)
        serializer = UsertableSerializer(data=request.data)
        serializer1 = Farmerserializer(data=request.data)
        if serializer.is_valid() and serializer1.is_valid():
            print(serializer)
            print(serializer1)
            c=serializer.save()
            serializer1.save(loginid=c)
            return Response({"message": "User created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class Viewprofile(APIView):
    def get(self, request, id):
            print("222222222222222222")
            user = farmer.objects.get(loginid__id=id)
            serializer = Farmerserializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        

class ViewProducts(APIView):
    def get(self, request,id):
        Products = product.objects.filter(loginid__id=id).all()
        Products_serializer = ProductsSerializer1(Products, many=True)
        # print("-----> Offer images:", Products_serializer.data)
        return Response(Products_serializer.data)
    def post(self, request, id):
        # Add a new product associated with the given loginid


        serializer = ProductsSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ViewNotifications(APIView):
    def get(self, request):
        Notifications = notification.objects.all()
        Notifications_serializer = NotificationsSerializer(Notifications, many=True)
        # print("-----> Offer images:", Products_serializer.data)
        return Response(Notifications_serializer.data)
    
class ViewRequests(APIView):
    def get(self, request,id):
        Requests = requesttable.objects.filter(loginid__id=id).all()
        Requests_serializer = RequestsSerializer(Requests, many=True)
        print("-----> Offer images:", Requests_serializer.data)
        return Response(Requests_serializer.data)
    
    def put(self, request, id):
        try:
            request_instance = requesttable.objects.get(id=id)
        except requesttable.DoesNotExist:
            return Response({"error": "Request not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = RequestsSerializer(request_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ViewComplaints(APIView):
    def get(self, request):
        Complaints = complaint.objects.all()
        Complaints_serializer = ComplaintSerializer(Complaints, many=True)
        # print("-----> Offer images:", Products_serializer.data)
        return Response(Complaints_serializer.data)
    def post(self, request):
        # Add a new complaint
        serializer = ComplaintSerializer1(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginPage(APIView):
    def post(self, request):
        response_dict = {}

        # Get data from the request
        username = request.data.get("username")
        password = request.data.get("password")
        print(username)
        print(password)
        # Validate input
        if not username or not password:
            response_dict["message"] = "failed"
            return Response(response_dict, status=status.HTTP_400_BAD_REQUEST)
         # Fetch the user from LoginTable
        t_user = Usertable.objects.filter(username=username,password=password).first()

        if not t_user:
            response_dict["message"] = "failed"
            return Response(response_dict, status=status.HTTP_401_UNAUTHORIZED)



        # Successful login response
        response_dict["message"] = "success"
        response_dict["login_id"] = t_user.id
        return Response(response_dict, status=status.HTTP_200_OK)
class LabourCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LabourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ComplaintAPIView(APIView):
    """
    API view for managing complaints.
    """
    
    def get(self, request,id):
        complaints = complaint.objects.filter(loginid=id)
        complaints = complaint.objects.all()
        serializer = ComplaintSerializer(complaints, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.db.models import Avg, Sum, F
from django.utils.timezone import now, timedelta
class MarketTrendAPIView(APIView):
    """
    API view to analyze market trends for the last week and this week.
    """

    def get(self, request):
        # Define date ranges
        today = now().date()
        start_of_this_week = today - timedelta(days=today.weekday())
        start_of_last_week = start_of_this_week - timedelta(days=7)

        # Query for products grouped by category
        categories = product.objects.values('category').distinct()
        print(categories)

        trend_data = []

        for category in categories:
            category_id = category['category']
                       # Get the category name
            category_name = Category.objects.filter(id=category_id).values_list('category_name', flat=True).first()


            # Calculate average price for last week and this week
            last_week_price = (
                product.objects.filter(category_id=category_id, date__range=[start_of_last_week, start_of_this_week])
                .aggregate(avg_price=Avg('price'))
                .get('avg_price') or 0
            )
            this_week_price = (
                product.objects.filter(category_id=category_id, date__gte=start_of_this_week)
                .aggregate(avg_price=Avg('price'))
                .get('avg_price') or 0
            )

            # Calculate total demand (sum of quantities) for this category
            total_demand = (
                requesttable.objects.filter(productid__category_id=category_id)
                .aggregate(total_quantity=Sum('quantity'))
                .get('total_quantity') or 0
            )

            # Add data to the response list
            trend_data.append({
                "productcategory": category_id,
                "productcategoryname": category_name,
                "last_week_price": last_week_price,
                "this_week_price": this_week_price,
                "demand": total_demand
            })

        return Response(trend_data, status=status.HTTP_200_OK)
class CategoryAPIView(APIView):
    """
    API view to retrieve all categories.
    """

    def get(self, request):
        # Query all categories
        categories = Category.objects.all().values('id', 'category_name')
        
        # Convert to list for JSON response
        category_list = list(categories)
        
        return Response(category_list, status=status.HTTP_200_OK)
    
from rest_framework import status
import pandas as pd
import joblib

model_path = "crop_recommendation_model.joblib"
clf = joblib.load(model_path)
print("Model loaded successfully.")

class CropRecommendationAPIView(APIView):
    def post(self, request):
        try:
            data = request.data
            n = float(data.get("N"))
            p = float(data.get("P"))
            k = float(data.get("K"))
            temperature = float(data.get("temperature"))
            humidity = float(data.get("humidity"))
            ph = float(data.get("ph"))
            rainfall = float(data.get("rainfall"))

            input_data = pd.DataFrame({'N': [n], 'P': [p], 'K': [k],
                                       'temperature': [temperature], 'humidity': [humidity],
                                       'ph': [ph], 'rainfall': [rainfall]})
            prediction = clf.predict(input_data)
            return Response({'recommended_crop': prediction[0]}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

import google.generativeai as genai

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ChatHistory
# Initialize Google Gemini API
genai.configure(api_key="AIzaSyA0USMpFTzWEzYM3EqiTyXCYKKdbeZ9BIE")  # Replace with your Gemini API key


class chatbotapi(APIView):
    def post(self, request):
        # Get query from the user input
        user_query = request.data.get('query', '')

        # Default response if no input
        response_data = {
            'chatbot_response': "",
            "chat_history": [],   # This will store the chatbot-like response
        }


        # Construct the prompt using the filtered data (ensure it's only from the models)
        print(user_query)
        prompt = (
            f"User Query: {user_query}. "
            f"Provide the response based on above data"
        )

        try:
            # Call Gemini API to generate the response
            gemini_response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
            gemini_chatbot_response = gemini_response.text.strip()
            print(user_query)
            ChatHistory.objects.create(
                user_query=user_query,
                chatbot_response=gemini_chatbot_response,
            )

            # Update response data with the chatbot response
            response_data['chatbot_response'] = gemini_chatbot_response
                        # Retrieve the chat history
            chat_history = ChatHistory.objects.order_by("-timestamp").values(
                "user_query", "chatbot_response", "timestamp"
            )
            response_data.update(
                {

                    "chatbot_response": gemini_chatbot_response,
                    "chat_history": list(chat_history),
                }
            )

            



            # Return the chatbot-like response with the itinerary data
            return Response(response_data, status=200)
        
        except Exception as e:
            return Response({"error": str(e)}, status=400)