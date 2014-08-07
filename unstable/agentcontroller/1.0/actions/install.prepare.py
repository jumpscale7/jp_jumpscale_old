def main(j,jp):
    redis=j.packages.findNewest("jumpscale","redis")
    instancename = 'agentcontrolller'
    if not redis.isInstalled(instancename):
        redis.install(hrddata={"redis.name":instancename,"redis.port":"7769","redis.disk":"1","redis.mem":500},instance=instancename)
    redis.start()

    redis=j.packages.findNewest("jumpscale","redis")
    instancename = 'webdis'
    if not redis.isInstalled(instancename):
        redis.install(hrddata={"redis.name":instancename,"redis.port":"7770","redis.disk":"1","redis.mem":300},instance=instancename)
    redis.start()
