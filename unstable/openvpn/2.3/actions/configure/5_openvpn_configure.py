import pexpect

def main(j,args,params,tags,tasklet):

    from IPy import IP

    privnet=j.application.config.get("openvpn.privatenet")
    ip = IP(privnet)
    privnet=j.application.config.set("openvpn.privatenet.mask",str(ip.netmask()))
    privnet=j.application.config.set("openvpn.privatenet.net",str(ip.net()))

    args.qp.copyFiles(subdir="easy-rsa",destination="%s/apps/easy-rsa"%j.dirs.baseDir,applyhrd=True) #  will copy files from subdir called root of platforms to root of system (carefull), will also use templateEngine for hrd 
    args.qp.copyFiles(subdir="openvpnconfig",destination="/etc/openvpn",applyhrd=True)
   
    #configure the package 
    keydir="%s/cfg/rsakeys"%j.dirs.baseDir
    appdir="%s/apps/easy-rsa"%j.dirs.baseDir

    execute=j.system.process.executeWithoutPipe
    

    if not j.system.fs.exists(keydir) or True:
        j.system.fs.createDir(keydir)
        j.system.fs.changeDir(appdir)
        # cmd=";source vars;./openvpn-build-server"%appdir
        e = pexpect.spawn ("sh")
        e.send("PS1=\"#.#.#\"\n")
        e.expect("#.#.#",timeout=1)
        e.send("cd %s\n"%appdir)
        e.expect("#.#.#",timeout=1)
        e.send("ls\n")
        e.expect("#.#.#",timeout=1)

        from IPython import embed
        print "DEBUG NOW oooe"
        embed()
        
        #execute()
        #execute("cd %s;source vars;./openvpn-build-client"%appdir)


    path="%s/keys"%appdir
    for filter in ["*.crt","*.key","client_*","dh1024.pem"]:
        for source in j.system.fs.listFilesInDir( path, recursive=False, filter=filter):
            dest="/etc/openvpn/%s"%j.system.fs.getBaseName(source)
            j.system.fs.copyFile(source,dest)

    # cmd="iptables -t nat -A POSTROUTING -s $(rsa.privatenet) -o eth0 -j MASQUERADE"
    # execute(cmd)
    # cmd="service iptables save"
    # execute(cmd)

    #enable ip forwarding
    te=j.codetools.getTextFileEditor("/etc/sysctl.conf")
    te.replace1Line("net.ipv4.ip_forward = 1",includes=[".*net.ipv4.ip_forward.*"])
    te.save()

    cmd="sysctl -p"
    execute(cmd)
    cmd="service openvpn start"
    execute(cmd)

    return params
    
    
def match(j,args,params,tags,tasklet):
    return True