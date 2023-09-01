// Customer.cpp
#include "customer.h"

Customer::Customer(const std::string& name) : name(name) {}

std::string Customer::getName() const {
    return name;
}