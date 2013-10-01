def main(j,args,params,tags,tasklet):
    args.qp.copyFileParts('apps/portalbase', '/opt/jumpscale/apps/portalbase') #  will copy files to sandbox
    args.qp.copyFileParts('apps/portalftpgateway', '/opt/jumpscale/apps/portalftpgateway') #  will copy files to sandbox
   
    cwd = args.qp.getPathFilesPlatform('generic')
    j.system.process.run("pip install .", cwd=cwd)
    
    params.result=True #return True if result ok
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
