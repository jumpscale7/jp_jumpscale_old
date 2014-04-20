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

    # j.tools.startupmanager.stopJPackage(j.packages.findNewest(name="workers"))
    for proc in [item for item in j.tools.startupmanager.listProcesses() if item.find("_worker")<>-1]:
        dom,name=proc.split("__")
        j.tools.startupmanager.removeProcess(dom,name)

    j.system.fs.remove(j.system.fs.joinPaths(j.dirs.cfgDir,"hrd","workers.hrd"))
