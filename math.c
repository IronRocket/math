#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#ifdef __linux__

#elif _WIN32
    #include<windows.h>
#endif
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

typedef struct Person{
    int id;
}Person;

void test(int wow){
    wow += 1;
}

void initQueue(Person arr[],int arrSize){
    for(int i = 0;i<arrSize;i++){
        arr[i].id = -1;
    }
}

void insertPerson(Person arr[],int arrSize,int *id){
    for(int i = 0;i<arrSize;i++){
        if (arr[i].id == -1){
            arr[i].id = *id;
            *id += 1;
            break;
        }
    }
}
int frontPerson(Person arr[],int arrSize){
    int id = arr[0].id;
    for(int i = 0;i<arrSize-1;i++){
        if(arr[i].id == -1){
            return id;
        }
        arr[i].id = arr[i+1].id;
    }
    arr[arrSize].id = -1;
    return id;
}

void printArray(Person arr[],int arrSize){
    for(int i = 0;i<arrSize;i++){
        printf("%d,",arr[i].id);
    }
    printf("\n");
}

int main(){
    Person arr[10];
    int size = sizeof(arr)/sizeof(arr[0]);
    int id = 0;
    initQueue(arr,size);
    insertPerson(arr,size,&id);
    insertPerson(arr,size,&id);
    insertPerson(arr,size,&id);
    insertPerson(arr,size,&id);
    printArray(arr,size);
    frontPerson(arr,size);
    printArray(arr,size);
    return 0;
}
