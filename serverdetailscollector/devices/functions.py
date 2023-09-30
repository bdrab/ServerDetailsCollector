import paramiko
import re
from .models import Device
from django.http import HttpResponse

USERNAME = "bartek"
PASSWORD = "12345678"


def refresh_data():
    all_devices = Device.objects.all()

    for device in all_devices:
        host = device.ip
        port = device.port

        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=USERNAME, password=PASSWORD, port=port)

        # RAM usage
        _stdin, _stdout, _stderr = client.exec_command("free")
        a = _stdout.readlines()
        values = re.split('\s+', a[1].strip())

        # system version
        _stdin, _stdout, _stderr = client.exec_command("uname -r")
        a = _stdout.read().decode().strip()
        client.close()

        # modify database
        device.free_space = values[3]
        device.available_space = values[1]
        device.system = a
        device.save()


def check_connection(ip, port):
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=USERNAME, password=PASSWORD, port=port)
    try:
        _stdin, _stdout, _stderr = client.exec_command("pwd", timeout=5)
        return True
    except Exception as e:
        return False


def add(request):

    hostname = request.POST["hostname"]
    ip = request.POST["ip"]
    port = int(request.POST["port"])
    print(hostname, ip, port)
    if check_connection(ip, port):
        try:
            new_device = Device.objects.create(hostname=hostname, ip=ip, port=port)
            new_device.save()
        except Exception as e:
            return HttpResponse(status=500)
    else:
        return HttpResponse(status=500)

    return HttpResponse(status=204)

