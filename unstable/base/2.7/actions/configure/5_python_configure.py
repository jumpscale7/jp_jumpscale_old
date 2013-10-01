def main(j,args,params,tags,tasklet):
   
    #configure the package 

    j.application.config.set("jumpscale.paths.base",j.dirs.baseDir)

    return params
    
    
def match(j,args,params,tags,tasklet):
    return True