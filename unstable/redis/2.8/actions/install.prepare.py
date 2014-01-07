def main(j,jp):
   
    #prepare the platform before copying the files


    j.system.platform.ubuntu.install("python-redis")
    j.system.platform.ubuntu.checkInstall("redis-server", "redis-server")

    j.system.fs.createDir("/opt/redis/db/redis_cache")
    j.system.fs.createDir("/opt/redis/db/redis_prod")

    # can happen by e.g. installing a debian package e.g. by
    ## j.system.platform.ubuntu.install(packagename)
       
    #install found debs they need to be in debs dir of one or more of the platforms (all relevant platforms will be used)
    #args.qp.installUbuntuDebs()
    
    #shortcut to some usefull install tools
    #do=j.system.installtools

    #configuration is not done in this step !!!!!
    #copying files from files section of jpackages is not done in this step
    
    pass
