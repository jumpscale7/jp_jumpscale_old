def main(j,args,params,tags,tasklet):
   
    #configure the package 

    gridid=j.application.config.getInt("gridmaster.grid.id")


    #check osis installed
    if not j.system.net.tcpPortConnectionTest("127.0.0.1", 5544):
        raise RuntimeError("Cannot find local osis running, needs to run on port 5544")

    #register in osis
    import JumpScale.grid.osis
    client = j.core.osis.getClient()
    client.createNamespace(name="system",template="coreobjects",incrementName=False)
    client_grid=j.core.osis.getClientForCategory(client,"system","grid")

    gridobj = client_grid.new(name="grid_%s"%gridid,id=gridid)
    gridobj.initFromLocalNodeInfo()
    key, new, changed = client_grid.set(gridobj)

    #configure avahi
    import JumpScale.lib.remote.avahi
    j.remote.avahi.registerService("js_grid_%s"%gridid,5544)

    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
