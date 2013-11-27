def main(j,jp):
   
    jp.log("set autostart $(jp.name)")

    # #example start osis
    cmd = 'python'
    args = 'portal_start.py'
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'gridportal')
    j.tools.startupmanager.addProcess(jp.name, cmd, args=args, workingdir=workingdir,jpackage=jp,priority=50)
