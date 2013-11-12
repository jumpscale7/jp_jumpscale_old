   
    fwtypes=["shorewall_protect_node","shorewall_dual_nic"]

    fwtype=j.console.askChoice(fwtypes)        

    j.system.fs.removeDirTree("/etc/shorewall")

    nics=j.system.net.getNics()

    if j.application.config.get("firewall.nics.vpn").strip()=="":
        for item in nics:
            if item.find("tun")<>-1:
                j.application.config.set("firewall.nics.vpn",item)
    intnic=j.application.config.get("firewall.nics.vpn").strip()
    try:
        nics.pop(nics.index(intnic))
    except:
        pass

    if j.application.config.get("firewall.nics.pub").strip()=="":
        intnic=j.console.askChoice(nics,"Choose nics which are public")
        j.application.config.set("firewall.nics.pub",intnic)
    intnic=j.application.config.get("firewall.nics.pub").strip()
    try:
        nics.pop(nics.index(intnic))
    except:
        pass

    if j.application.config.get("firewall.nics.private").strip()=="":    
        intnics=j.console.askChoiceMultiple(nics,"Choose nics which are private")
        for nic in intnics:
            nics.pop(nics.index(nic))
        intnic=",".join(intnics).strip(",")
        if intnic=="":
            intnic="none"
        j.application.config.set("firewall.nics.private",intnic)

    if j.application.config.get("firewall.nics.dmz").strip()=="":
        dmznics=j.console.askChoiceMultiple(nics,"Choose nics which are for dmz")
        for nic in dmznics:
            nics.pop(nics.index(nic))
        dmznic=",".join(dmznics).strip(",")
        if dmznic=="":
            dmznic="none"
        j.application.config.set("firewall.nics.dmz",dmznic)

        
    j.application.config.set("firewall.ruletemplate",fwtype)
    j.application.config.set("firewall.type","shorewall")


    args.jp.copyFiles(subdir=fwtype,destination="/etc/shorewall",applyhrd=True) #  will copy files from subdir called root of platforms to root of system (carefull), will also use templateEngine for hrd 

    do=j.system.installtools
    rescode,res=j.system.process.execute("shorewall restart")
    if rescode<>0:
        o.errorconditionhandler.raiseBug(message="Could not restart shorewall.",category="shorewall.init")

    rescode,res=j.system.process.execute("shorewall status")
    if rescode<>0:
        o.errorconditionhandler.raiseBug(message="Could not get status from shorewall.",category="shorewall.status")

    res=res.lower()
    if res.find("started")==-1:
        o.errorconditionhandler.raiseBug(message="Could not start shorewall.",category="shorewall.status")


    return params
    
    
    return True

