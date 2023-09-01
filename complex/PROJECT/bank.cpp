// Bank.cpp
#include "bank.h"
#include "account.h"
#include <iostream>
Bank::Bank(const std::string& name) : name(name) {}

void Bank::addAccount(const Account& account) {
    accounts.push_back(account);
}

void Bank::displayAccounts() const {
    std::cout << "Bank Name: " << name << "\n";
    std::cout << "Customer Accounts:\n";

    for (const Account& account : accounts) {
        std::cout << "Account Number: " << account.getAccountNumber() << "\n";
        std::cout << "Account Balance: " << account.getBalance() << "\n";
        std::cout << "-----------------------------\n";
    }
}