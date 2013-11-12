from JumpScale import j
def main(jp):
   
    # pypackages = ['circus','circus-web','chaussette']
    pypackages = ['tomako','tornadio2']

    cmd="stop circus"
    j.system.process.executeAsync(cmd)

    #kill remainders
    for tcpport in [5555,5556,5557,9099]:
        j.system.process.killProcessByPort(tcpport)

    toremove = ['circus','circus-web','chaussette'] 
    j.system.platform.python.remove(toremove)

    for pp in pypackages:
        # do.execute("pip uninstall %s" % pp)
        j.system.platform.python.install(pp)
