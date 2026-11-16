#include <iostream>
#include <Windows.h>
#include <string>
#include <sstream>

using namespace std;

int main()
{
	string input = "";
	
	int targetPID;
	while (true) {
		cout << "Enter target program's ID: ";
		getline(cin, input);

		stringstream myStream(input);
		if (myStream >> targetPID)
			break;
		cout << "NaN, please try again." << endl;
	}

	uintptr_t targetMemAdr;
	while (true) {
		cout << "Enter the memory address you want to target: ";
		getline(cin, input);

		stringstream myStream(input);
		if (myStream >> targetMemAdr)
			break;
		cout << "NaN, please try again." << endl;
	}

	int intRead = 0;

	HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, targetPID);
	if (hProcess == NULL) { // Failed to get a handle
		cout << "OpenProcess failed. GetLastError = " << dec << GetLastError() << endl;
		system("pause");
		return EXIT_FAILURE;
	}

	ReadProcessMemory(hProcess, (LPCVOID)targetMemAdr, &intRead, sizeof(int), NULL);
	cout << "Value of varInt:" << intRead;
}