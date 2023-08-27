/*
Q3) Solve the tower of hanoi problem using recursion
*/

#include <stdio.h>

void toH(int n, char beg, char end, char aux)
{
	if (n == 1)
	{
		printf("\n Move disk 1 from rod %c to rod %c",beg ,end );
		return;
	}
	toH(n-1, beg, aux, end);
	printf("\n Move disk %d from rod %c to rod %c", n, beg, end);
	toH(n-1, aux, end, beg);
}

int main()
{
	int num;
	printf("Enter number of disks: ");
	scanf("%d", &num);
	toH(num, 'A','C','B'); 
	return 0;
}
