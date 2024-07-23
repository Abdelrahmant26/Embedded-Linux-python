#include <iostream>
#include <iomanip>
#include <string.h>
#include <math.h>
#include <string>
int main(){
    int x;
    std::cout<<"enter a number : \n";
    std::cin>>x;
    [x]()->void{
        std::cout<<(x*x)<<"\n";
    }();
    /*std::cout<<"odd : { "<<odd[0];
    for(int i = 1 ; i < lenOdd ; i++){
         std::cout<<", "<<odd[i];
    }
    std::cout<<"}\n";*/
    return 0;
}