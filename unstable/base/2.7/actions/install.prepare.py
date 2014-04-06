def main(j,jp):
    j.logger.consoleloglevel = 6
    j.system.fs.createDir("/usr/local/lib/python2.7/dist-packages/")
    j.system.fs.createDir("/usr/local/lib/python2.7/site-packages/")

    debpackages = ('libleveldb1', # required by leveldb
                   "byobu",
                   "tmux",
                   'liblapack3', # required by numpy
                   'libmhash2') # required by mhash #@todo copy to sandbox


    for name in debpackages:
        print "install %s" % name
        j.system.platform.ubuntu.install(name)

    # remove packages which will be installed of this jpackage, they should not be on the system
    toremove = ["blosc", "msgpack", "zmq", "pylzma", "ujson", "urllib3"]  # DO NOT REMOVE ipython

    j.system.platform.python.remove(toremove)

