from configparser import ConfigParser


if __name__ == "__main__":
    cfg = ConfigParser()
    ### WRITE config file 
    cfg['zmData1'] = {'zmienna': 'wartosc1', 'zmienna2': '2', 'zmienna3' : '-4.55', 'zmienna4' : '=', 'zmienna5' : 'false'}
    cfg['zmData2'] = {}
    cfg['zmData2']['zm_string'] = "wartosc1"
    cfg['zmData2']['zm_int'] = '2'
    cfg['zmData2']['zm_float'] = '-4.99' 
    cfg['zmData2']['zm_string'] = '='
    cfg['zmData2']['zm_bool'] = 'false'
    
    with open('config.ini', 'w') as configfile:
        cfg.write(configfile)
        
    ### READ config file
    
    cfg.read('config.ini')
    print(cfg.sections())
    print(cfg.items('zmData1'))
    print(cfg.get('zmData1', 'zmienna'))
    print(cfg.get('zmData1', 'zmienna2'))
    print(cfg.get('zmData1', 'zmienna3'))
    print(cfg.get('zmData1', 'zmienna4'))
    print(cfg.get('zmData1', 'zmienna5'))
    
    print(cfg.get('zmData2', 'zm_string'))
    print(cfg.getint('zmData2', 'zm_int'))
    print(cfg.getfloat('zmData2', 'zm_float'))
    print(cfg.get('zmData2', 'zm_string'))
    print(cfg.getboolean('zmData2', 'zm_bool'))
    
