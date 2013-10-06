def main(j,args,params,tags,tasklet):
   
    #configure the package 

    #make sure there are no traces of elastic search any more
    j.system.process.killProcessByPort(9200)
    j.system.process.killProcessByName("elasticsearch")

    j.system.fs.remove("/etc/init.d/elasticsearch")

    import JumpScale.baselib.circus

    cmd="/usr/share/elasticsearch/bin/elasticsearch"
    args="-fD es.config=/etc/elasticsearch/elasticsearch.yml"

    j.tools.circus.manager.addProcess(name="elasticsearch",cmd=cmd,args=args,warmup_delay=0,numprocesses=1)

    j.tools.circus.manager.apply()

    
    
    from IPython import embed
    print "DEBUG NOW id"
    embed()    

    return params
    
    
def match(j,args,params,tags,tasklet):
    return True