def main(j,jp):
    # remove the default nginx server config
    j.system.fs.remove(j.system.fs.joinPaths('/etc', 'nginx', 'sites-enabled', 'default'))
    j.system.process.execute('service nginx restart')