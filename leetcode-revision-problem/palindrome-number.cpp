#include <iostream>
#include <vector>
using namespace std;

bool isPalindrome(int x) {

    if(x < 0) {
        return false;
    }

    int r = 0;
    int remin;
    int orginal = x;

    while(x != 0){
        remin = x % 10;
        r = r * 10 + remin;
        x /= 10;
    }

    return (r == orginal);

}



int main() {

     int x = -121;

     cout << isPalindrome(x);


    return 0;
}


