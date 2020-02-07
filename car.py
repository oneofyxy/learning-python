"""A class that can be used to represent a car."""


class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """'Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car`s mileage."""
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        """
        Set the odometer to a given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cannot roll back a odometer!')

    def increment_odometer(self, increment):
        """
        Add a given amount to the odometer reading.
        Reject the change if the increment is minus.
        """
        if increment >= 0:
            self.odometer_reading += increment
        else:
            print('You cannot roll back an odometer!')


class Battery():
    """A simple attempt to represent a electric vehicles."""

    def __init__(self, battery_size=70):
        """Initialize attributes specific to electric vehicles."""
        self.battery_size = battery_size

    def describe_battery_size(self):
        """Print a statement showing the battery size."""
        print(
            'This car has a ' +
            str(self.battery_size) +
            '-kwh battery.')

    def get_range(self):
        """"Print a statement showing about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        print(
            'This car can go approximately ' +
            str(range) +
            ' miles on a full charge.'
        )


class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of parent class.
        Then initialize attribute specific to a electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
