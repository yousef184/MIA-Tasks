---
title: PROJECT/account.h

---

# PROJECT/account.h



## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Account](Classes/classAccount.md)** <br>Represents a customer's bank account.  |




## Source code

```cpp
// Account.h
#ifndef ACCOUNT_H
#define ACCOUNT_H

class Account {
public:
    Account(int accountNumber, double balance);

    double getBalance() const;
    double getAccountNumber() const;

private:
    int accountNumber; 
    double balance; 
};

#endif // ACCOUNT_H
```


-------------------------------

Updated on 2023-09-01 at 22:52:07 +0300
