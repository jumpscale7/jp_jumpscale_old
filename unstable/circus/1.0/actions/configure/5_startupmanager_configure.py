def main(j,args,params,tags,tasklet):
   
    #configure the package
    cfgpath = j.system.fs.joinPaths(j.dirs.cfgDir, 'startup')
    j.system.fs.createDir(cfgpath)

    cfg = j.system.fs.joinPaths(cfgpath, 'server.ini')

    ini = j.tools.inifile.open(cfg)
    ini.addSection('circus')
    ini.addParam('circus', 'include', "*.more.config.ini")
    ini.addParam('circus','check_delay',5)
    ini.addParam('circus','httpd','True')
    ini.addParam('circus','httpd_host','localhost')
    ini.addParam('circus','httpd_port',8080)
    ini.addParam('circus','statsd','True')
    ini.addParam('circus','check_delay',5)
    
    j.system.platform.ubuntu.serviceInstall('circus', '/usr/local/bin/circusd', '--daemon %s' % j.system.fs.joinPaths(cfgpath, 'server.ini'))

    # j.system.installtools.execute("circusd --daemon %s" % j.system.fs.joinPaths(cfgpath, 'server.ini'))    
    j.system.platform.ubuntu.serviceUninstall('circus')
    for port in [5555,5556,5557,8080]:
        j.system.process.killProcessByPort(port)
    
    cmd="python /usr/local/lib/python2.7/site-packages/circus/circusd.py --log-level info /opt/jumpscale/cfg/startup/server.ini "
    # cmd='/usr/local/bin/circusd'
    # args='%s' % j.system.fs.joinPaths(cfgpath, 'server.ini')
    j.system.platform.ubuntu.serviceInstall('circus', cmd, "")
    j.system.platform.ubuntu.startService('circus')

    return params
    
def match(j,args,params,tags,tasklet):
    return True