def main(j,args,params,tags,tasklet):
    j.system.platform.ubuntu.install("openjdk-7-jre")
    j.system.platform.python.install('pyelasticsearch')

    cmd='dpkg -r elasticsearch'
    j.system.installtools.execute(cmd,dieOnNonZeroExitCode=False,ignoreErrorOutput=True, useShell=True)

    cmd='dpkg -P elasticsearch'
    j.system.installtools.execute(cmd,dieOnNonZeroExitCode=False,ignoreErrorOutput=True, useShell=True)

    j.system.process.killProcessByPort(9200)

    args.jp.copyFiles(subdir="rootconfig",destination="/",applyhrd=True)

    args.jp.copyFiles(subdir="root",destination="/",applyhrd=False)

    params.result=True #return True if result ok
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
