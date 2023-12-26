#include<bits/stdc++.h>
#include <windows.h>
#define INF 0x3f3f3f3f
using namespace std;
int main(){
	HWND hWnd = GetConsoleWindow();
	ShowWindow(hWnd, SW_HIDE);
	system("powershell ./launch.ps1");
	// system("pause");
	return 0;
}
