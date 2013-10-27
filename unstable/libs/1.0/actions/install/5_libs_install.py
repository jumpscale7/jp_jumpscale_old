def main(j,args,params,tags,tasklet):
   
    #install the required files onto the system

    args.jp.copyFiles(subdir="",destination="/",applyhrd=False)


    initpath=j.system.fs.joinPaths(j.application.config.get("python.paths.local.sitepackages"),"JumpScale","lib","__init__.py")
    j.system.fs.writeFile(initpath,"")
    
    params.result=True #return True if result ok
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
