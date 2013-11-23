def main(j,jp):
   
    #check can access osis

    print "test if osis is reachable by doing a port test"

    masterip=j.application.config.get("grid.master.ip")

    if j.system.net.waitConnectionTest(masterip,5544,2)==False:
        raise RuntimeError("Could not configure logger, osis was not found to be active on %s on port 5544."%masterip)       

    print "osis reachable" 

    return True