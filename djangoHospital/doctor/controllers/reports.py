import json
import time

from django.http import HttpResponse
from django.shortcuts import render

from common.models import User, Doctor, Reports


def index(request):

    ajax = request.GET.get('ajax')

    if ajax is not None:

        page = request.GET.get('page') if request.GET.get('page') is not None else 1
        page = int(page)

        limit = request.GET.get('limit') if request.GET.get('limit') is not None else 10
        limit = int(limit)
        start = (int(page) - 1) * int(limit)
        end = int(page) * int(limit)

        doctor_id = request.session.get("doctor_id", "")

        rows = Reports.objects.filter(doctor_id=doctor_id)
        count = Reports.objects.filter(doctor_id=doctor_id)

        rows = rows[start:end].values()
        count = count.count()
        rows = list(rows)
        for i, value in enumerate(rows):
            rows[i]['addtime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(rows[i]['addtime'])))

            user = User.objects.filter(id=rows[i]['user_id']).first()
            if user is not None:
                rows[i]['user'] = user.realname

            doctor = Doctor.objects.filter(id=rows[i]['doctor_id']).first()
            if doctor is not None:
                rows[i]['doctor'] = doctor.realname

        data = {"code": 0, "msg": "", "count": count, "data": rows}

        return HttpResponse(json.dumps(data))
    else:
        return render(request, 'admin/reports/index.html')


def edit(request):
    id = request.GET.get('id')
    info = Reports.objects.get(id=id)
    return render(request, 'admin/reports/edit.html', {'info': info})
