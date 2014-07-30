def main(j,jp):
   
    names=["redism","redisp","redisc"]

    if j.application.config.getBool("redis.ac.enable"):
        names.append("redisac")
        names.append("redisw")

    for name in names:
        dpath = "$vardir/redis/%s" % name
        cpath = j.system.fs.joinPaths(dpath, "redis.conf")
        port=j.application.config.getInt("redis.port.%s"%name)
        pd=j.tools.startupmanager.addProcess(\
            name=name,\
            cmd="./redis-server", \
            args=cpath,\
            env={},\
            numprocesses=1,\
            priority=1,\
            shell=False,\
            workingdir='$base/apps/redis/',\
            jpackage=jp,\
            domain="redis",\
            ports=[port],\
            autostart=True,\
            reload_signal=0,\
            user="root",\
            log=True,\
            stopcmd=None,\
            check=True,\
            timeoutcheck=2,\
            isJSapp=0,\
            upstart=True,\
            stats=True,\
            processfilterstr="redis/%s/redis.conf"%(name))#what to look for when doing ps ax to find the process
        
        pd.start()

        # self.startInstance(name)
