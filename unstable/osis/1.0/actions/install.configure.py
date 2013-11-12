from JumpScale import j
def main(jp):
<<<<<<< local
=======
    import JumpScale.baselib.startupmanager
    cmd = 'python'
    args2 = 'osisServerStart.py'
>>>>>>> other

<<<<<<< local
    pass=======
    jp.log("set autostart")
    
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'osis')

    j.tools.startupmanager.addProcess('osis', cmd, args2, priority=2, workingdir=workingdir,jpackage=jp)
>>>>>>> other
