#include <bits/stdc++.h>
using namespace std;
int main()
{
	int A;
	char B;
	double C;
	string S;
	cin>>S;
	for(int i=0;i<S.length();i++){
		if(S[i]=='+'||
			S[i]=='-'|
			S[i]=='*'|
			S[i]=='/'|){
			A = i;
		}
	}
	for(int i=0;i<A;i++){
		cout<<S[i];
	}
	return 0;
}
