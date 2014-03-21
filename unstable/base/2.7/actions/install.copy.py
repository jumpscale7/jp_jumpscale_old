def main(j,jp):
    import sys

    j.logger.consoleloglevel = 6
    # debpackages = ('libleveldb1', 'ipython', 'python-gevent', 'python-simplejson', 'python-numpy', \
    #     'python-apt', 'python-pip', 'python-requests', "byobu", "tmux",\
    #     "python-paramiko", "python-mhash", "python-snappy", "python-m2crypto", "python-iowait", "python-psutil","python-ipdb","python-regex","python-netaddr")

    debpackages = ('libleveldb1', "byobu", "tmux")


    for name in debpackages:
        print "install %s" % name
        j.system.platform.ubuntu.install(name)

    # remove packages which will be installed of this jpackage, they should not be on the system
    toremove = ["blosc", "msgpack", "zmq", "pylzma", "ujson", "urllib3"]  # DO NOT REMOVE ipython

    #"cauchyec","galoisbuffer"
    j.system.platform.python.remove(toremove)

    ## is done as part of jpackage files
    # distpath = "$(python.paths.local.distpackages)/jumpscale.pth"
    # if not j.system.fs.exists(distpath):
    #     j.system.fs.writeFile(distpath, "$(python.paths.local.sitepackages)\n")
    #     # make sure currnt process can access site-oackage
    #     sys.path.append("$(python.paths.local.sitepackages)")

    #copying of files is done in this step
    jp._copyfiles()