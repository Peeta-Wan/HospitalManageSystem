from django.urls import path
from index.controllers import index
from index.controllers import login
from index.controllers import register
from index.controllers import user
from index.controllers import upload

urlpatterns = [

    path('index/upload/image.html', upload.image),

    path('', index.index, name='index_index'),
    path('index/', index.index, name='index_index'),
    path('index.html', index.index, name='index_index'),
    path('index/index.html', index.index, name='index_index'),
    path('index/appointment.html', index.detail),
    path('index/save.html', index.save),

    path('login/index.html', login.index, name='login_index'),
    path('login/login.html', login.login),
    path('login/logout.html', login.logout),

    path('register/index.html', register.index, name='register_index'),
    path('register/register.html', register.register),

    path('user/center.html', user.center),
    path('user/set.html', user.set),
    path('user/userinfo.html', user.userinfo),
    path('user/password.html', user.password),
    path('user/avatar.html', user.avatar),
    path('user/report.html', user.report),
    path('user/detailReport.html', user.detailReport),

]
