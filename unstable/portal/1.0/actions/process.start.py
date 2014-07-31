def main(j,jp):
   
    #start the application (only relevant for server apps)
    jp.log("start $(jp.name)")


    if jp.hrd_instance.get("portal_auth_source_addr")=="127.0.0.1":
        jposis=j.packages.findByName("osis")
        if j.tools.startupmanager.getStatus4JPackage(jposis)==False:
            jposis.start()

    j.tools.startupmanager.startJPackage(jp)
    jp.waitUp(timeout=20)

