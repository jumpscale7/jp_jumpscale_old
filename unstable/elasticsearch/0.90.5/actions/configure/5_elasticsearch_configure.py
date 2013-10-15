def main(j,args,params,tags,tasklet):
    import JumpScale.baselib.circus
    #make sure there are no traces of elastic search any more
    j.system.process.killProcessByPort(9200)
    cmd="/usr/share/elasticsearch/bin/elasticsearch"
    args="-fD es.config=/etc/elasticsearch/elasticsearch.yml"

    j.tools.circus.manager.addProcess(name="elasticsearch", cmd=cmd, args=args, warmup_delay=0, numprocesses=1)
    j.tools.circus.manager.apply()
    j.tools.circus.manager.startProcess('elasticsearch')

    return params
    
def match(j,args,params,tags,tasklet):
    return True
