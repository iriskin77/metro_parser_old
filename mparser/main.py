from mparser.metro_parser import ParserMetro


url_main = "https://online.metro-cc.ru/category/sladosti-chipsy-sneki/konfety-podarochnye-nabory"

prox = [
        {"http": "socks5://217.29.53.133:11012"},
        {"http": "http://217.29.53.104:11045"},
        {"http": "http://217.29.53.104:11046"},
]

def main():

    pars_metro = ParserMetro(url_main, prox)
    pars_metro()

if __name__ == '__main__':
    main()





