from restaurant import Restaurant
from customer import Customer
from review import Review


def main():
    # Instantiate some customers, restaurants, and reviews
    customer1 = Customer(given_name="John", family_name="Doe")
    customer2 = Customer(given_name="Alice", family_name="Sssmith")

    restaurant1 = Restaurant(name="Tasty Treats")
    restaurant2 = Restaurant(name="Burger Palace")

    review1 = Review(customer1, restaurant1, 4)
    review2 = Review(customer2, restaurant2, 5)

    # Example usage of the methods
    print(customer1.full_name())  # Output: John Doe
    print(restaurant2.average_star_rating())  # Output: 5.0
    print(customer2.num_reviews())  # Output: 1

if __name__ == '__main__':
    main()