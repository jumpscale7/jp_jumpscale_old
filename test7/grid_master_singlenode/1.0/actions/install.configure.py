def main(j,jp):
    j.packages.findNewest('jumpscale', 'core').install()
    j.packages.findNewest('jumpscale', 'elasticsearch1').install()
    j.packages.findNewest('jumpscale', 'graphite').install()
    j.packages.findNewest('jumpscale', 'grid_master').install()
