// Account.cpp
#include "account.h"

Account::Account(int accountNumber, double balance)
    : accountNumber(accountNumber), balance(balance) {}

double Account::getBalance() const {
    return balance;
}
double Account::getAccountNumber() const {
    return accountNumber;
}