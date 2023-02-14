from django.urls import path
from .views import *
urlpatterns=[
    path("index/",index),
    path('user_index/',user_index),
    # path("home/",home)
    # path('reg/',registration),
    path('log/',login),
    path('user_reg/',userreg),
    path('user_login/',userlogin),
    path('user details/',userdetails),
    path('appoinment/<int:id>',appo),
    # path('appo/<int:id>',show),
    path('show/',appoint),
    path('userprofile',userprofile),
    path('payment/',pay),
    path('admin index/',adminindex),
    path('services/',serviceadd),
    path('service display/',servicedisplay),
    path('admin display/',service_edit),
    path('service edit/<int:id>',edit_service),
    path('service delete/<int:id>',delete),
    path('payment/<str:ag>',pay)

]