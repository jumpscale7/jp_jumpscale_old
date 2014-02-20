def main(j,jp):
    #configure the application to autostart
    # jp.log("set autostart $(jp.name)")

    cmd = 'python'
    args = 'controller.py'
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'agentcontroller')
    name="agentcontroller"
    j.tools.startupmanager.addProcess(name, cmd, args=args, env={}, numprocesses=1, priority=20, shell=False, workingdir=workingdir,jpackage=jp,domain="",ports=[4444])

    import JumpScale.baselib.redis
    j.clients.redis.deleteInstance("redisac")
    j.clients.redis.configureInstance("redisac",7769,100,True)

