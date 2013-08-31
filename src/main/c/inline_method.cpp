#include <cassert>
#include <vector>
#include <iostream>

using namespace std;

// Before
class Calculator
{
private:
    vector<int> array;
public:
    Calculator(int num, ...);
    bool isOverThousand(int val);
    int compute();
};

Calculator::Calculator(int num, ...)
{
    va_list args;
    va_start(args, num);

    for (int i = 0; i < num; i++) {
        int val = va_arg(args, int);
        array.push_back(val);
    }

    va_end(args);
}

bool Calculator::isOverThousand(int val)
{
    return val > 1000;
}

int Calculator::compute()
{
    int total = 0;
    for (int i = 0; i < array.size(); i++) {
        total += array[i];
    }

    if (isOverThousand(total)) {
        total = 1000;
    }

    return total;
}

// After
class Calculator2
{
private:
    vector<int> array;
public:
    Calculator2(int num, ...);
    bool isOverThousand(int val);
    int compute();
};

Calculator2::Calculator2(int num, ...)
{
    va_list args;
    va_start(args, num);

    for (int i = 0; i < num; i++) {
        int val = va_arg(args, int);
        array.push_back(val);
    }

    va_end(args);
}

int Calculator2::compute()
{
    int total = 0;
    for (int i = 0; i < array.size(); i++) {
        total += array[i];
    }

    if (total > 1000) {
        total = 1000;
    }

    return total;
}


int
main(void)
{
    Calculator c(1, 2, 31);
    Calculator c2(1, 2, 31);

    assert(c.compute() == c2.compute());
}
