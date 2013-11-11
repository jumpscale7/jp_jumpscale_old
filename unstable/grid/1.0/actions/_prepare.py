   
    #install the required files onto the system

    # can happen by e.g. installing a debian package e.g. by
    ## j.system.platform.ubuntu.install(packagename)
       
    #install found debs they need to be in debs dir of one or more of the platforms (all relevant platforms will be used)
    #args.qp.installUbuntuDebs()
    
    #shortcut to some usefull install tools
    #do=j.system.installtools

    #configuration is not done in this step !!!!!
    #copying files from files section of jpackages is not done in this step

    j.system.platform.ubuntu.install('msgpack-python')
    j.system.platform.ubuntu.install('python-gevent')

    if j.system.platform.ubuntu.check():
        j.system.platform.ubuntu.install('avahi-utils')
    
    params.result=True #return True if result ok
    return params
    
    
    return True

