def main(j,jp):
   
    #configure the package 

    #needed because the new location is site packages, just to make sure it gets removed
    j.system.fs.removeDirTree("/usr/local/lib/python2.7/dist-packages/JumpScale/")    
    j.system.fs.removeDirTree("/usr/local/lib/python2.7/dist-packages/JumpScale_core-6.0.0.egg-info/")    
    