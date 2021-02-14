

class StockEntry:

    name = ""
    url = ""
    xpath = ""

    def __init__(self, item_name, url, xpath):
        self.name = item_name
        self.url = url
        self.xpath = xpath