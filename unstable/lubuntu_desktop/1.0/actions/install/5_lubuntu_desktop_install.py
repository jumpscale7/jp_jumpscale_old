def main(j,args,params,tags,tasklet):
   
    #install the required files onto the system
    # can happen by e.g. installing a debian package e.g. by
    ## j.system.platform.ubuntu.install(packagename)
    # can happen by copying files from the jpackages included files (they come from the bundle) e.g. by
    
    #args.qp.copyFiles() #  will copy files to sandbox
    
    ##params.jpackages.copyFiles(destination="/opt/qbase3") #  will copy files to sandbox qbase3
    
    #configuration is not done in this step !!!!!

    j.system.platformtype.dieIfNotPlatform("linux64")

    j.system.platform.ubuntu.updatePackageMetadata()

    j.system.platform.ubuntu.install("lubuntu-desktop")

    e="apt-get autoclean"
    j.system.installtools.execute(e)
    e="rm /var/cache/apt/archives/*.deb"
    j.system.installtools.execute(e)
    
    params.result=True #return True if result ok
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
