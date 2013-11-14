from JumpScale import j
def main(j,jp):
    #install the required files onto the system

    # can happen by e.g. installing a debian package e.g. by
    j.system.platform.ubuntu.install("shellinabox")
    j.system.platform.ubuntu.install("byobu")
    j.system.platform.ubuntu.install("screen")
       
    #install found debs they need to be in debs dir of one or more of the platforms (all relevant platforms will be used)
    #args.qp.installUbuntuDebs()
    
    #shortcut to some usefull install tools
    do=j.system.installtools
    do.execute("killall screen")
