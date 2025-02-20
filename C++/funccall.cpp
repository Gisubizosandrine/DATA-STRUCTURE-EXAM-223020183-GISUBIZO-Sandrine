// functions don't return anything but still perform a task are void functions.
#include <iostream>
using namespace std;
void greet(string name) {
    cout << "Hello, " << name << "!" << endl;
}

int main() {
    greet("Alice");  // Calling the function
    return 0;
}

