---
title: PROJECT/customer.h

---

# PROJECT/customer.h



## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Customer](Classes/classCustomer.md)** <br>Represents a bank customer.  |




## Source code

```cpp
// Customer.h
#ifndef CUSTOMER_H
#define CUSTOMER_H

#include <string>

class Customer {
public:
    Customer(const std::string& name);

    std::string getName() const;

private:
    std::string name; 
};

#endif // CUSTOMER_H
```


-------------------------------

Updated on 2023-09-01 at 22:52:07 +0300
