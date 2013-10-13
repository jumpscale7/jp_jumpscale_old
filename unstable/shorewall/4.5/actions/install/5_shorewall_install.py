def main(j,args,params,tags,tasklet):
   
    #install the required files onto the system

    # can happen by e.g. installing a debian package e.g. by
    j.system.platform.ubuntu.install("shorewall")
       

    #configuration is not done in this step !!!!!
    
    params.result=True #return True if result ok
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
