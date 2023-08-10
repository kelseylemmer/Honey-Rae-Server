from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from repairsapi.views import register_user, login_user
from rest_framework import routers
from repairsapi.views import CustomerView, EmployeeView, TicketView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'customers', CustomerView, 'customer')
router.register(r'employees', EmployeeView, 'employee')
router.register(r'tickets', TicketView, 'ticket')

urlpatterns = [
    # Requests to http://localhost:8000/register will be routed to the register_user function
    path('register', register_user),
    # Requests to http://localhost:8000/login will be routed to the login_user function
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
