"""
URL configuration for Agrinova project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    #/////////////////////////// ADMIN //////////////////////
    path('',Adminhome.as_view(),name='Home12'),
    path('login/',Login.as_view(),name='login'),
     path('Registration/',Registration.as_view(),name='registration'),
    #////////////////// policy cread////////////////////////
    path('Policy/',policy_add.as_view(),name='Policy_add'),
    path('Policy_List/',policy_List.as_view(),name='Policy_List'),
    path('policy_Edit/<int:id>',policy_Edit.as_view(),name='policy_Edit'),
    path('policy_Delete/<int:id>',policy_Delete.as_view(),name='Policy_Delete'),

    #/////////////////////// end///////////////////////////////
    path('Approval/',Approval.as_view(),name='Approval12'),
    path('Acceptfarmer/<int:id>',Acceptfarmer.as_view(),name='Acceptfarmer'),
    path('Rejectfarmer/<int:id>',Rejectfarmer.as_view(),name='Rejectfarmer'),

    #///////////////////////// complaint //////////////////////
    path('Complaint/',Complaint.as_view(),name='Complaint12'),
    path('complaintreplay/<int:id>',complaintReply.as_view(),name='complaintreplay'),

    #//////////////// complaint end /////////////////////////////////////

    #//////////////// feedback start /////////////////////////
    path('Feedback/',Feedback.as_view(),name='Feedback12'),
     path('feedbackreply/<int:id>',FeedbackReply.as_view(),name='Feedbackreply'),
     #/////////////feedback end ///////////////////////

     #//////////////labour /////////////////////
    path('Labour/',Labour.as_view(),name='Labour12'),

#//////////////// bussiness side start /////////////////////
     #//////////////notification /////////////////////
    path('Notification/',Notification.as_view(),name='Notification12'),

    #////////////// products /////////////////////
    path('Product/',Product.as_view(),name='product12'), 

#//////////////// complaint /////////////////////////////////
path('Bcomplaint/',bussinesscomplaint.as_view(),name='bcomplaint'),
path('complaint_List/',b_complaintlist.as_view(),name='complaint_List'),
path('complaint_Edit/<int:id>',complaint_Edit.as_view(),name='complaint_Edit'),
path('complaint_Delete/<int:id>',complaint_Delete.as_view(),name='complaint_Delete'),

#//////////////// Cart  /////////////////////////////////
path('Cart/',Cart.as_view(),name='cart12'),
path('Addtocart/<int:productid>/',Addtocart.as_view(),name='Addtocart'),
path('delete-cart-item/<int:cart_item_id>/', DeleteCartItem.as_view(), name='delete_cart_item'),

#//////////////// Request /////////////////////////////////
path('Request_list/',request_list.as_view(), name='request_list'),
path('Addtorequest/<int:productid>/',Addtorequest.as_view(),name='AddtoRequest'),
path('delete-request-item/<int:request_item_id>/', DeleteRequestItem.as_view(), name='Delete_request_item'),
path('update-quantity/<int:product_id>/', UpdateQuantity.as_view(), name='update_quantity'),
##############api########################
path('registration',CreateUserView.as_view(),name='CreateUserView'),
path('Viewprofile/<int:id>',Viewprofile.as_view(),name='Viewprofile'),
path('LoginPage',LoginPage.as_view(),name='LoginPage'),
path('ViewProducts/<int:id>',ViewProducts.as_view(),name='ViewProducts'),
path('ViewNotifications',ViewNotifications.as_view(),name='ViewNotifications'),
path('ViewRequests/<int:id>',ViewRequests.as_view(),name='ViewRequests'),
path('create_labour/', LabourCreateView.as_view(), name='create_labour'),
path('complaintsapi/', ComplaintAPIView.as_view(), name='complaints-api'),
path('market-trends/', MarketTrendAPIView.as_view(), name='market-trend-api'),
path('chatbotapi',chatbotapi.as_view(),name='chatbotapi'),
path('CategoryAPIView',CategoryAPIView.as_view(),name='CategoryAPIView'),

    
]
