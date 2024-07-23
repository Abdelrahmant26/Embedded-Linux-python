#include <iostream>
#include <iomanip>
#include <string.h>
#include <math.h>
#include <string>
int main(){
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
    int len = sizeof(arr)/sizeof(arr[0]);
    int even[len];
    int odd[len];
    int lenEven=0, lenOdd=0;
    for(int i = 0 ; i < len ; i++){
        if((arr[i]%2)==0){
            even[lenEven] = arr[i];
            lenEven++;
        }
    } 
    for(int i = 0 ; i < len ; i++){
        if((arr[i]%2)!=0){
            odd[lenOdd] = arr[i];
            lenOdd++;
        }
    } 
    std::cout<<"even : { "<<even[0];
    for(int i = 1 ; i < lenEven ; i++){
         std::cout<<", "<<even[i];
    }
    std::cout<<"}\n";
    std::cout<<"odd : { "<<odd[0];
    for(int i = 1 ; i < lenOdd ; i++){
         std::cout<<", "<<odd[i];
    }
    std::cout<<"}\n";
    return 0;
}