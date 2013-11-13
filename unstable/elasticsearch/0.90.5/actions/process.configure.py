from JumpScale import j
def main(jp):
    j.system.process.killProcessByPort(9200)

    name="elasticsearch"
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'elasticsearch','bin')
    cmd="%s/elasticsearch"%workingdir
    args="-fD es.config=/etc/elasticsearch/elasticsearch.yml"

    j.tools.startupmanager.addProcess(name, cmd, args=args, jpackage=jp,ports=[9200])
    j.tools.startupmanager.startJPackage(jp)
