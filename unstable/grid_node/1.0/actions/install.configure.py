
def main(j,jp):
    gridid=j.application.config.getInt("grid.id")

    master_exists=False
    masterip=""
    if j.application.config.getBool("grid.useavahi"):
        import JumpScale.baselib.remote.avahi
        s=j.remote.avahi.getServices()
        master_exists,services=s.exists(partofname="js_grid_%s"%gridid)


        if master_exists==False:
            raise RuntimeError("Could not find master. Is avahi installed on your master node in your network. Grid id='%s'\nCheck with 'avahi-browse -a'. \nThere should be something like 'despiegk-desktop                    _js_grid_1._tcp      local'"%gridid)

        if master_exists:
            for service in services:
                if j.system.net.tcpPortConnectionTest(service.address, 5544):
                    masterip=service.address

    if masterip=="":
        
        raise RuntimeError("Could not find ip addr of master, is master osis running? We did connection test on port 5544, but failed")

    print "found master ip from avahi"

    #remember master ip for further usage
    j.application.config.set("grid.master.ip",masterip)

    #now register node
    import JumpScale.grid.osis
    print "make connection to master osis"
    client = j.core.osis.getClient(masterip)
    print "client ok"
    client_node=j.core.osis.getClientForCategory(client,"system","node")
    print "client for client 'node' ok"
    client_grid=j.core.osis.getClientForCategory(client,"system","grid")
    print "client for client 'grid' ok"
    print "connection done, osis ok."

    obj = client_node.new()
    obj.initFromLocalNodeInfo()
    key, new, changed = client_node.set(obj)
    print "save to osis"

    obj=client_node.get(key)

    j.application.config.set("grid.node.id",obj.id)
    j.application.config.set("grid.node.machineguid",obj.machineguid)

    print "save to local hrd"
    print "initialization of node done"


    print "initialize disks"
    import JumpScale.lib.diskmanager

    j.system.platform.diskmanager.partitionsFind(initialize=True,forceinitialize=False)