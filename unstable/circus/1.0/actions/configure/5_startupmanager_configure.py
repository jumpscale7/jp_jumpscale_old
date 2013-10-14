def main(j,args,params,tags,tasklet):
   
    #configure the package
    cfgpath = j.system.fs.joinPaths(j.dirs.cfgDir, 'startup')
    j.system.fs.createDir(cfgpath)
    config = """[circus]
check_delay = 5
httpd = True
httpd_host = localhost
httpd_port = 8080
statsd = True
include = *.more.config.ini
"""
    j.system.fs.writeFile(j.system.fs.joinPaths(cfgpath, 'server.ini'), config)
    
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