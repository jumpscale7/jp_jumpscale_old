def main(j,args,params,tags,tasklet):
    args.qp.copyFiles('apps/portalbase', j.system.fs.joinPaths(j.dirs.baseDir, 'apps/portalbase'))
    args.qp.copyFiles('apps/portalftpgateway', j.system.fs.joinPaths(j.dirs.baseDir,'apps/portalftpgateway'))
   
    cwd = args.qp.getPathFilesPlatform('generic')
    j.system.process.run("pip install .", cwd=cwd)
    
    params.result=True #return True if result ok
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
