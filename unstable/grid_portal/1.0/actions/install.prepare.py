
def main(j,jp):
    path="$(jumpscale.paths.base)/apps/portals/$(grid.portal.instance)"
    if j.system.fs.isLink(path):
        j.system.fs.unlink(path)

    j.packages.findNewest('jumpscale', 'core').install()
    j.packages.findNewest('jumpscale', 'libs').install()
    j.packages.findNewest('jumpscale', 'redis').install()
    j.packages.findNewest('jumpscale', 'mongodb').install()
    j.tools.startupmanager.startAll()
    j.packages.findNewest('jumpscale', 'osis').install()
    j.tools.startupmanager.startAll()
