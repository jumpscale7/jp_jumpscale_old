
def main(j,jp):
    j.system.fs.remove("/opt/jumpscale/cfg/hrd/python.hrd")
    j.system.fs.createDir("/usr/local/lib/python2.7/dist-packages/")
    j.system.fs.createDir("/usr/local/lib/python2.7/site-packages/")