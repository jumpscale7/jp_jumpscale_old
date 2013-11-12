def main(jp):
   
    #configure the application to autostart
    
    # jp.log("set autostart $(jp.name)")

    # #example start elasticsearch
    j.system.process.killProcessByPort(9200)

    name="elasticsearch"
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'elasticsearch','bin')
    cmd="%s/elasticsearch"%workingdir
    args="-fD es.config=/etc/elasticsearch/elasticsearch.yml"

    
    j.tools.startupmanager.addProcess(name, cmd, args=args, env={}, numprocesses=1, priority=1, shell=False, workingdir="",jpackage=jp,domain="",ports=[9200])
    


    pass
