def main(j,jp):
   
    #prepare the platform before copying the files

    # can happen by e.g. installing a debian package e.g. by
    ## j.system.platform.ubuntu.install(packagename)
       
    #install found debs they need to be in debs dir of one or more of the platforms (all relevant platforms will be used)
    #args.qp.installUbuntuDebs()
    
    #shortcut to some usefull install tools
    do=j.system.installtools

    print "get mongodb keys added to apt"
    do.execute("apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10",dieOnNonZeroExitCode=False)
    print "get debs"
    do.execute("echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | tee /etc/apt/sources.list.d/mongodb.list")
    print "update apt metadata"
    j.system.platform.ubuntu.updatePackageMetadata()

    j.system.platform.ubuntu.install("mongodb-org")

    R="""
/etc/mongod.conf
/etc/init/mongod.conf
/etc/init/mongodb.conf
/etc/mongodb.conf
/etc/logrotate.d/mongodb-server
/etc/init.d/mongod
/etc/init.d/mongodb
    """
    for item in R.split("\n"):
        j.system.fs.remove(item)
        
    j.system.fs.createDir("$vardir/mongodb")

    do.execute("apt-get install python-pip -y")
    do.execute("apt-get install build-essential python-dev -y")
    do.execute("pip install pymongo")


    #configuration is not done in this step !!!!!
    #copying files from files section of jpackages is not done in this step
    
    pass