#include <iostream>
#include <iomanip>
#include <string.h>
#include <math.h>
#include <string>
int main(){
    int original[] = {5,6,3,2,6,4,9,8,1,10};
    int len = sizeof(original)/sizeof(original[0]);
    int asc[len];
    int des[len];
    [&original, &asc, &des, len]()->void{
        int temp;
        int x[len];
        for(int i = 0 ; i < len ; i++){
            x[i] = original[i];
        }
        for(int i = 0 ; i < len ; i++){
            for (int a = i+1 ; a < len ;a++){
                if(x[a] > x[i]){
                    temp = x[i];
                    x[i] = x[a];
                    x[a] = temp;
                }
            }
        }
        for(int i = 0 ; i < len ; i++){
            des[i] = x[i];
        }
        for(int i = 0 ; i < len ; i++){
            for (int a = i+1 ; a < len ;a++){
                if(x[a] < x[i]){
                    temp = x[i];
                    x[i] = x[a];
                    x[a] = temp;
                }
            }
        }
        for(int i = 0 ; i < len ; i++){
            asc[i] = x[i];
        }
    }();

    std::cout<<"{"<< des[0] ;
    for(int i = 1 ; i < len ; i++){
         std::cout<<", "<<des[i];
    }
    std::cout<<"}\n";

    std::cout<<"{"<< asc[0] ;
    for(int i = 1 ; i < len ; i++){
         std::cout<<", "<<asc[i];
    }
    std::cout<<"}\n";
    return 0;
}