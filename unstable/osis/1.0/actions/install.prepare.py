def main(j,jp):
   
    #prepare the platform before copying the files

    # can happen by e.g. installing a debian package e.g. by
    ## j.system.platform.ubuntu.install(packagename)
       
    #install found debs they need to be in debs dir of one or more of the platforms (all relevant platforms will be used)
    #args.qp.installUbuntuDebs()
    
    #shortcut to some usefull install tools
    #do=j.system.installtools

    #configuration is not done in this step !!!!!
    #copying files from files section of jpackages is not done in this step
    
    jp2=j.packages.findNewest("jumpscale","redis")
    jp2.instance="system"    
    if not jp2.isInstalled():
        jp2.install(hrddata={"redis.name":"production","redis.port":"7768","redis.disk":"1","redis.mem":400},instance="production")
    jp2.start()

    