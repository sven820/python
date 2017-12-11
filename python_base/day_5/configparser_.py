__author__ = "JJ.sven"

import configparser

'''write'''
config = configparser.ConfigParser()

config["DEFAULT"] = {'ServerAliveInterval': '55',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}

topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here

config['DEFAULT']['ForwardX11'] = 'yes'

with open('parser_config', 'w') as configfile:
    config.write(configfile)


'''read'''
config.sections()
config.read('parser_config')
print(config.defaults())
print(config['DEFAULT']['ServerAliveInterval'])
for key in config:
    print(key)

# ########## 改写 ##########
# sec = config.remove_section('bitbucket.org')
# config.write(open('parser_config', "w"))

# sec = config.has_section('wupeiqi')
# sec = config.add_section('wupeiqi')
# config.write(open('i.cfg', "w"))

# config.set('group2','k1',11111)
# config.write(open('i.cfg', "w"))

# config.remove_option('group2','age')
# config.write(open('i.cfg', "w"))

