#include <stdio.h>
#include <cassert>

// Before
class PriceCalculator
{
private:
    int unitPrice;
    int num;
public:
    PriceCalculator(int unitPrice, int num);
    int price();
};

PriceCalculator::PriceCalculator(int unitPrice, int num)
{
    this->unitPrice = unitPrice;
    this->num = num;
}

int PriceCalculator::price()
{
    return unitPrice * num * 1.1;
}

// After
class PriceCalculator2
{
private:
    int unitPrice;
    int num;
public:
    PriceCalculator2(int unitPrice, int num);
    int price();
    int addTax(int);
};

PriceCalculator2::PriceCalculator2(int unitPrice, int num)
{
    this->unitPrice = unitPrice;
    this->num = num;
}

int PriceCalculator2::price()
{
    return addTax(unitPrice * num);
}

int PriceCalculator2::addTax(int value)
{
    return value * 1.1;
}

int
main(void)
{
    PriceCalculator p(100, 10);
    PriceCalculator2 p2(100, 10);

    assert(p.price() == p2.price());

    return 0;
}
