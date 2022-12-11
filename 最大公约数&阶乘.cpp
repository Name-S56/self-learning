#include <stdio.h>
int fact(int);
int main()
{
	int a,b;
	int t;
	scanf("%d %d", &a, &b);
	int origa = a;
	int origb = b;
	while ( b != 0 ) {
		t = a%b;
		a = b;
		b = t;
	}
	printf("%d和%d的最大公约数是%d.\n", origa, origb, a);
	return 0;
}

int fact(int x)
{
	int fact=1;
	for (int i=2;i<=x;i++)
		{fact*=i;
		}
	return fact;
}
