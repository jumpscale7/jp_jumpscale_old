def main(j,args,params,tags,tasklet):
   
    #configure the package

    gridid=j.application.config.getInt("grid.id")

    master_exists=False
    masterip=""
    if j.application.config.getBool("grid.useavahi"):
        import JumpScale.lib.remote.avahi
        s=j.remote.avahi.getServices()
        master_exists,services=s.exists(partofname="js_grid_%s"%gridid)
        if master_exists:
            for service in services:                
                if j.system.net.tcpPortConnectionTest(service.address, 5544):
                    masterip=service.address

    if masterip=="":
        raise RuntimeError("Could not find ip addr of master")
            
    
    #remember master ip for further usage
    j.application.config.set("grid.master.ip",masterip)

    #now register node
    import JumpScale.grid.osis
    client = j.core.osis.getClient(masterip)
    client_node=j.core.osis.getClientForCategory(client,"system","node")
    client_grid=j.core.osis.getClientForCategory(client,"system","grid")

    obj = client_node.new()
    obj.initFromLocalNodeInfo()
    key, new, changed = client_node.set(obj)

    obj=client_node.get(key)

    j.application.config.set("grid.node.id",obj.id)
    j.application.config.set("grid.node.machineguid",obj.machineguid)

    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
