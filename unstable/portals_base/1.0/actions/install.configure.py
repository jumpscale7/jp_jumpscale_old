def main(j,jp):
   
    #configure the package 
    cmd="/etc/init.d/nginx stop"
    j.system.process.execute(cmd)

    cmd="jsuser add -d admin:admin:admin::incubaid"    
    j.system.process.execute(cmd)
