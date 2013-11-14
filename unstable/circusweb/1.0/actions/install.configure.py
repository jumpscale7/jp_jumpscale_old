
def main(j,jp):
   
    #configure the package
    cfgpath = j.system.fs.joinPaths(j.dirs.cfgDir, 'startup')
    cfg = j.system.fs.joinPaths(cfgpath, 'server.ini')

    ini = j.tools.inifile.open(cfg)
    ini.addParam('circus','httpd','True')
    ini.addParam('circus','httpd_host','localhost')
    ini.addParam('circus','httpd_port',8080)

    j.tools.startupmanager.apply()
