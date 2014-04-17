def main(j,jp):
    j.packages.findNewest('jumpscale', 'elasticsearch').start()
    j.packages.findNewest('jumpscale', 'graphite').start()
