from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponseRedirect

from common.models import Doctor, Admin


class checkLogin(MiddlewareMixin):
    def process_request(self, request):

        adminpattern = "/admin/"

        isadmin = request.path.startswith(adminpattern)
        if isadmin:
            urls_list = [
                '/common/login/index.html',
                '/common/login/checkLogin.html',
                '/common/login/register.html',
            ]
            if request.path not in urls_list:
                admin_id = request.session.get("admin_id", "")
                admin_password = request.session.get("admin_password", "")
                if admin_id == "" or admin_id is None or admin_password == "" or admin_password is None:
                    return HttpResponseRedirect('/common/login/index.html')
                else:
                    try:

                        rows = Admin.objects.get(id=admin_id)
                        if rows.password == admin_password:
                            if rows.status == '0':
                                status = 0
                                msg = 'Account unavailable'

                                del request.session["admin_id"]
                                del request.session["admin_password"]
                            else:
                                status = 1
                                msg = 'Allow login'
                        else:
                            status = 0
                            msg = 'Incorrect password'

                            del request.session["admin_id"]
                            del request.session["admin_password"]
                    except Admin.DoesNotExist:
                        status = 0
                        msg = 'username does not exist'
                    if status == 0:
                        return HttpResponseRedirect('/common/login/index.html')
        else:
            doctorpattern = '/doctor/'
            isdoctor = request.path.startswith(doctorpattern)

            urls_list = [
                '/common/login/index.html',
                '/common/login/checkLogin.html',
                '/common/login/register.html',
            ]
            if isdoctor:
                if request.path not in urls_list:
                    doctor_id = request.session.get("doctor_id", "")
                    doctor_password = request.session.get("doctor_password", "")
                    if doctor_id == "" or doctor_id is None or doctor_password == "" or doctor_password is None:
                        return HttpResponseRedirect('/common/login/index.html')
                    else:
                        try:

                            rows = Doctor.objects.get(id=doctor_id)
                            if rows.password == doctor_password:
                                if rows.status == '0':
                                    status = 0
                                    msg = 'Account unavailable'

                                    del request.session["doctor_id"]
                                    del request.session["doctor_password"]
                                else:
                                    status = 1
                                    msg = 'Allow login'
                            else:
                                status = 0
                                msg = 'Incorrect password'

                                del request.session["doctor_id"]
                                del request.session["doctor_password"]
                        except Doctor.DoesNotExist:
                            status = 0
                            msg = 'username does not exist'
                        if status == 0:
                            return HttpResponseRedirect('/common/login/index.html')

    def process_response(self, request, response):
        # print("url：" + request.path)
        return response
