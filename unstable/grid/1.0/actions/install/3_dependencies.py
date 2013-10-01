def main(j, args, params, tags, tasklet):


    def _installPythonPackage(name):
        j.system.platform.python.install(name)
    
    _installPythonPackage('msgpack-python')
    j.system.platform.ubuntu.install('python-gevent')
    j.system.platform.ubuntu.install('libleveldb-dev')
    j.system.platform.ubuntu.install('libleveldb1')
    _installPythonPackage('ujson') 
    _installPythonPackage('pyzmq')
    
    params.result = True  # return True if result ok
    return params


def match(j, args, params, tags, tasklet):
    return True
