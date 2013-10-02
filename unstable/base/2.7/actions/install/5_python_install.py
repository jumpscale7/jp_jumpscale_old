def main(j,args,params,tags,tasklet):

    j.logger.consoleloglevel=6
   
    debpackages = ('python2.7','python-gevent', 'python-simplejson', 'python-numpy','python-psutil', 'python-apt','python-pip','python-imaging','python-requests',"python-paramiko","python-mhash","python-snappy","python-beaker","python-mimeparse", "python-m2crypto","python-iowait")


    for name in debpackages:
        print "check install %s"%name
        j.system.platform.ubuntu.install(name)

    #remove packages which will be installed of this jpackage, they should not be on the system
    toremove=["blosc","msgpack","zmq","pylzma","ujson","urllib3"] #DO NOT REMOVE ipython or circus

    #"cauchyec","galoisbuffer"

    j.system.platform.python.remove(toremove)

    args.qp.copyPythonLibs()

    pypackages = ['ipython']
    
    do=j.system.installtools

    for pp in pypackages:
        # do.execute("pip uninstall %s" % pp)
        do.execute("pip install %s" % pp)

    #configuration is not done in this step !!!!!
    
    params.result=True #return True if result ok
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
