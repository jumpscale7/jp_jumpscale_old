def main(j,args,params,tags,tasklet):
   
    #stop the application (only relevant for server apps)
    #make sure you doublecheck that the app is really stopped (DO THIS CAREFULLY) e.g. check process & optionally network ports of server process
    
    import JumpScale.baselib.circus
    args.jp.log("stop osis")
    j.tools.circus.manager.stopProcess('osis')

    args.jp.log("test if osis got stopped by doing a port test")
    if j.system.net.waitConnectionTestStopped("127.0.0.1",5544,5)==False:
       j.system.process.killProcessByPort(5544)
       # raise RuntimeError("Could not stop osis, osis did not stop on port 5544.")

    args.jp.log("osis stopped")

    return params
    
    
def match(j,args,params,tags,tasklet):
    return True