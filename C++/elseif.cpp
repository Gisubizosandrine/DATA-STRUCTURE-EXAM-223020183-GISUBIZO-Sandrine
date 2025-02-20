//The program checks if the person is an adult, senior, or minor based on their age
#include <iostream>
using namespace std;

int main() {
int age = 25;
if (age >= 18 && age < 60) {
    cout << "You are an adult." << endl;
} else if (age >= 60) {
    cout << "You are a senior citizen." << endl;
} else {
    cout << "You are a minor." << endl;
}
}
