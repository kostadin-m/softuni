class PizzaDelivery:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient, quantity, price_per_unit):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient not in self.ingredients.keys():
            self.ingredients[ingredient] = 0
        self.ingredients[ingredient] += quantity
        self.price += quantity * price_per_unit

    def remove_ingredient(self, ingredient, quantity, price_per_unit):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient not in self.ingredients.keys():
            return f'Wrong ingredient selected! We do not use {ingredient} in {self.name}!'
        if quantity > self.ingredients[ingredient]:
            return f'Please check again the desired quantity of {ingredient}!'
        self.ingredients[ingredient] -= quantity

        self.price -= quantity * price_per_unit

    def make_order(self):
        self.ordered = True
        formatted_ingredients = [f"{ingredient}: {quantity}" for ingredient, quantity in self.ingredients.items()]

        return f"You've ordered pizza {self.name} prepared with {', '.join(formatted_ingredients)} " \
               f"and the price will be {self.price}lv."

