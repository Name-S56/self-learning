#include<stdio.h>
int main()
{
	int n,m;//要求输入的两个数
	int i;	//循环用 
	int cnt=0;//计数 
	int sum=0;//和 
	scanf("%d %d",&m,&n);			//基础我还能错..scanf("", )少加逗号 
	
	if(m==1)
	m=2;//1不是素数,从二开始不影响 
	
	for(i=m;i<=n;i++){
			int k;//下面的循环用 
			int isPrime=1; //假定为素数
			for(k=2;k<i-1;k++){
			if(i%k==0) {
				isPrime=0;//除尽,不是素数 
				break;
				}
			}
		if(isPrime==1){
			cnt++;
			sum+=i;
		} 
	}
	printf("%d %d\n",cnt,sum); 
 return 0;
}
