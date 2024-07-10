#include <iostream>
#include <iomanip>
#include <string.h>
#include <math.h>
int main(){
    for(int i = 1; i<=12; i++){
        for (int x = 1; x<=12; x++){
            std::cout<<i<<"x"<<x<<"="<<i*x<<"\n";
        }
        std::cout<<"\n\n";
    }
    return 0;
}