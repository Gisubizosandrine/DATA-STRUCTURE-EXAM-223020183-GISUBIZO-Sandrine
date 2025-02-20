//The program prints the message once before checking the condition (i <= 5).
#include <iostream>
using namespace std;

int main() {
int i = 1;
do {
    cout << "This is iteration " << i << endl;
    i++;
} while (i <= 5);
}
