#include <iostream>
#include <iomanip>
#include <string.h>
#include <math.h>
#include <string>
int main(){
    double search;
    double arr[] = {1, 2, 3, 44, 64, 12.34, 22.3, 12.33, 97.21, 122};
    std::cout<<"Enter a number to search for : \n";
    std::cin>>search;
    std::cout<<" "<<search<<"\n";
    for(int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++){
        if(arr[i] == search){
            std::cout<<i<<"\n";
             break;
        }
    }

    return 0;
}