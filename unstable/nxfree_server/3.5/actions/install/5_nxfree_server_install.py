def main(j,args,params,tags,tasklet):
   
    #install the required files onto the system
    # can happen by e.g. installing a debian package e.g. by
    ## j.system.platform.ubuntu.install(packagename)
    # can happen by copying files from the jpackages included files (they come from the bundle) e.g. by
    
    #args.qp.copyFiles() #  will copy files to sandbox


    path = args.qp.getPathFilesPlatform('linux64')

    packages = ('nxclient_3.5.0-7_amd64.deb',
                'nxnode_3.5.0-9_amd64.deb',
                'nxserver_3.5.0-11_amd64.deb')

    for package in packages:
        j.system.platform.ubuntu.installDebFile(j.system.fs.joinPaths(path, package))

    
    ##params.jpackages.copyFiles(destination="/opt/qbase3") #  will copy files to sandbox qbase3
    

    te= j.codetools.getTextFileEditor("/usr/NX/etc/server.cfg")
    te.replace1Line("EnableAdministratorLogin = \"1\"",["EnableAdministratorLogin*"])
    te.save()

    j.system.installtools.execute("/etc/init.d/nxserver restart")

    #configuration is not done in this step !!!!!
    
    params.result=True #return True if result ok
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
