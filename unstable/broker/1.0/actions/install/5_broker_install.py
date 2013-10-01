def main(j,args,params,tags,tasklet):
    args.qp.copyFiles('apps', '%s/apps' % j.dirs.baseDir) #  will copy files to sandbox
    
    params.result=True #return True if result ok
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
