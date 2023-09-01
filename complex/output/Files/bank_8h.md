---
title: PROJECT/bank.h

---

# PROJECT/bank.h



## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Bank](Classes/classBank.md)** <br>Represents a bank that manages customer accounts.  |




## Source code

```cpp
// Bank.h
#ifndef BANK_H
#define BANK_H

#include <string>
#include <vector>

class Account; // Forward declaration

class Bank {
public:
    Bank(const std::string& name);

    void addAccount(const Account& account);

    void displayAccounts() const;

private:
    std::string name; 
    std::vector<Account> accounts; 
};

#endif // BANK_H
```


-------------------------------

Updated on 2023-09-01 at 22:52:07 +0300
