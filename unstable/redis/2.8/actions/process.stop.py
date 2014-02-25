def main(j,jp):
   
    #stop the application (only relevant for server apps)
    
    import JumpScale.baselib.redis
    j.clients.redis.stopInstance("redisp")
    j.clients.redis.stopInstance("redisc")

