def main(j,args,params,tags,tasklet):
    args.qp.copyFiles() #  will copy files to sandbox
    
    params.result=True #return True if result ok
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
