def main(j,jp):
    jp.log("set autostart $(jp.name)")
    cmd = 'python'
    args = 'loggerStart.py'
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'logger')
    j.tools.startupmanager.addProcess('logger', cmd, args=args, env={}, workingdir=workingdir,jpackage=jp,priority=30)
