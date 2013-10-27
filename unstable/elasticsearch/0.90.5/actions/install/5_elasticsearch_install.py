def main(j,args,params,tags,tasklet):
    args.jp.installUbuntuDebs()
    j.system.platform.ubuntu.install("openjdk-7-jre")
    j.system.platform.python.install('pyelasticsearch')
    args.jp.copyFiles(subdir="root",destination="/",applyhrd=True)

    params.result=True #return True if result ok
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
