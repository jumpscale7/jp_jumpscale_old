def main(j,jp):
   
    #start the application (only relevant for server apps)
    jp.log("start portalbase")

    j.tools.startupmanager.addProcess('portalbase', 'python', 'portal_start.py', workingdir='/opt/jumpscale/apps/portalbase/')
    j.tools.startupmanager.apply()
    j.tools.startupmanager.startProcess('jumpscale', 'portalbase')

    jp.waitUp(timeout=20)

