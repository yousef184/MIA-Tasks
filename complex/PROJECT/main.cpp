// main.cpp
#include "bank.h"
#include "account.h"
#include "customer.h"

int main() {
    // Create a bank
    Bank bank("MyBank");

    // Create customer accounts
    Account account1(101, 5000.0);
    Account account2(102, 7500.0);

    // Add accounts to the bank
    bank.addAccount(account1);
    bank.addAccount(account2);

    // Display customer account information
    bank.displayAccounts();
    return 0;
}