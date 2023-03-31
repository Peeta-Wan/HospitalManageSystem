from django.urls import path
from common.controllers import login

urlpatterns = [

    path('login/index.html', login.index, name='common_login'),
    path('login/logout.html', login.logout),
    path('login/checkLogin.html', login.checkLogin),
]
