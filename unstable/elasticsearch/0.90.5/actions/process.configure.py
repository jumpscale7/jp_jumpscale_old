
def main(j,jp):
    j.system.process.killProcessByPort(9200)

    name="elasticsearch"
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'elasticsearch','bin')
    cmd="%s/elasticsearch"%workingdir
    ymlfile = j.system.fs.joinPaths(j.dirs.baseDir, 'etc', 'elasticsearch', 'elasticsearch.yml')
    args="-fD es.config=%s" % ymlfile
    startstoptimeout=60
    j.tools.startupmanager.addProcess(name, cmd, args=args, domain="jumpscale",jpackage=jp,ports=[9200],priority=1,\
        check=True,timeoutcheck=startstoptimeout,isJSapp=0)
    # j.tools.startupmanager.startJPackage(jp)
