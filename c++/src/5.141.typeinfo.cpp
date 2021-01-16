// typeinfo -- typeinfo 
#include <iostream>
#include <typeinfo>

using namespace std;
typedef float* FLOATPTR;

typedef const float* CFLOAT;
FLOATPTR pa, pb;

CFLOAT pc;
int main() {
    cout << "pa type:" << typeid(pa).name() << endl;
    cout << "pb type:" << typeid(pb).name() << endl;
    cout.setf(ios_base::boolalpha);
    cout << "pa type (float*): " << (typeid(pa) == typeid(float*)) << endl;
    cout << "pb type (float*): " << (typeid(pb) == typeid(float*)) << endl;
    cout << "pb type (const float*): " << ( typeid(pb) == typeid(const float*)) << endl;
    cout << "pc type (const float*): " << ( typeid(pc) == typeid(const float*)) << endl; 
    return 0;
}