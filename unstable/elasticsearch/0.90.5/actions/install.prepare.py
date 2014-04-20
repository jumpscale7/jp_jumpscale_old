
def main(j,jp):

    cmd='dpkg -r elasticsearch'
    j.system.installtools.execute(cmd,dieOnNonZeroExitCode=False,ignoreErrorOutput=True, useShell=True)

    cmd='dpkg -P elasticsearch'
    j.system.installtools.execute(cmd,dieOnNonZeroExitCode=False,ignoreErrorOutput=True, useShell=True)

    j.system.process.killProcessByPort(9200)

    j.system.fs.createDir("/opt/data/elasticsearch/data")
    j.system.fs.createDir("/opt/data/elasticsearch/tmp")
    j.system.fs.createDir("/opt/data/elasticsearch/logs")
