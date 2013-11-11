def main(j,args,params,tags,tasklet):
   
    #start the application (only relevant for server apps)
    #make sure you doublecheck that the app is really started (DO THIS CAREFULLY) e.g. check process & port if network daemon & eventually even a selftest in the app
    
    import JumpScale.baselib.circus
    
    j.tools.startupmanager.startProcess('elasticsearch')

    print "test if elasticsearch started by doing a port test"  #@todo why does it take so long?
    if j.system.net.waitConnectionTest("127.0.0.1",9200,60)==False:
        raise RuntimeError("Could not configure elasticsearch, elasticsearch did not start on port 9200.")    

    print "elasticsearch reachable"

    params.result=True #return True if result ok
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True