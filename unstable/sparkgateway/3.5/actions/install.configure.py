def main(j,jp):
    cfgpath = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'SparkGateway', 'gateway.conf') 
    te = j.codetools.getTextFileEditor(cfgpath)
    te.appendReplaceLine('^\s*port\s*=', 'port = $(sparkgateway.port)')
    te.save()
