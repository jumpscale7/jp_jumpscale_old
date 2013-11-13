from JumpScale import j

def main(jp):
    #configure the application to autostart
    jp.log("set autostart $(jp.name)")
    # #example start osis
    cmd = 'python'
    args = 'osisServerStart.py'
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'osis')

    j.tools.startupmanager.addProcess("osis", cmd, args=args, priority=2, workingdir=workingdir,jpackage=jp,ports=[5544])
    j.tools.startupmanager.startJPackage(jp)
    
