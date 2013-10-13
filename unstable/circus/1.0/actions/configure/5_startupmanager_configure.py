def main(j,args,params,tags,tasklet):
   
    #configure the package
    cfgpath = j.system.fs.joinPaths(j.dirs.cfgDir, 'startup')
    j.system.fs.createDir(cfgpath)
    cfg = j.system.fs.joinPaths(cfgpath, 'server.ini')
    ini = j.tools.inifile.open(cfg)
    ini.addSection('circus')
    ini.addParam('circus', 'include_dir', cfgpath)
    j.system.platform.ubuntu.serviceInstall('circus', '/usr/local/bin/circusd', '--daemon %s' % j.system.fs.joinPaths(cfgpath, 'server.ini'))
    j.system.platform.ubuntu.startService('circus')
    import JumpScale.baselib.circus
    j.tools.circus.manager.apply()

    return params
    
def match(j,args,params,tags,tasklet):
    return True
