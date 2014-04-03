def main(j,jp):
    key = 'workers.queues'
    if j.application.config.exists(key):
        workers = j.application.config.getDict(key)
        if 'monitor' not in workers:
            workers['monitor'] = 1
            j.application.config.setDict(key, workers)
