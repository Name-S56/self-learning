#include <iostream>
#include <iomanip> 
using namespace std;

int main() {
	int a, b;
	cin >> a >> b; 
	
	double sang = <double>(a) / b;
	int yu = a % b;
	
	printf("%0.2lf",sang);	
	cout<< " " << yu;
	
	return 0;
}
