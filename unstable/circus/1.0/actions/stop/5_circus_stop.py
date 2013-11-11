def main(j,args,params,tags,tasklet):
   
    #stop the application (only relevant for server apps)
    #make sure you doublecheck that the app is really stopped (DO THIS CAREFULLY) e.g. check process & optionally network ports of server process
    
    # import JumpScale.baselib.circus
    # args.jp.log("start osis")
    # j.tools.circus.manager.stopProcess('osis')

    # args.jp.log("test if osis got started by doing a port test")
    # if j.system.net.waitConnectionTestStopped("127.0.0.1",5544,5)==False:
    
    for port in [5555,5556,5557,8080]:
        j.system.process.killProcessByPort(port)


    # if j.system.net.waitConnectionTestStopped("127.0.0.1",5544,1)==False:
    #    raise RuntimeError("Could not stop osis, osis did not stop on port 5544.")


    return params
    
    
def match(j,args,params,tags,tasklet):
    return True