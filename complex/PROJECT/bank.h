// Bank.h
#ifndef BANK_H
#define BANK_H

#include <string>
#include <vector>

class Account; // Forward declaration

/**
 * @class Bank
 * @brief Represents a bank that manages customer accounts.
 */
class Bank {
public:
    /**
     * @brief Constructor for the Bank class.
     * @param name The name of the bank.
     */
    Bank(const std::string& name);

    /**
     * @brief Add a new customer account to the bank.
     * @param account The account to be added.
     */
    void addAccount(const Account& account);

    /**
     * @brief Display information about all customer accounts in the bank.
     */
    void displayAccounts() const;

private:
    std::string name; /**< The name of the bank. */
    std::vector<Account> accounts; /**< List of customer accounts. */
};

#endif // BANK_H