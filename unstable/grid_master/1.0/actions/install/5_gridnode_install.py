def main(j,args,params,tags,tasklet):
    
    params.result=True #return True if result ok

    j.system.platform.ubuntu.install('avahi-daemon')

    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
