from collections import namedtuple


def driver_carrying_capacity(driver, num_packages):
    return driver.car_capacity >= num_packages

def main():
    Driver = namedtuple("driver", ["name", "car_type","car_capacity"])

    amos = Driver("Amos", "Benz", 5 )
    bruce = Driver("Bruce","C200", 5)
    zac = Driver("Zac", "Outlander",5)
    print(driver_carrying_capacity(zac,30))

if __name__ == "__main__":
    main()
