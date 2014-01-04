
def main(j,jp):
    
    try:
        j.tools.startupmanager.stopProcess("jumpscale","elasticsearch")
    except Exception,e:
        pass


    cmd='dpkg -r elasticsearch'
    j.system.installtools.execute(cmd,dieOnNonZeroExitCode=False,ignoreErrorOutput=True, useShell=True,outputToStdout=False)

    cmd='dpkg -P elasticsearch'
    j.system.installtools.execute(cmd,dieOnNonZeroExitCode=False,ignoreErrorOutput=True, useShell=True,outputToStdout=False)

    j.system.process.killProcessByPort(9200)

    j.system.fs.createDir("/opt/data/elasticsearch/data")
    j.system.fs.createDir("/opt/data/elasticsearch/tmp")
    j.system.fs.createDir("/opt/data/elasticsearch/logs")

    j.system.platform.python.install('pyelasticsearch')