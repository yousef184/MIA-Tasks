---
title: Bank
summary: Represents a bank that manages customer accounts. 

---

# Bank



Represents a bank that manages customer accounts. 


`#include <bank.h>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Bank](Classes/classBank.md#function-bank)**(const std::string & name)<br>Constructor for the [Bank](Classes/classBank.md) class.  |
| void | **[addAccount](Classes/classBank.md#function-addaccount)**(const [Account](Classes/classAccount.md) & account)<br>Add a new customer account to the bank.  |
| void | **[displayAccounts](Classes/classBank.md#function-displayaccounts)**() const<br>Display information about all customer accounts in the bank.  |

## Public Functions Documentation

### function Bank

```cpp
Bank(
    const std::string & name
)
```

Constructor for the [Bank](Classes/classBank.md) class. 

**Parameters**: 

  * **name** The name of the bank. 


### function addAccount

```cpp
void addAccount(
    const Account & account
)
```

Add a new customer account to the bank. 

**Parameters**: 

  * **account** The account to be added. 


### function displayAccounts

```cpp
void displayAccounts() const
```

Display information about all customer accounts in the bank. 

-------------------------------

Updated on 2023-09-01 at 22:52:07 +0300