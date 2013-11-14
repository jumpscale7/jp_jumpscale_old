
def main(j,jp):
    import JumpScale.baselib.startupmanager
    status = j.tools.startupmanager.status('logger')
    if not status in ['active', 'stopped']:
        j.errorconditionhandler.raiseMonitoringError('logger is failing')
    return True
