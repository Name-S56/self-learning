#include<stdio.h>
int main()
{
	int n,m;//Ҫ�������������
	int i;	//ѭ���� 
	int cnt=0;//���� 
	int sum=0;//�� 
	scanf("%d %d",&m,&n);			//�����һ��ܴ�..scanf("", )�ټӶ��� 
	
	if(m==1)
	m=2;//1��������,�Ӷ���ʼ��Ӱ�� 
	
	for(i=m;i<=n;i++){
			int k;//�����ѭ���� 
			int isPrime=1; //�ٶ�Ϊ����
			for(k=2;k<i-1;k++){
			if(i%k==0) {
				isPrime=0;//����,�������� 
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
