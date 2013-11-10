def main(j,args,params,tags,tasklet):
   
    #configure the package 
    e="apt-get autoclean"
    j.system.installtools.execute(e)
    e="rm /var/cache/apt/archives/*.deb"
    j.system.installtools.execute(e)
    
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True