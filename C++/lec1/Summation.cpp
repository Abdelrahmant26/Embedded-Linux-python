#include <iostream>
#include <iomanip>
#include <string.h>
#include <math.h>
int main(){
    std::string input;
    std::cout<<"Enter integer numbers separated by space: \n";
    //std::cin>>input;
    getline(std::cin, input);
    int A=0;
    std::cout<<input.length()<<"\n";
    for(int i = 0; i<input.length(); i++){
        std::cout<<"iteration : "<<input[i]<<"\n";
        if(input[i] < 58 && input[i] > 47){
            std::cout<<"1\n";
            A+=input[i]-'0';
        }
        std::cout<<"\n\n";
    }
    std::cout<<A;
    return 0;
}