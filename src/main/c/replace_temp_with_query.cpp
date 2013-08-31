#include <cassert>
#include <vector>
#include <iostream>

using namespace std;

// Before
class BookStore
{
private:
    static const int bookBasePrice = 100;
    int num;

public:
    BookStore(int num);
    int price();
};

BookStore::BookStore(int num)
{
    this->num = num;
}

int BookStore::price()
{
    double rate = 1.0;
    double basePrice = num * bookBasePrice;

    if (basePrice >= 1000) {
        rate = 0.9;
    }

    return basePrice * rate;
}

// After
class BookStore2
{
private:
    static const int bookBasePrice = 100;
    int num;

public:
    BookStore2(int num);
    int price();
    double basePrice();
};

BookStore2::BookStore2(int num)
{
    this->num = num;
}

int BookStore2::price()
{
    double rate = 1.0;

    if (basePrice() >= 1000) {
        rate = 0.9;
    }

    return basePrice() * rate;
}

double BookStore2::basePrice()
{
    return num * bookBasePrice;
}


int
main(void)
{
    BookStore bs(100);
    BookStore2 bs2(100);

    printf("%d\n", bs.price());
    assert(bs.price() == bs2.price());
    return 0;
}
