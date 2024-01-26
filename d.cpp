#include <iostream>
#include <math.h>
unsigned int factorial(unsigned int n)
{
    int result = 1, i;
 
    // loop from 2 to n to get the factorial
    for (i = 2; i <= n; i++) {
        result *= i;
    }
 
    return result;
}

int main(){
    std::cout<<factorial(8)/(2*pow(3,7));
}