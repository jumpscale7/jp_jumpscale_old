def main(j,jp):
    j.packages.findNewest('jumpscale', 'elasticsearch1').start()
    j.packages.findNewest('jumpscale', 'graphite').start()
