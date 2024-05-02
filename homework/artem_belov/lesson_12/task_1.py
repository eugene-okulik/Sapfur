class Flower:
    def __init__(self, name, color, freshness, stem_length, price, lifespan):
        self.name = name
        self.color = color
        self.freshness = freshness
        self.stem_length = stem_length
        self.price = price
        self.lifespan = lifespan


class Rose(Flower):
    def __init__(self, color, freshness, stem_length, price, lifespan):
        super().__init__("Rose", color, freshness, stem_length, price, lifespan)


class Lotus(Flower):
    def __init__(self, color, freshness, stem_length, price, lifespan):
        super().__init__("Lotus", color, freshness, stem_length, price, lifespan)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def calculate_wilting_time(self):
        total_lifespan = sum([flower.lifespan for flower in self.flowers])
        return total_lifespan / len(self.flowers) if len(self.flowers) > 0 else 0

    def sort_flowers(self, key):
        self.flowers.sort(key=lambda x: getattr(x, key))

    def search_flowers_by_lifespan(self, lifespan):
        return [flower for flower in self.flowers if flower.lifespan == lifespan]


rose1 = Rose("Red", 90, 30, 5.0, 7)
rose2 = Rose("White", 85, 25, 4.0, 6)
lotus1 = Lotus("Yellow", 95, 40, 6.0, 8)


bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(rose2)
bouquet.add_flower(lotus1)


print("Average wilting time of the bouquet:", bouquet.calculate_wilting_time())


bouquet.sort_flowers("freshness")
print("Sorted flowers by freshness:")
for flower in bouquet.flowers:
    print(flower.name)


search_result = bouquet.search_flowers_by_lifespan(7)
print("Flowers with lifespan 7 days:")
for flower in search_result:
    print(flower.name)
