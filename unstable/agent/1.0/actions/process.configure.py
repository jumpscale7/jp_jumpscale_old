def main(j,jp):
    #configure the application to autostart
    # jp.log("set autostart $(jp.name)")

    # for i in range(j.basetype.integer.fromString('$(agent.nrinstances)')):
    cmd = 'python'
    args = 'agent.py'
    # name="agent_%s"%i
    name="agent"
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'agent')
    j.tools.startupmanager.addProcess(name, cmd, args=args, env={}, numprocesses=1, priority=39, shell=False, workingdir=workingdir,jpackage=jp,domain="",ports=[])


    #e.g. default:2,hypervisor:1,io:1
    for q in "$(agent.queues)".split(","):
        print "Queue:%s"%q
        splitted=q.split(":")
        if len(splitted)<>2:
            raise RuntimeError("format needs to be: default:2,hypervisor:1,io:1")
        qname,nrinstances=splitted

        for nr in range(int(nrinstances)):
            cmd = 'python'
            wname="worker_%s_%s"%(qname,nr)
            if "$(agent.redis.auth)".strip()<>"":
                args = 'worker.py -pw $(agent.redis.auth) -a $(agent.redis.addr) -p $(agent.redis.port) -qn %s -wn %s'%(qname,wname)
            else:
                args = 'worker.py -a $(agent.redis.addr) -p $(agent.redis.port) -qn %s -wn %s'%(qname,wname)
            workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'agent')
            j.tools.startupmanager.addProcess(wname, cmd, args=args, env={}, numprocesses=1, priority=21, shell=False, \
                workingdir=workingdir,jpackage=jp,domain="workers",ports=[])
