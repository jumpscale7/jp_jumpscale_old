def main(j,jp):
   
    #configure the package 
    cmd="/etc/init.d/nginx stop"
    
    j.system.process.execute(cmd,False)

    cmd="jsuser add -d admin:js007:admin::incubaid"
    j.system.process.execute(cmd,False) #do not die

    print "prepare done"