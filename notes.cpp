#include <iostream>
#include <math.h>
#define MATH_PI  3.1415926535897932384626433832795028841971693993751

class Snapshot{
    public:
        float radius,rotations,duration;
        Snapshot(float radius, float rotations, float duration){
            this->radius = radius;
            this->rotations = rotations;
            this->duration = duration;
        }
        float radians(){
            return (rotations*2*MATH_PI)/duration; 
        }
        float linearSpeedToRPM(float distance){
            float c = 2*MATH_PI*radius;
            return c*distance;
        }
        float linearSpeed(){
            float c = 2*MATH_PI*radius;
            return (c*rotations)/duration;
        }
};

int main(){
    Snapshot c = Snapshot(310,0.23,1);
    printf("\nLinear Speed:%f\n",c.linearSpeed());
    printf("Angular Speed:%f\n\n",c.radians());
    printf("%f",c.linearSpeedToRPM(50));
    return 0;
}