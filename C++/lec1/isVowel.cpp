#include <iostream>
#include <iomanip>
#include <string.h>
#include <math.h>
int main(){
    char c;
    std::cout<<"Enter 1 letter : \n";
    std::cin>>c;
    if (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U' \
    || c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') std::cout<<"is vowel \n";
    else std::cout<<"not vowel !\n";
    return 0;
}