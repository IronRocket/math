#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define M_PI 3.14159265358979323846


unsigned int factorial(unsigned int n)
{
    int result = 1, i;

    for (i = 2; i <= n; i++) {
        result *= i;
    }
 
    return result;
}

double degreesToRadians(double degrees){
    return (M_PI/180)*degrees;
}

double funcCos(float x,int n){
    double cosAprox = 0;
    double coef,num;
    double denom;
    for(int i = 0;i<n;i++){
        coef = pow((-1),i);
        num = pow(x,(2*i));
        denom = factorial(2*i);
        cosAprox += coef* (num/denom);
    }
    return cosAprox;
}


int main(){
    double c = cos(degreesToRadians(2));
    double *ptr = &c;
    printf("%p,%f\n",ptr,funcCos(degreesToRadians(2),5));
    return 0;
}
