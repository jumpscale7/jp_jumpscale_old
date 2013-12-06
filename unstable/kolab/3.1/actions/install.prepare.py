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

    #See http://docs.kolab.org/installation-guide/ubuntu.html for details

    j.system.installtools.writefile('/etc/apt/sources.list.d/kolab.list', "deb http://obs.kolabsys.com:82/Kolab:/3.1/Ubuntu_13.10/ ./\ndeb http://obs.kolabsys.com:82/Kolab:/3.1:/Updates/Ubuntu_13.10/ ./")

    j.system.installtools.execute("wget http://obs.kolabsys.com:82/Kolab:/3.1/Ubuntu_13.10/Release.key -O /tmp/Release.key",dieOnNonZeroExitCode=False,ignoreErrorOutput=True, useShell=True)
    j.system.installtools.execute("apt-key add /tmp/Release.key",dieOnNonZeroExitCode=False,ignoreErrorOutput=True, useShell=True)
    j.system.installtools.execute("rm -rf /tmp/Release.key",dieOnNonZeroExitCode=False,ignoreErrorOutput=True, useShell=True)
    j.system.installtools.execute("wget http://obs.kolabsys.com:82/Kolab:/3.1:/Updates/Ubuntu_13.10/Release.key -O /tmp/Release.key",dieOnNonZeroExitCode=False,ignoreErrorOutput=True, useShell=True)
    j.system.installtools.execute("apt-key add /tmp/Release.key",dieOnNonZeroExitCode=False,ignoreErrorOutput=True, useShell=True)
    j.system.installtools.execute("rm -rf /tmp/Release.key",dieOnNonZeroExitCode=False,ignoreErrorOutput=True, useShell=True)

    j.system.installtools.writefile('/etc/apt/preferences.d/kolab', "Package: *\nPin: origin obs.kolabsys.com\nPin-Priority: 501")

    j.system.platform.ubuntu.updatePackageMetadata()
    j.system.platform.ubuntu.install('kolab')

