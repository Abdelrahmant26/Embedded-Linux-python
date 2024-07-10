#include <iostream>
#include <iomanip>
int main(){
    int i;
    std::cout<<"________________\n";
    std::cout<<"| char | ASCII |\n";
    std::cout<<"----------------\n";
    for(i =0; i<=255;i++){
        std::cout<<"|     "<<(char)i<<" |      "<<i<<" |\n";

    }
    return 0;
}