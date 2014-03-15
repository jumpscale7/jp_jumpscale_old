
def main(j,jp):
    j.system.process.killProcessByPort(9200)

    name="elasticsearch"
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'elasticsearch','bin')
    cmd="%s/elasticsearch"%workingdir
    args="-fD es.config=/etc/elasticsearch/elasticsearch.yml"
    startstoptimeout=60
    j.tools.startupmanager.addProcess(name, cmd, args=args, domain="jumpscale",jpackage=jp,ports=[9200],priority=1,\
        check=True,timeoutcheck=startstoptimeout)
    # j.tools.startupmanager.startJPackage(jp)
