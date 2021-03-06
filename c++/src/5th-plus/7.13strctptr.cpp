// strctptr.cpp -- functions with pointer to structure arguments
#include <iostream>
#include <cmath>
// structure templates 

struct polar 
{
    double distance; // distance from origin 
    double angle; // direction from origin 
};

struct react 
{
    double x; // horizontal distance from origin 
    double y; // vertical distance from origin 
};

// prototypes 
void react_to_polar(const react *pxy, polar *pda);
void show_polar(const polar *pda);

int main() {
    using namespace std; 
    react rplace;
    polar pplace;

    cout << "Enter the x and y values: ";
    while (cin >> rplace.x >> rplace.y) {
        react_to_polar(&rplace, &pplace); // pass addresses
        show_polar(&pplace); // pass address
        cout << "Next two numbers(q to quit):";
    }
    cout << "Done.\n";
    return 0;
}

// show polar coordinates, converting angle to degrees
void show_polar(const polar *pda)
{
    using namespace std;
    const double Rad_to_deg = 57.29577951;
    cout << "distance = " << pda->distance;
    cout << ", angle = " << pda->angle * Rad_to_deg;
    cout << " degrees\n";
}

// convert rectangular to polar coordinates;
void react_to_polar(const react *pxy, polar *pda){
    using namespace std;
    pda->distance = sqrt(pxy->x * pxy->x + pxy->y * pxy->y);
    pda->angle = atan2(pxy->y, pxy->x);
}