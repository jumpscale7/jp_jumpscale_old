def main(j,args,params,tags,tasklet):
   
    #configure the package
    cfgpath = j.system.fs.joinPaths(j.dirs.cfgDir, 'startup')
    j.system.fs.createDir(cfgpath)
    config = """[circus]
check_delay = 5
"""
    j.system.fs.writeFile(j.system.fs.joinPaths(cfgpath, 'server.ini'), config)
    j.system.installtools.execute("circusd --daemon %s" % j.system.fs.joinPaths(cfgpath, 'server.ini'))
    
    j.system.platform.ubuntu.serviceInstall('circus', '/usr/local/bin/circusd', '--daemon %s' % j.system.fs.joinPaths(cfgpath, 'server.ini'))

    return params
    
def match(j,args,params,tags,tasklet):
    return True