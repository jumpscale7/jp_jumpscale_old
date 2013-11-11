def main(j,args,params,tags,tasklet):
    import JumpScale.baselib.circus
    #make sure there are no traces of elastic search any more
    j.system.process.killProcessByPort(9200)
    cmd="/opt/elasticsearch/bin/elasticsearch"
    args="-fD es.config=/etc/elasticsearch/elasticsearch.yml"

    j.tools.startupmanager.addProcess(name="elasticsearch", cmd=cmd, args=args, priority=1)
    j.tools.startupmanager.apply()

    return params
    
def match(j,args,params,tags,tasklet):
    return True
