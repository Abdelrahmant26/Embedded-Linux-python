#include <iostream>
#include <iomanip>
#include <string.h>
#include <math.h>
#include <string>
int main(){
    double arr1[] = {1, 2, 3, 44, 64, 12.34, 22.3, 12.33, 97.21, 122};
    double ar2[] = {1, 2, 3, 4, 5};
    int length1 = sizeof(arr1)/sizeof(arr1[0]);
    int length2 = sizeof(ar2)/sizeof(ar2[0]);
    const int len = length1+length2;
    double result[len];
    std::cout<<length1<<"    "<<length2<<"\n";
    for(int i = 0 ; i < length1; i++){
        result[i]=arr1[i];
    }
    for(int a = 0 ; a < length2; a++){
        result[a+length1]=ar2[a];
    }
    std::cout<<"{ "<<result[0];
    for(int i = 1 ; i < length1+length2 ; i++){
         std::cout<<", "<<result[i];
    }
    std::cout<<"}\n";
    return 0;
}