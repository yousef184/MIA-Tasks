// Account.h
#ifndef ACCOUNT_H
#define ACCOUNT_H

/**
 * @class Account
 * @brief Represents a customer's bank account.
 */
class Account {
public:
    /**
     * @brief Constructor for the Account class.
     * @param accountNumber The account number.
     * @param balance The account balance.
     */
    Account(int accountNumber, double balance);

    /**
     * @brief Get the account balance.
     * @return The account balance.
     */
    double getBalance() const;
    /**
     * @brief Get the account number.
     * @return The account balance.
     */
    double getAccountNumber() const;

private:
    int accountNumber; /**< The account number. */
    double balance; /**< The account balance. */
};

#endif // ACCOUNT_H