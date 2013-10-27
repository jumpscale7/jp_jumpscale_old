def main(j,args,params,tags,tasklet):
   
    # pypackages = ['circus','circus-web','chaussette']
    # pypackages = ['tomako','tornadio2']
    pypackages=[]

    do=j.system.installtools

    toremove = ['tornado','tornadio2','tomako'] 
    j.system.platform.python.remove(toremove)

    for pp in pypackages:
        # do.execute("pip uninstall %s" % pp)
        do.execute("pip install %s" % pp)

    args.jp.copyPythonLibs()

    params.result=True #return True if result ok
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
