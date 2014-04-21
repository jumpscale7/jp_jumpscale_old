def main(j,jp):
   
    try:
        j.system.platform.ubuntu.stopService("nginx")
    except:
        pass

    cmd="killall nginx"
    try:
        j.system.process.execute(cmd)
    except:
        pass

    j.system.platform.ubuntu.remove("nginx")
    j.system.platform.ubuntu.remove("lua-nginx-memcached")
    j.system.platform.ubuntu.remove("lua-nginx-redis")
    j.system.platform.ubuntu.remove("nginx-common")
    j.system.platform.ubuntu.remove("nginx-extras")


