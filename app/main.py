class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand
        cars = [Car]

    pass


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power= clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings


    def serve_cars(self, cars: list) -> list:
        served_cars = []
        for car in cars:
            if car.clean_mark < self.clean_power:
                served_cars.append(car)
        # for car in served_cars:
        #     car.clean_mark = self.clean_power
        for car in served_cars:
            self.wash_single_car(car)
        return served_cars
    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, cars: list) -> float:
        price = []
        income = sum(list(price))
        served_cars = self.serve_cars(cars)
        for car in served_cars:
            if not served_cars:
                return 0
            else:
               washing_price = round(car.comfort_class * (self.clean_power - car.clean_mark) * (self.average_rating/self.distance_from_city_center), 1)
               price.append(washing_price)
        return income


    def rate_service(self, rate: float):
        sum_of_rates = self.count_of_ratings * self.average_rating
        self.count_of_ratings += 1
        self.average_rating = round(((sum_of_rates + rate) / self.count_of_ratings), 1)

