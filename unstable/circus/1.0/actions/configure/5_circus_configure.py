def main(j,args,params,tags,tasklet):

    cfgpath = j.system.fs.joinPaths(j.dirs.cfgDir, 'startup')
    j.system.fs.createDir(cfgpath)

    cfg = j.system.fs.joinPaths(cfgpath, 'server.ini')

    ini = j.tools.inifile.open(cfg)
    ini.addSection('circus')
    ini.addParam('circus', 'include', "*.ini")
    ini.addParam('circus','check_delay', 5)
    ini.addParam('circus','httpd','True')
    ini.addParam('circus','httpd_host','localhost')
    ini.addParam('circus','httpd_port',8080)
    ini.addParam('circus','statsd','True')

    
    j.system.platform.ubuntu.serviceInstall('circus', '/usr/local/bin/circusd', '--daemon %s' % j.system.fs.joinPaths(cfgpath, 'server.ini'))
    j.system.platform.ubuntu.serviceUninstall('circus')
    for port in [5555,5556,5557,8080]:
        j.system.process.killProcessByPort(port)
    
    cmd="python /usr/local/lib/python2.7/site-packages/circus/circusd.py --log-output /var/log/circus.log --log-level info /opt/jumpscale/cfg/startup/server.ini "
    j.system.platform.ubuntu.serviceInstall('circus', cmd, "")

    try:
        j.system.platform.ubuntu.startService('circus')
    except:
        cmd='sh /etc/init/circus.conf 2>&1 > /dev/null &'
        try:
            j.system.process.execute(cmd)
        except:
            pass

    return params
    
def match(j,args,params,tags,tasklet):
    return True