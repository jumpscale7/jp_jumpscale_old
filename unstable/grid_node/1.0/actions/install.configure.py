
def main(j,jp):
    gridid=j.application.config.getInt("grid.id")

    master_exists=False
    masterip=""
    if j.application.config.getBool("grid.useavahi"):
        if gridid==0:
            gridid = j.console.askInteger("Please provide grid id. Grid id must be in range 1 - 32767", minValue=1, maxValue=32767, retry=5)
            j.application.config.set("grid.id", gridid)

        import JumpScale.baselib.remote.avahi
        s=j.remote.avahi.getServices()
        master_exists,services=s.exists(partofname="js_grid_%s."%gridid)

        if master_exists==False:
            raise RuntimeError("Could not find master. Is avahi installed on your master node in your network. Grid id='%s'\nCheck with 'avahi-browse -a'. \nThere should be something like 'despiegk-desktop                    _js_grid_1._tcp      local'"%gridid)

        if master_exists:
            for service in services:
                if j.system.net.tcpPortConnectionTest(service.address, 5544):
                    masterip=service.address
    else:
        masterip =j.application.config.get("grid.master.ip")
        if masterip=="":
            masterip=j.console.askString("Please provide, ip address of grid master")

        j.packages.findNewest(domain="jumpscale",name="libs").install()

        if j.system.net.isIpLocal(masterip):
            j.packages.findNewest(domain="jumpscale",name="sentry").install()
            j.tools.startupmanager.startProcess("jumpscale","sentry")
            redis=j.packages.findNewest(domain="jumpscale",name="redis")
            redis.install()
            redis.start()
            j.packages.findNewest(domain="jumpscale",name="elasticsearch").install()
            j.tools.startupmanager.startProcess("jumpscale","elasticsearch")
            j.packages.findNewest(domain="jumpscale",name="grid").install()
            j.packages.findNewest(domain="jumpscale",name="portal").install()
            j.packages.findNewest(domain="jumpscale",name="osis").install()
            j.tools.startupmanager.startProcess("jumpscale","osis")            
            j.packages.findNewest(domain="jumpscale",name="osis").install()
            j.tools.startupmanager.startProcess("jumpscale","osis")
            # j.packages.findNewest(domain="jumpscale",name="workers").install()       
            j.packages.findNewest(domain="jumpscale",name="grid_master").install()
    
        if j.system.net.tcpPortConnectionTest(masterip, 5544)==False:
            raise RuntimeError("Cannot reach grid master on ip %s (using port test 5544 to see if there is an osis server)"%masterip)     

    if masterip=="":        
        raise RuntimeError("Could not find ip addr of master, is master osis running? We did connection test on port 5544, but failed")

    print "found master ip from avahi"

    #remember master ip for further usage
    j.application.config.set("grid.master.ip",masterip)

    #make sure superadminpasswd is known
    if j.application.config.get("grid.master.superadminpasswd") == "" and j.application.config.get("grid.master.superadminpasswd").lower() <> "none":
        passwdmd5 = j.tools.hash.md5_string(j.console.askString("Please provide: grid.master.superadminpasswd", regex="^(?!\s*$).+", retry=5))
        if not j.console.askYesNo("do you want to remember the superadmin passwd for the grid (only do this on trusted machines)"):
            j.application.config.set("grid.master.superadminpasswd", passwdmd5)
        else:
            j.application.config.set("grid.master.superadminpasswd", "None")

    #now register node
    import JumpScale.grid.osis
    print "make connection to master osis"
    client = j.core.osis.getClient(masterip, user='root',passwd=j.application.config.get("grid.master.superadminpasswd"))
    print "client ok"
    client_node=j.core.osis.getClientForCategory(client,"system","node")
    print "client for client 'node' ok"
    # client_grid=j.core.osis.getClientForCategory(client,"system","grid")
    # print "client for client 'grid' ok"
    print "connection done, osis ok."

    obj = client_node.new()

    if gridid:
        obj.gid = gridid
    else:
        obj.gid = j.console.askInteger("Please provide grid id. Grid id must be in range 1 - 32767", minValue=1, maxValue=32767, retry=5)
        j.application.config.set("grid.id",obj.gid)

    obj.initFromLocalNodeInfo()
    key, new, changed = client_node.set(obj)
    print "save to osis"

    obj=client_node.get(key)

    j.application.config.set("grid.node.id",obj.id)
    j.application.config.set("grid.node.machineguid",obj.machineguid)

    print "save to local hrd"
    print "initialization of node done"

