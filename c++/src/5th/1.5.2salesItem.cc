#include <iostream>
#include "salesItem.h"

int main()
{
    SalesItem item1, item2;
    std::cin >> item1 >> item2;
    if (item1.isbn() == item2.isbn())
    {
        std::cout << item1 + item2 << std::endl;
        return 0;
    } else {
        std::cerr << "Data must refer to same ISBN" << std::endl;
        return -1;
    }
    // 0-201-78345-x 3 20.00
    // 0-201-78345-x 2 25.00
}