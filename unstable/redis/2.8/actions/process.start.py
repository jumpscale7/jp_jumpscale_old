def main(j,jp):
   
    #start the application (only relevant for server apps)
    import JumpScale.baselib.redis
    j.clients.redis.startInstance("redisp")
    j.clients.redis.startInstance("redisc")
    

