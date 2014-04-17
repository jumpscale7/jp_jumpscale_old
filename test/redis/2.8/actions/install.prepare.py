def main(j,jp):
   
    #prepare the platform before copying the files


    j.system.platform.ubuntu.install("python-redis")
    j.system.platform.ubuntu.checkInstall("redis-server", "redis-server")

    cmd="killall redis-server"
    j.system.process.execute(cmd,dieOnNonZeroExitCode=False)

