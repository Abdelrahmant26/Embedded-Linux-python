#include <iostream>
#include <iomanip>
#include <string.h>
#include <math.h>
int main(){
    std::string a,b,c;
    std::cout<<"Enter 3 numbers : \n";
    std::cin>>a>>b>>c;
    //std::cout<<a<<"\n"<<b<<"\n"<<c<<"\n";
    //std::cout<<a.length()<<"\n"<<b.length()<<"\n"<<c.length()<<"\n";
    int A=0,B=0,C=0;
    for(int i=0;i<a.length();i++){
        //std::cout<<a.length()<<"\n";
        //std::cout<<a[i]<<"\n";
        //std::cout<<(a[i]-'0')*pow(10,a.length()-1-i)<<"\n";
        A+=(a[i]-'0')*pow(10,a.length()-1-i);
    }
    for(int i=0;i<b.length();i++){
        B+=(b[i]-'0')*pow(10,b.length()-1-i);
    }
    for(int i=0;i<c.length();i++){
        C+=(c[i]-'0')*pow(10,c.length()-1-i);
    }
    //std::cout<<A<<"\n"<<B<<"\n"<<C;
    if(A<B){
        if(B>C){
            std::cout<<B;
        }
        else if(C>=B){
            std::cout<<C;
        }
    }
    else if(A>B){
        if(A>C){
            std::cout<<A;
        }
        else if(C>=A){
            std::cout<<C;
        }
    }
    else{
        if(C>A){
            std::cout<<C;
        }
        else{
            std::cout<<A;
        }
    }

    return 0;
}