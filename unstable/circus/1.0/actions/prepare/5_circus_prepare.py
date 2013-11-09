def main(j,args,params,tags,tasklet):
   
    # pypackages = ['circus','circus-web','chaussette']
    pypackages = ['tomako','tornadio2']

    do=j.system.installtools

    cmd="stop circus"
    j.system.process.executeAsync(cmd)
    
    #kill remainders
    for tcpport in [5555,5556,5557,9099]:
        j.system.process.killProcessByPort(tcpport)

    toremove = ['circus','circus-web','chaussette'] 
    j.system.platform.python.remove(toremove)

    for pp in pypackages:
        # do.execute("pip uninstall %s" % pp)
        do.execute("pip install %s" % pp)

    params.result=True #return True if result ok
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
