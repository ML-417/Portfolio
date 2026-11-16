#include <iostream>
#include <Windows.h>

int main()
{
    int varInt = 123456;
    std::string varString = "DefaultString";
    char arrChar[128] = "Long char array right there ->";

    int* ptr2int = &varInt;
    int** ptr2ptr = &ptr2int;
    int*** ptr2ptr2 = &ptr2ptr;
    while(true){
        std::cout << "Process ID:" << GetCurrentProcessId() << "\n";

        std::cout << "varInt(0x" << &varInt << ") = " << varInt << "\n";
        std::cout << "varString(0x" << &varString << ") = " << varString << "\n";
        std::cout << "arrChar(0x" << &arrChar << ") = " << arrChar << "\n";

        std::cout << "ptr2int(0x" << &ptr2int << ") = " << ptr2int << "\n";
        std::cout << "ptr2ptr(0x" << &ptr2ptr << ") = " << ptr2ptr << "\n";
        std::cout << "ptr2ptr2(0x" << &ptr2ptr2 << ") = " << ptr2ptr2 << "\n";

        std::cout << "Press ENTER to print again. \n";
        system("pause > nul");
    
        for (int i = 64; i > 0; i--) {
            std::cout << "-";
        }
        std::cout << "\n";
    }
    return EXIT_SUCCESS;
}