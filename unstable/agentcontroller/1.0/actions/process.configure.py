def main(j,jp):
    #configure the application to autostart
    # jp.log("set autostart $(jp.name)")


    sm=j.tools.startupmanager

    cmd = 'jsprocess restart -n webdis;python controller.py'
    args = ''
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'agentcontroller')
    name="agentcontroller"
    startstoptimeout=20
    j.tools.startupmanager.addProcess(name, cmd, args=args, env={}, numprocesses=1, priority=20, shell=False, workingdir=workingdir,jpackage=jp,domain="",\
        ports=[4444],check=True,timeoutcheck=startstoptimeout,stats=True,upstart=False)


