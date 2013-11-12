def main(jp):
   
    #configure the application to autostart
    jp.log("set autostart $(jp.name)")

    # #example start osis
    cmd = 'python'
    args = 'osisServerStart.py'
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'osis')

    j.tools.startupmanager.addProcess("osis", cmd, args=args, env={}, numprocesses=1, priority=2, shell=False, workingdir=workingdir,jpackage=jp,domain="",ports=[5544])
    
