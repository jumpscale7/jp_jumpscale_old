def main(j,args,params,tags,tasklet):
   
    #configure the package 

    gridid=j.application.config.getInt("gridmaster.grid.id")

    master_exists=False
    if j.application.config.getBool("gridmaster.useavahi"):
        import JumpScale.lib.remote.avahi
        s=j.remote.avahi.getServices()
        master_exists,services=s.exists(partofname="jsgrid.%s.master"%gridid)
        if master_exists:
            from IPython import embed
            print "DEBUG NOW master exist"
            embed()
            
            masterip=1
        master_exists=True    

    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
