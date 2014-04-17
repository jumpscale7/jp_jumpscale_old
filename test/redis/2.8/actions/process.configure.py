def main(j,jp):
   
    #configure the application to autostart
    import JumpScale.baselib.redis
    j.clients.redis.deleteInstance("redisp")
    j.clients.redis.deleteInstance("redisc")
    j.clients.redis.configureInstance("redisp",7768,500,True)
    j.clients.redis.configureInstance("redisc",7767,100,False)

    

