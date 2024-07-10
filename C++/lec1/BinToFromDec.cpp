#include <iostream>
#include <iomanip>
#include <string.h>
#include <math.h>
#include <string>
int main(){
    std::string A;
    std::cout<<"enter a number :\n";
    std::cin>>A;
    int a=0;
    for(int i=0;i<A.length();i++){
        a+=(A[i]-'0')*pow(10,A.length()-1-i);
    }
    int arr[32];
    for(int i=0;i<32;i++){
        arr[32-1-i]=a%2;
        a/=2;
    }
    for(int i=0;i<32;i++){
        std::cout<<arr[i];
    }
    std::string bin;
    std::cout<<"\nenter a binary number : \n";
    std::cin>>bin;
    int res=0;
    for(int i=0;i<bin.length();i++){
        if(bin[i]=='1'){
            res+=pow(2, bin.length()-1-i);
        }
    }
    std::cout<<"\n"<<res<<"\n";
    return 0;
}