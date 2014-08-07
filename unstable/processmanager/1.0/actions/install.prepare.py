def main(j,jp):
    redis=j.packages.findNewest("jumpscale","redis")
    instancename = 'production'
    if not redis.isInstalled(instancename):
        redis.install(hrddata={"redis.name":instancename,"redis.port":"7768","redis.disk":"1","redis.mem":400},instance=instancename)
    redis.start()
