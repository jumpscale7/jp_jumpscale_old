   
    #monitor the app if it is performing well, return False if not

    test=False

    #test 1
    test =test & j.system.net.tcpPortConnectionTest("localhost", 5544)
    print test

    #test 2
    #do an osis test using the lib

    params.result=test

    return params
    
    
    return True
