def main(j,args,params,tags,tasklet):
   
    #install the required files onto the system
    # can happen by e.g. installing a debian package e.g. by
    ## j.system.platform.ubuntu.install(packagename)
    # can happen by copying files from the jpackages included files (they come from the bundle) e.g. by
    
    #args.qp.copyFiles() #  will copy files to sandbox
    
    j.system.platformtype.dieIfNotPlatform("linux64")

    j.system.fs.removeDirTree("/opt/sublimetext")

    args.qp.copyFiles(destination="/") #  will copy files to root
        
    e="sh /opt/sublimetext/install.sh"
    j.system.process.execute(e)

    params.result=True #return True if result ok
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
