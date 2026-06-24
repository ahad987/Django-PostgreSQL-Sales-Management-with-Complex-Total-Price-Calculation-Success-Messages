from django.urls import path
from myApp.views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('s-up/', sign_up_view, name='sign_up'),
    path('s-in/', signin_view, name='sign_in'),
    path('s-out/', logout_page, name='logout'),
    path('s-list/', sale_list_page, name='sale_list'),
    path('add-sale/', add_sale_page, name='add_sale'),
]
