def main(j,jp):
   
    import JumpScale.baselib.startupmanager

    osis_ips = j.application.config.getList('osis.ip')
    osis_servers = ''
    for ip in osis_ips:
        osis_servers += '    server %s:5544;\n' % ip

    nginxcfg = '''
upstream osis {
    %s
}

server {
    listen 80;
    #ssl on;
    server_name _;
    location /osis {
        proxy_pass  http://osis;
    }
}
    ''' % osis_servers
    j.system.fs.createDir('$cfgdir/nginx/sites-enabled/')
    j.system.fs.writeFile('$cfgdir/nginx/sites-enabled/default', nginxcfg)
    j.tools.startupmanager.restartProcess("serverapps", "nginx")

    return True