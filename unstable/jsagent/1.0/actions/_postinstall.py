   
    #copying of files is not done in this step
    # the order is:
    # first do prepare
    # then the system automatically copies (if not in debug) starting from the files section of the jpackage
    # then do this tasklet (install), so is really a post install step

    #shortcut to some usefull install tools
    #do=j.system.installtools

    #configuration is not done in this step !!!!!
    #preparation like system preps like ubuntu deb installs
    
    params.result=True #return True if result ok
    return params
    
    
    return True

