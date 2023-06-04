from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', MyProjectLoginView, name= 'reg'),
    path('manager/', manager, name= 'manager'),
    path('manager/add',add_manger,name = 'add_manager'),
    path('manager/change', change_manager, name = 'change-manager'),
    path('marketer/', marketer, name= 'marketer'),
    path('marketer/add',add_marketer,name = 'add_marketer'),
    path('marketer/change', change_marketer, name = 'change-marketer'),
    path('adm/', admin, name = 'adm'),
    path('adm/add', admin_add, name = 'admin-add'),
    path('adm/inst/', admin_inst, name = 'adm-inst'),
    path('adm/mark/', admin_mark, name = 'adm-mark'),
    path('adm/pol/', admin_pol, name = 'adm-pol'),
    path('adm/eqp/', admin_eqp, name = 'adm-eqp'),
    path('adm/auth/', admin_auth, name = 'adm-auth')
]