from JumpScale import j
def main(j,jp):
    import JumpScale.baselib.startupmanager
    status = j.tools.startupmanager.status('elasticsearch')
    if not status in ['active', 'stopped']:
        j.errorconditionhandler.raiseMonitoringError('elasticsearch is failing')
    return True
