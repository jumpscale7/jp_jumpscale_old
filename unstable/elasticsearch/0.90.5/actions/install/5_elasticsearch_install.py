def main(j,args,params,tags,tasklet):

    do=j.system.installtools
    # do.execute("circusctl stop elasticsearch")
   
    args.qp.installUbuntuDebs()

    j.system.platform.ubuntu.install("openjdk-7-jre")

    j.system.platform.python.install('pyelasticsearch')

    args.qp.copyFiles(subdir="root",destination="/",applyhrd=True)

    # do.execute("circusctl reload")
    # do.execute("circusctl start elasticsearch")

    params.result=True #return True if result ok
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
