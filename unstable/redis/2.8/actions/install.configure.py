def main(j,jp):
    import JumpScale.baselib.redis

    if j.application.config.getBool("redis.ac.enable"):
        name="redisac"
        port=j.application.config.getInt("redis.port.%s"%name)
        j.clients.redis.configureInstance("redisac",port,500,True)
    
        name="redisw"
        port=j.application.config.getInt("redis.port.%s"%name)
        j.clients.redis.configureInstance(name,port,300,True)

    name="redisp"
    port=j.application.config.getInt("redis.port.%s"%name)
    j.clients.redis.configureInstance(name,port,500,True)

    name="redism"
    port=j.application.config.getInt("redis.port.%s"%name)
    j.clients.redis.configureInstance(name,port,20,True)

    name="redisc"
    port=j.application.config.getInt("redis.port.%s"%name)
    j.clients.redis.configureInstance(name,port,100,False)

    
