from django.http import HttpResponse
import json
import time
import hashlib
from django.conf import settings
import os
import shutil


def image(request):
    if request.method == 'POST':
        img1 = request.FILES.get('file')
        img = request.FILES['file']
        file_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        file_name = int(time.time())
        file_path = settings.MEDIA_ROOT + 'temp/' + file_date + '/'  # 构造文件名以及文件路径

        ext = str(img).split('.')

        name = hashlib.md5(str(img).encode('utf-8')).hexdigest() + '.' + ext[-1]

        if not os.path.isdir(file_path):
            os.makedirs(file_path, 493)
        img_name = file_path + str(file_name) + '_' + name
        with open(img_name, 'wb+') as f:
            f.write(img1.read())

        info = {'state': 1, 'msg': 'Upload successful', 'name': file_date + '/' + str(file_name) + '_' + name}
        return HttpResponse(json.dumps(info))


def move_image(request, dest_file, positi_dir):

    file_path = settings.MEDIA_ROOT + 'temp/'

    file_name = file_path + dest_file

    fpath, fname = os.path.split(file_name)

    positi_path = settings.MEDIA_ROOT + positi_dir + '/' + fpath.split('/')[-1]

    if not os.path.isdir(positi_path):
        os.makedirs(positi_path, 493)


    img_name = positi_path + '/' + fname

    shutil.move(file_name, img_name)

    info = {'state': 1, 'msg': 'Upload successful'}

    return json.dumps(info)


def del_image(request, dest_file):
    info = {'state': 1, 'msg': 'Upload successful'}
    if os.path.exists(dest_file):
        os.remove(dest_file)
    return json.dumps(info)
