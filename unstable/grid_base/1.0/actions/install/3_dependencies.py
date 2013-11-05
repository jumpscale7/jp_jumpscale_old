def main(j, args, params, tags, tasklet):

    j.system.platform.ubuntu.install('msgpack-python')
    j.system.platform.ubuntu.install('python-gevent')

    if j.system.platform.ubuntu.check():
    	j.system.platform.ubuntu.install('avahi-utils')

    params.result = True  # return True if result ok
    return params


def match(j, args, params, tags, tasklet):
    return True
