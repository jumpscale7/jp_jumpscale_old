def main(j,args,params,tags,tasklet):
   
    toremove = ['circus-web'] 
    j.system.platform.python.remove(toremove)

    
    params.result=True #return True if result ok
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
