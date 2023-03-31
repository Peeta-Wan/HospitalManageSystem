import json

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

from common.models import Admin
from common.models import Doctor


def index(request):

    return render(request, 'common/login/index.html')


def logout(request):

    try:

        del request.session["doctor_username"]
        del request.session["doctor_id"]
        del request.session["doctor_password"]

        del request.session["admin_username"]
        del request.session["admin_id"]
        del request.session["admin_password"]
    except Exception:
        pass
    return redirect(reverse('common_login'))


def checkLogin(request):
    if request.method == 'POST':
        status = 0
        msg = 'Login error'
        username = request.POST.get('username')
        password = request.POST.get('password')
        login_type = request.POST.get('login_type')

        try:

            if login_type == "1":
                rows = Doctor.objects.filter(username=username).first()
                if rows is None:
                    msg = 'Username does not exist'

                elif rows.password == password:
                    if rows.status == 0:
                        msg = 'Account unavailable'
                    else:
                        request.session['doctor_username'] = request.POST.get('username')
                        request.session['doctor_id'] = rows.id
                        request.session['doctor_password'] = request.POST.get('password')
                        status = 1
                        msg = 'Login succeeded'
                else:
                    msg = 'Incorrect password'

            elif login_type == "2":
                rows = Admin.objects.filter(username=username).first()
                if rows is None:
                    msg = 'Username does not exist'

                elif rows.password == password:
                    if rows.status == 0:
                        msg = 'Account unavailable'
                    else:
                        request.session['admin_username'] = request.POST.get('username')
                        request.session['admin_id'] = rows.id
                        request.session['admin_password'] = request.POST.get('password')
                        status = 1
                        msg = 'Login succeeded！'
                else:
                    msg = 'Incorrect password'
        except Doctor.DoesNotExist:
            msg = 'Username does not exist'
        except Admin.DoesNotExist:
            msg = 'Username does not exist'
        ret = {"status": status, "msg": msg}
        return HttpResponse(json.dumps(ret))
