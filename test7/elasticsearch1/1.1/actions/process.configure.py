
def main(j,jp):
    j.system.process.killProcessByPort(9200)

    name="elasticsearch"
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'elasticsearch1','bin')
    cmd="%s/elasticsearch"%workingdir
    ymlfile = j.system.fs.joinPaths(j.dirs.cfgDir, 'elasticsearch1', 'elasticsearch.yml')
    args="-fD es.config=%s" % ymlfile
    startstoptimeout=60
    processfilterstr="elasticsearch.yml org.elasticsearch.bootstrap.ElasticSearch"
    j.tools.startupmanager.addProcess(name, cmd, args=args, domain="jumpscale",jpackage=jp,ports=[9200],priority=1,\
        check=True,timeoutcheck=startstoptimeout,isJSapp=0,processfilterstr=processfilterstr,stats=True,upstart=False)
    # j.tools.startupmanager.startJPackage(jp)
