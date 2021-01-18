// assgn_st.cpp -- assigning structures 
#include <iostream>

struct inflatable 
{
    char name[20];
    float volume;
    double price;
};

struct perks 
{
    int key_number;
    char car[12];
} mr_smith, ms_jones; // two perks variables

struct another 
{
    int key_number;
    char car[12];
} mr_glitz = {
    7,  // value for mr_glitz.key_number member
    "Packard" // value for mr_glitz.car member 
};

struct  // no tag
{
    int x; // 2 members
    int y;
} position; // a structure variable 

int main(){
    using namespace std;
    inflatable bouquet = {
        "sunflowers",
        0.20,
        12.49
    };
    inflatable choice;
    cout << "bouquet : " << bouquet.name << " for $";
    cout << bouquet.price << endl;
    choice = bouquet; // assign one structure to another 
    cout << "choice: " << choice.name << " for $";
    cout << choice.price << endl;
    return 0;
}