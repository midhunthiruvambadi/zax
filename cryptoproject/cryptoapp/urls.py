from. import views
from django.urls import path,include

urlpatterns = [

    path('',views.demo,name='demo'),
    #  path('about/',views.about,name='about'),
    #  path('contract',views.contract,name='contract'),
    # path('details',views.details,name='details'),
    # path('thanks',views.thanks,name='thanks')

]