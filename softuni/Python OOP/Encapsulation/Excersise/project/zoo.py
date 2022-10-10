class Zoo:
    def __init__(self, name, budget, animal_capacity,workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.workers = []
        self.animals = []

    def add_animal(self, animal, animal_price):
        if self.__budget - animal_price < 0:
            return f"Not enough budget"
        if len(self.animals) == self.__animal_capacity:
            return f"Not enough space for animal"
        self.__budget -= animal_price
        self.animals.append(animal)
        return f"{animal.name} the {type(animal).__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity == len(self.workers):
            return f"Not enough space for worker"
        self.workers.append(worker)
        return f'{worker.name} the {type(worker).__name__} hired successfully'


    def fire_worker(self, worker_name):
        for x in self.workers:
            if x.name == worker_name:
                self.workers.remove(x[0])
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"


    def pay_workers(self):
        all_salaries = sum(x.salary for x in self.workers)
        if self.__budget - all_salaries < 0:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= all_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        price_for_animal_care = sum(x.money_for_care for x in self.animals)
        if self.__budget - price_for_animal_care < 0:
            return f"You have no budget to tend the animals. They are unhappy."
        self.__budget -= price_for_animal_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, profit):
        self.__budget += profit

    def animals_status(self):
        animals_dict = {'Lion': [], 'Tiger': [], 'Cheetah': []}
        return self.__result(animals_dict, self.animals, 'animals')

    def workers_status(self):
        workers_dict = {'Keeper': [], 'Caretaker': [], 'Vet': []}
        return self.__result(workers_dict, self.workers, 'workers')

    def __result(self, type_dict, type_list, type):
        result = f"You have {len(type_list)} {type}"
        for obj in type_list:
            obj_name = type(obj).__name__
            if obj_name in type_dict.keys():
                type_dict[obj_name].append(obj)
        for key, value in type_dict.items():
            result += f"\n----- {len(value)} {key}s:\n"
            result += '\n'.join([repr(x) for x in value])
        return result
