def main(j,args,params,tags,tasklet):
   
    #install the required files onto the system

    args.qp.copyFiles(subdir="",destination="/",applyhrd=False) 
    
    params.result=True #return True if result ok
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
