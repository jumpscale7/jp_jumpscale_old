def main(j,args,params,tags,tasklet):

    j.system.platform.ubuntu.install("tuxcmd")
    j.system.platform.ubuntu.install("xfe")

    p=j.packages.ui.find("sublimetext*")
    p.install()

    p=j.packages.ui.find("nxfree_server*")
    p.install()

    e="add-apt-repository ppa:alexx2000/doublecmd"
    j.system.installtools.execute(e)
    e="apt-get update"
    j.system.installtools.execute(e)

    try:
        j.system.platform.ubuntu.install("doublecmd-gtk")
    except:
        e="add-apt-repository ppa:alexx2000/doublecmd"
        j.system.installtools.execute(e)
        e="apt-get update"
        j.system.installtools.execute(e)
        j.system.platform.ubuntu.install("doublecmd-gtk")

    args.qp.copyFiles(destination="/")


    params.result=True #return True if result ok
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
