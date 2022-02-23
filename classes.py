from abc import abstractmethod


class Storage:
    @abstractmethod
    def add(self, name, count):
        # is_found = False
        # for key in self.items.keys():
        #     if key == key:
        #         self.items[key] = self.items[key] + count
        # if not is_found:
        #     self.items[key] = count
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_item(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

    def add(self, name, count):
        is_found = False
        if self.get_free_space() > count:
            for key in self.items.keys():
                if name == key:
                    self.items[key] = self.items[key] + count
                    is_found = True
            if not is_found:
                self.items[key] = count
            print("Товар добавлен")
        else:
            print(f"Товар не может быть добавлен, так как есть места осталось {self.get_free_space()}")

    def remove(self, name, count):
        for key in self.items.keys():
            if name == key:
                if self.items[key] >= 0:
                    self.items[key] = self.items[key] + count
                else:
                    print(f"Слишком мало {name.title()}")
            else:
                print(f"{name.title()} не найден на складе")

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_item(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items.keys())


class Shop(Store):
    def __init__(self, limit=5):
        super().__init__()
        self.capacity = 20
        self.limit = limit

    @property
    def get_limit(self):
        return self.limit

    def add(self, name, count):
        if self.get_unique_items_count() < self.limit:
            super.add(name, count)
        else:
            print(f"Товар не может быть добавлен")


class Request:
    def __init__(self, str):
        lst = self.get_info(str)
        self.from_ = lst[4]
        self.to = lst[6]
        self.amount = int(lst[1])
        self.product = lst[2]

    def get_info(self, str):
        return str.split(" ")

    def __repr__(self):
        return f'Доставить {self.amount} {self.product} из {self.from_} в {self.to}'

