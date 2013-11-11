def main(j,args,params,tags,tasklet):
   
    #stop the application (only relevant for server apps)
    #make sure you doublecheck that the app is really stopped (DO THIS CAREFULLY) e.g. check process & optionally network ports of server process

    import JumpScale.baselib.circus
    args.jp.log("stop logger")
    j.tools.startupmanager.stopProcess('logger')

    args.jp.log("test if logger got stopped by doing a port test")
    if not j.system.net.waitConnectionTestStopped("127.0.0.1",4443,5):
       j.system.process.killProcessByPort(4443)
       # raise RuntimeError("Could not stop osis, osis did not stop on port 5544.")

    args.jp.log("logger stopped")
    
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True