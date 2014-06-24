
def main(j,jp):
    j.system.process.killProcessByPort(9200)

    name="elasticsearch"
    bindir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'elasticsearch','bin')
    cmd="%s/elasticsearch"% bindir
    cfgdir = j.system.fs.joinPaths(j.dirs.cfgDir, 'elasticsearch')
    ymlfile = j.system.fs.joinPaths(cfgdir, 'elasticsearch.yml')
    args="-fD es.config=%s" % ymlfile
    startstoptimeout=60
    env = {"JAVA_HOME": "$base/apps/openjdk7/"}
    processfilterstr="elasticsearch.yml org.elasticsearch.bootstrap.ElasticSearch"
    j.tools.startupmanager.addProcess(name, cmd, args=args, env=env, domain="jumpscale",jpackage=jp,ports=[9200],priority=1,\
        workingdir=cfgdir,check=True,timeoutcheck=startstoptimeout,isJSapp=0,processfilterstr=processfilterstr,stats=True,upstart=False)
    # j.tools.startupmanager.startJPackage(jp)
