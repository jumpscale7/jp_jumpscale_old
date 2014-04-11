def main(j,jp):
    import JumpScale.baselib.redis

    if j.application.config.getBool("redis.ac.enable"):
        name="redisac"
        port=j.application.config.getInt("redis.port.%s"%name)
        j.clients.redis.configureInstance("redisac",port,500,True)

    j.clients.redis.configureInstance("redisp",7768,500,True)
    j.clients.redis.configureInstance("redisc",7767,100,False)
    
