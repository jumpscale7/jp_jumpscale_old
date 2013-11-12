from JumpScale import j
def main(jp):
<<<<<<< local
    pass
=======
    import JumpScale.baselib.startupmanager
    #make sure there are no traces of elastic search any more
    j.system.process.killProcessByPort(9200)
    cmd="/opt/jumpscale/apps/elasticsearch/bin/elasticsearch"
    args="-fD es.config=/etc/elasticsearch/elasticsearch.yml"

    j.tools.startupmanager.addProcess(name="elasticsearch", cmd=cmd, args=args, priority=1)
    j.tools.startupmanager.apply()
>>>>>>> other
