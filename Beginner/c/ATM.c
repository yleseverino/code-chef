#include<stdio.h>

int main()
{
	int retirada;
	float conta,conta_real;

	scanf("%d %f",&retirada,&conta);
	
	conta_real = conta;

	if (retirada < (conta_real-0.5) && retirada % 5 == 0)
	{
		conta_real = conta_real - retirada - 0.5;
	}


	printf("%f\n",conta_real);





}

