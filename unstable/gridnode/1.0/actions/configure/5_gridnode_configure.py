def main(j,args,params,tags,tasklet):
   
    #configure the package 

    master_exists=False
    if j.application.config.getBool("grid.useavahi"):
        import JumpScale.lib.remote.avahi
        s=j.remote.avahi.getServices():
        master_exists,services=s.exists(partofname="jsgrid.1.master")
        if master_exists:
            from IPython import embed
            print "DEBUG NOW master exist"
            embed()
            
            masterip=1
        master_exists=True

    if master_exists==False:
        if j.application.config.get("grid.ismaster")=="":
            ismaster=j.console.askYesNo("Is this node the master of the grid?")
            if ismaster:
                if j.console.askYesNo("Do you want to enable this node to become the master of the grid?"):
                    
            from IPython import embed
            print "DEBUG NOW question master grid"
            embed()
            
        else:
            




        

    from IPython import embed
    print "DEBUG NOW configuregridnode"
    embed()
    

    return params
    
    
def match(j,args,params,tags,tasklet):
    return True