def main(j,args,params,tags,tasklet):
   
    j.system.platform.ubuntu.install('php5-cgi')
    j.system.platform.ubuntu.install('php5-json')
    j.system.platform.ubuntu.install('python-imaging')
    j.system.platform.ubuntu.install('nginx-full')
    j.system.platform.ubuntu.install('python-beaker')
    j.system.platform.ubuntu.install('python-mimeparse')
    j.system.platform.ubuntu.install('redis-server')
    j.system.platform.ubuntu.install('python-redis')

    
    params.result=True #return True if result ok
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
