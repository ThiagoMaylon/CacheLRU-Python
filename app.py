class CacheLru():
    def __init__(self, capacity):
        self.order = []
        self.capacity = capacity
        self.itens = {}
    
    def set(self, key, value):
        if key in self.itens:
            for k in self.order:
                if k == key:
                    self.order.remove(k)
                    del self.itens[key]
            self.order.append(key)
            self.itens[key] = value
        else:
            self.order.append(key)
            self.itens[key] = value
            if len(self.itens) > self.capacity:
                k = self.order[0]
                self.order.pop(0)
                del self.itens[k]
                self.order.append(key)
                self.itens[key] = value
    def get(self, key):
        if key not in self.order:
            return -1
        else:
            for k in self.order:
                if k == key:
                    value = self.itens[k]
                    self.order.remove(k)
                    del self.itens[k]
            self.order.append(key)
            self.itens[key] = value

# inicializando a minha classe com a capacidade de 5
cache = CacheLru(5)
# testando a método set()
cache.set("Bala", 1)
cache.set("Refrigerante", 2)
cache.set("Paçoca", 3)
cache.set("Biscoito", 4)
cache.set("Pirulito", 5)
print(cache.itens)
cache.set("Bala", 2)
print(cache.itens)
cache.set("Jujuba", 2)
print(cache.itens)

# testando o método get()
cache.get("Paçoca")
print(cache.itens)
cache.set("Refrigerante", 2)
print(cache.itens)