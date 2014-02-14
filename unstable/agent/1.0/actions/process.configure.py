def main(j,jp):
    #configure the application to autostart
    # jp.log("set autostart $(jp.name)")

    cmd = 'python'
    args = 'agent.py'
    # name="agent_%s"%i
    name="agent"
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'agent')
    j.tools.startupmanager.addProcess(name, cmd, args=args, env={}, numprocesses=1, priority=39, shell=False, workingdir=workingdir,jpackage=jp,domain="",ports=[])


