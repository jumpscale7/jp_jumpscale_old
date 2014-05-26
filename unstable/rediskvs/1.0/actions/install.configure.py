def main(j,jp):
    import JumpScale.baselib.redis

    name="rediskvs"
    slave=(j.application.config.get("rediskvs.master.addr"),j.application.config.get("rediskvs.master.port"),j.application.config.get("rediskvs.secret"))
    j.clients.redis.configureInstance(name,7771,100,appendonly=False,snapshot=True,slave=slave,ismaster=False)



    
