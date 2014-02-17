def main(j,jp):
    masterip=""

    if j.application.config.get("processmanager.osis.addr")=="":
        # if not j.console.askYesNo("Do you want to log to the log master? or to other node? (Y means to gridmaster)"):
        masterip =j.application.config.get("grid.master.ip")
        port=5544
        # else:
        #     masterip=j.console.askString("Addr of logmaster")
        #     port=j.console.askInteger("port for logmaster, default 5544", defaultValue=5544)

        if j.system.net.tcpPortConnectionTest(masterip, 5544)==False:
            raise RuntimeError("Cannot reach log master on ip %s (using port test 5544 to see if there is an osis server)"%masterip)

        if masterip=="":
            raise RuntimeError("Could not find ip addr of log master, is master osis running? We did connection test on port 5544, but failed")


    if j.application.config.get("grid.master.superadminpasswd") == "":
        passwdmd5 = j.tools.hash.md5_string(j.console.askString("Please provide: grid.master.superadminpasswd", regex="^(?!\s*$).+", retry=5))
    else:
        passwdmd5 = j.application.config.get("grid.master.superadminpasswd")

    if masterip=="":
        masterip =j.application.config.get("processmanager.osis.addr")
        port=int(j.application.config.get("processmanager.osis.port"))

    #now register node
    import JumpScale.grid.osis
    print "make connection to master logger"
    client = j.core.osis.getClient(masterip, user='root',passwd=passwdmd5)
    print "client ok"
    client_node=j.core.osis.getClientForCategory(client,"system","node")
    print "client for client 'node' ok"
    print "connection done, osis ok."

    obj = client_node.new()
    obj.gid = j.application.whoAmI.gid
    obj.nid = j.application.whoAmI.nid
    obj.initFromLocalNodeInfo()
    obj.gid = j.application.whoAmI.gid
    obj.nid = j.application.whoAmI.nid
    key, new, changed = client_node.set(obj)
    print "save to log master osis"

    obj=client_node.get(key)

    #remember master info for further usage
    j.application.config.set("processmanager.osis.addr",masterip)
    j.application.config.set("processmanager.osis.port",port)

    print "initialization of processmanager done"
