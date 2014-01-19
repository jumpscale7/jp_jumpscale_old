
def main(j,jp):
    gridid=j.application.config.getInt("gridmaster.grid.id")
    j.application.config.set("grid.id",gridid)

    j.application.config.set("grid.master.ip","127.0.0.1")

    #check osis installed
    if not j.system.net.tcpPortConnectionTest("127.0.0.1", 5544):
        j.tools.startupmanager.startProcess('jumpscale', 'elasticsearch')
        j.tools.startupmanager.startProcess('jumpscale', 'osis')

    #register in osis
    import JumpScale.grid.osis
    client = j.core.osis.getClient(user="root")
    client.createNamespace(name="system",template="coreobjects",incrementName=False)
    client_grid=j.core.osis.getClientForCategory(client,"system","grid")

    gridobj = client_grid.new(name="grid_%s"%gridid,id=gridid)
    gridobj.initFromLocalNodeInfo()
    key, new, changed = client_grid.set(gridobj)


    #configure avahi
    if j.application.config.getBool("gridmaster.useavahi"):
        j.application.config.set("grid.useavahi",1)        
        import JumpScale.baselib.remote.avahi
        j.remote.avahi.registerService("js_grid_%s"%gridid,5544)
    else:
        j.application.config.set("grid.useavahi",0)
