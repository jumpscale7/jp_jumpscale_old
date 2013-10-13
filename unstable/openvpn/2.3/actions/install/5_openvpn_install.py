def main(j,args,params,tags,tasklet):
   
    #install the required files onto the system

    # can happen by e.g. installing a debian package e.g. by
    j.system.platform.ubuntu.install("openvpn")
    j.system.platform.ubuntu.install("python-ipy")
    # j.system.platform.ubuntu.install("easy-rsa")

    

    ##copy python libs: then need to be in subdir site-packages of one of the platforms, they will all be copied to site-packages in local python dir
    #args.qp.copyPythonLibs(remove=False)

    #install found debs they need to be in debs dir of one or more of the platforms (all relevant platforms will be used)
    #args.qp.installUbuntuDebs()
    
    #shortcut to some usefull install tools
    #do=j.system.installtools

    #configuration is not done in this step !!!!!
    
    params.result=True #return True if result ok
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
