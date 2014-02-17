def main(j,jp):
    #configure the application to autostart
    # jp.log("set autostart $(jp.name)")

    #e.g. default:2,hypervisor:1,io:1
    for q in "$(workers.queues)".split(","):
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
                workingdir=workingdir,jpackage=jp,domain="jumpscale",ports=[])
