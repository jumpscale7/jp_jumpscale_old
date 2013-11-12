from JumpScale import j
def main(jp):
    j.system.platform.ubuntu.install('msgpack-python')
    j.system.platform.ubuntu.install('python-gevent')

    if j.system.platform.ubuntu.check():
        j.system.platform.ubuntu.install('avahi-utils')
