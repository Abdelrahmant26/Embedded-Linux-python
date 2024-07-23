#include <iostream>
#include <iomanip>
#include <string.h>
#include <math.h>
#include <string>
int main(){
    double search;

    double arr[] = {1, 2, 3, 44, 64, 12.34, 22.3, 12.33, 97.21, 122};
    int length = sizeof(arr)/sizeof(arr[0]);
    std::cout<<"{ "<<arr[0];
    for(int i = 1 ; i < length ; i++){
         std::cout<<", "<<arr[i];
    }
    std::cout<<"}\n";
    std::cout<<"Enter a number to search for : \n";
    std::cin>>search;
    std::cout<<" "<<search<<"\n";
    for(int i = 0; i < length; i++){
        if(arr[i] == search){
            std::cout<<i<<"\n";
            for(int a = i; a<=length;a++){
                arr[a] = arr[a+1];
            }
            length--;
            break;
        }
    }
    std::cout<<"{ "<<arr[0];
    for(int i = 1 ; i < length ; i++){
         std::cout<<", "<<arr[i];
    }
    std::cout<<"}\n";
    return 0;
}