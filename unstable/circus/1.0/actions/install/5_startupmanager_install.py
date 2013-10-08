def main(j,args,params,tags,tasklet):
   
    pypackages = ['circus','circus-web','chaussette']
    
    #kill remainders
    for tcpport in [5555,5556,5557]:
    	j.system.process.killProcessByPort(tcpport)

    do=j.system.installtools

    for pp in pypackages:
        # do.execute("pip uninstall %s" % pp)
        do.execute("pip install %s" % pp)


    params.result=True #return True if result ok
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
