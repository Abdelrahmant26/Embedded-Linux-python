#include <iostream>
#include <iomanip>
#include <string.h>
#include <math.h>
#include <string>
int main(){
    float arr[] = {1, 2, 3, 4.5, 5.6, 23, 23.23};
    float max = arr[0];
    for(int i=1;i<7;i++){
        if (arr[i] > max){
            max = arr[i];
        }
    }
    std::cout<<max;
    return 0;
}