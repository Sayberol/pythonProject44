from classes import Shop, Store, Request

if __name__ == '__main__':
    shop = Shop()
    print(shop.limit)
    print(shop.get_limit)
    shop.limit = 8
    print(shop.limit)
    print(shop.get_limit)
