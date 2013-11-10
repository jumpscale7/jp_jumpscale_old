def main(j,args,params,tags,tasklet):
   
    #monitor the app if it is performing well, if not ok raise j.errorconditionhandler.raiseMonitoringError( error 
    
    import JumpScale.baselib.circus
    status = j.tools.circus.manager.status('logger')
    if not status in ['active', 'stopped']:
        j.errorconditionhandler.raiseMonitoringError('logger is failing')

    params.result=True #or False
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True