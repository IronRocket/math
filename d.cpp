#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>

typedef struct Person{
    int id;
}Person;


class Queue{
    private:
        int id;
        std::vector<Person> v;
    public:
        Queue(int size){
            id = 0;
            Person p = {-1};
            for (int i = 0;i<size-1;i++){
                v.push_back(p);
            }
        }
        int insertPerson(){
            for (int i = 0;i<v.size();i++){
                if(v[i].id == -1){
                    v[i].id = id;
                    id++;
                    return v[i].id;
                }
            }
            return -1;
        }
        int frontPerson(){
            int removedId = v[0].id;
            if (removedId == -1){
                return -1;
            }
            v.erase(v.begin());
            v.insert(v.end(),Person{-1});
            return removedId;
        }
        void printArray(){
            for(int i = 0;i<v.size();i++){
                printf("%d,",v[i].id);
            }
            printf("\n");
        }

};

int main(){
    
}