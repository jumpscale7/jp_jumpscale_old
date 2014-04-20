

def main(j,jp):
    #configure the application to autostart
    jp.log("set autostart $(jp.name)")
    # #example start osis
    cmd = 'python'
    args = 'osisServerStart.py'
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'osis')
    startstoptimeout=20
    j.tools.startupmanager.addProcess("osis", cmd, args=args, priority=15, workingdir=workingdir,jpackage=jp,\
        check=True,timeoutcheck=startstoptimeout,stats=True,upstart=False)
    # j.tools.startupmanager.startJPackage(jp)
    
