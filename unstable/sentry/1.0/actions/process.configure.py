def main(j,jp):
   
    #configure the application to autostart
    
    # jp.log("set autostart $(jp.name)")

    # #example start osis
    # cmd = 'python'
    # args = 'osisServerStart.py'
    # workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'osis')
    # name = jp.name
    # domain = jp.domain
    # ports = jp.ports
    # j.tools.startupmanager.addProcess(name=name, cmd=cmd, args=args, env={}, numprocesses=1, priority=1, \
    #    shell=False, workingdir=workingdir,jpackage=jp,domain=domain,ports=ports)
    
    #can configure more apps to start than just 1 linked to the jpackage


    j.dirs.replaceFilesDirVars("$base/apps/sentry/cfg/")

    import os
    ospath=os.environ["PATH"]


    env={}
    env["VIRTUAL_ENV"]="$base/apps/sentry"
    env["PYTHONPATH"]="$base/apps/sentry/lib/python2.7:$base/apps/sentry/lib/python2.7/site-packages:$base/apps/sentry/lib/python2.7/lib-dynload"
    env["PATH"]="$base/apps/sentry/bin:%s"%ospath

    pd=j.tools.startupmanager.addProcess(\
        name=jp.name,\
        cmd="./sentry --config=$base/apps/sentry/cfg/sentry.conf.py start", \
        args="",\
        env=env,\
        numprocesses=1,\
        priority=100,\
        shell=False,\
        workingdir='$base/apps/sentry/bin',\
        jpackage=jp,\
        domain="jumpscale",\
        ports=[9000],\
        autostart=True,\
        reload_signal=0,\
        user="root",\
        log=True,\
        stopcmd=None,\
        check=True,\
        timeoutcheck=20,\
        isJSapp=False,\
        upstart=False,\
        stats=True,\
        processfilterstr="sentry --config")#what to look for when doing ps ax to find the process
    
    pd.start()



    # cmd = 'source $base/apps/sentry/bin/activate;cd $base/apps/sentry;sentry --config=$base/apps/sentry/cfg/sentry.conf.py start'
    # args = ''
    # workingdir = ""
    # name = 'sentry'
    # domain = "jumpscale"
    # ports = [9000]
    # startstoptimeout=20
    # processfilterstr="sentry --config"
    # j.tools.startupmanager.addProcess(name=name, cmd=cmd, args=args, env={}, numprocesses=1, priority=1, \
    #    shell=False, workingdir=workingdir,jpackage=jp,domain=domain,ports=ports,\
    #    check=True,timeoutcheck=startstoptimeout,stats=True,isJSapp=False,upstart=False,processfilterstr=processfilterstr)


    # pass
