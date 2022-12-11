#include<stdio.h>
void pao(int b[]);
int main()
{
	int a[10],i;
	printf("请输入10个数:\n");
	for(i=0;i<10;i++) 
		scanf("%d",&a[i]);
	printf("前\n");
	for(i=0;i<10;i++)
		printf("%5d",a[i]);
	pao(a);
		printf("\n后\n");
	for(i=0;i<10;i++)
		printf("%5d",a[i]);
		
 return 0;
}
void pao(int b[])
{
	int i,j,t;
	for(i=1;i<10;i++)
	for(j=0;j<10-i;j++)
	if(b[j]>b[j+1])
	{
		t=b[j];
	b[j]=b[j+1];
	b[j+1]=t;
	}
}

