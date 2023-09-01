// Customer.h
#ifndef CUSTOMER_H
#define CUSTOMER_H

#include <string>

/**
 * @class Customer
 * @brief Represents a bank customer.
 */
class Customer {
public:
    /**
     * @brief Constructor for the Customer class.
     * @param name The customer's name.
     */
    Customer(const std::string& name);

    /**
     * @brief Get the customer's name.
     * @return The customer's name.
     */
    std::string getName() const;

private:
    std::string name; /**< The customer's name. */
};

#endif // CUSTOMER_H