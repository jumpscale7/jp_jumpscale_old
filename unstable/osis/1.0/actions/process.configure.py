def main(j,jp):
   
    #configure the application to autostart
    
    jp.log("set autostart $(jp.name)")


    #numprocesses: if more than 1 process, will be started in tmux as $name_$nr
    #ports: tcpports
    #autostart: does this app start auto
    #stopcmd: if special command to stop
    #check: check app to see if its running
    #stats: gather statistics by process manager
    #timeoutcheck: how long do we wait to see if app active
    #isJSapp: to tell system if process will self register to redis (is jumpscale app)

    pd=j.tools.startupmanager.addProcess(\
        name=jp.name,\
        cmd="", \
        args="",\
        env={},\
        numprocesses=1,\
        priority=100,\
        shell=False,\
        workingdir="$base/apps/osis",\
        jpackage=jp,\
        domain=jp.domain,\
        ports=jp.ports,\
        autostart=True,\
        reload_signal=0,\
        user="root",\
        log=True,\
        stopcmd=None,\
        check=True,\
        timeoutcheck=10,\
        isJSapp=1,\
        upstart=False,\
        stats=False,\
        processfilterstr="")#what to look for when doing ps ax to find the process
    
    pd.start()

    #configure the application to autostart
    jp.log("set autostart $(jp.name)")
    # #example start osis
    cmd = 'python'
    args = 'osisServerStart.py'
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'osis')
    startstoptimeout=20
    j.tools.startupmanager.addProcess("osis", cmd, args=args, priority=15, ports=[5544], workingdir=workingdir,jpackage=jp,\
        check=True,timeoutcheck=startstoptimeout,stats=True,upstart=False)
    
    j.tools.startupmanager.startJPackage(jp)



    j.system.platform.screen.executeInScreen("$jp_domain","$jp_name__$jp_instance",cmd,cwd="$base/apps/osis", env={},user="root")
