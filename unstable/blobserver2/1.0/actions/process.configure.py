def main(j,jp):
   
    #configure the application to autostart
    
    # jp.log("set autostart $(jp.name)")

    # #example start osis
    cmd = 'python'
    args = 'blobserver2.py'
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'blobserver2')
    name = jp.name
    domain = jp.domain
    j.tools.startupmanager.addProcess(name=name, cmd=cmd, args=args, env={}, numprocesses=1, priority=1, \
       shell=False, workingdir=workingdir,jpackage=jp,domain=domain,ports=[2345])
    
    #can configure more apps to start than just 1 linked to the jpackage

    pass
