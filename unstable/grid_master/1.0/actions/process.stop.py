def main(j,jp):
   
    #stop the application (only relevant for server apps)
    
    jp.log("stop portalbase")
    j.tools.startupmanager.startProcess('jumpscale', 'portalbase')

    jp.waitDown(timeout=20)


