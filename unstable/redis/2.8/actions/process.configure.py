def main(j,jp):
   
    #configure the application to autostart
    
    # jp.log("set autostart $(jp.name)")

    cmd = 'redis-server'
    args = ' /etc/redis/redis_cache.conf'
    workingdir = "/"
    name = "redisc"
    domain = jp.domain
    ports = [7767]
    j.tools.startupmanager.addProcess(name=name, cmd=cmd, args=args, env={}, numprocesses=1, priority=1, \
       shell=False, workingdir=workingdir,jpackage=jp,domain=domain,ports=ports)
    
    cmd = 'redis-server'
    args = ' /etc/redis/redis_prod.conf'
    workingdir = "/"
    name = "redisp"
    domain = jp.domain
    ports = [7768]
    j.tools.startupmanager.addProcess(name=name, cmd=cmd, args=args, env={}, numprocesses=1, priority=1, \
       shell=False, workingdir=workingdir,jpackage=jp,domain=domain,ports=ports)
