#ifndef SALESITEM_H
#define SALESITEM_H

#include <iostream>
#include <string>

class SalesItem {
    friend std::istream& operator>>(std::istream&, SalesItem&);
    friend std::ostream& operator<<(std::ostream&, const SalesItem&);
    friend bool operator<(const SalesItem&, const SalesItem&);
    friend bool operator==(const SalesItem&, const SalesItem&);

    public:
        SalesItem() = default;
        SalesItem(const std::string &book): bookNo(book){  }
        SalesItem(std::istream &is) { is >> *this; }
    public:
        SalesItem& operator+=(const SalesItem&);
        std::string isbn() const {return bookNo; }
        double avg_price() const;
    private:
        std::string bookNo;
        unsigned units_sold = 0;
        double revenue = 0.0;
};

inline bool compareIsbn(const SalesItem &lhs, const SalesItem &rhs){
    return lhs.isbn() == rhs.isbn(); 
}

SalesItem operator+(const SalesItem&, const SalesItem&);

inline bool operator==(const SalesItem &lhs, const SalesItem &rhs){
    return lhs.units_sold == rhs.units_sold && 
            lhs.revenue == rhs.revenue &&
            lhs.isbn() == rhs.isbn();
}

inline bool operator !=(const SalesItem &lhs, const SalesItem &rhs){
    return !(lhs == rhs); 
}
SalesItem& SalesItem::operator+=(const SalesItem& rhs){
    units_sold += rhs.units_sold;
    revenue += rhs.revenue;
    return *this;
}

SalesItem operator+(const SalesItem& lhs, const SalesItem& rhs){
    SalesItem ret(lhs);
    ret += rhs;
    return ret;
}

std::istream& operator>>(std::istream& in , SalesItem& s){
    double price;
    in >> s.bookNo >> s.units_sold >> price;
    if (in)
        s.revenue = s.units_sold * price;
    else 
        s = SalesItem();
    return in;
}

std::ostream& operator<<(std::ostream& out, const SalesItem& s)
{
    out << s.isbn() << " "<< s.units_sold << " "<< s.revenue << " "<< s.avg_price();
    return out;
}

double SalesItem::avg_price() const {
    if(units_sold)
        return revenue/units_sold;
    else 
    return 0;
}
#endif