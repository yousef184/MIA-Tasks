---
title: PROJECT/main.cpp

---

# PROJECT/main.cpp



## Functions

|                | Name           |
| -------------- | -------------- |
| int | **[main](Files/main_8cpp.md#function-main)**() |


## Functions Documentation

### function main

```cpp
int main()
```




## Source code

```cpp
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
```


-------------------------------

Updated on 2023-09-01 at 22:52:07 +0300
