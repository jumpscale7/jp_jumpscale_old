
def main(j,jp):
    j.system.platform.ubuntu.install('msgpack-python')
    j.system.platform.ubuntu.install('python-gevent')
    j.system.platform.python.install('grequests', latest=False)

    j.system.platform.ubuntu.install('avahi-utils')
