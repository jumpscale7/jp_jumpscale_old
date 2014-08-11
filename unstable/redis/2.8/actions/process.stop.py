def main(j,jp):
    #stop the application (only relevant for server apps)
    jp.log("stop $(jp.name)")

    name="redis_$(redis.name)"
    j.tools.startupmanager.stopProcess('redis', name)

