/*
Q5) Menu Driven C Program to implement a circular queue using array 
*/

#include <stdio.h>
#include <stdlib.h>
#define MAX 5

int arr[MAX];
int front = 0;
int rear = 0;
int len=0;

void insert(int item);
void del();
void display();

int main()
{
    int choice, item;
    while (1)
    {
        printf("1.Insert, 2.Delete, 3.Display, 4.Quit,    Enter your choice : ");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1:
                printf("Input the element for adding in c-queue : ");
                scanf("%d", &item);
                insert(item);
                display();
                break;
            case 2:
                del();
                display();
                break;
            case 3:
                display();
                break;
            case 4:
                exit(1);
            default:
                puts("Wrong choice");
        }
    }
}

void insert(int item)
{
    if (front == rear && len>0)
    {
        puts("C-Queue Overflow");
        return;
    }
    arr[rear]=item;
    rear=(rear+1)%MAX;
    len++;
}

void del()
{
    if (rear == front && len==0)
    {
        puts("C-Queue Underflow");
        return;
    }
    front=(front+1)%MAX;
    len--;
}

void display()
{
    int i=front;
    if (front == rear && len==0)
        puts("C-Queue is empty");
    else{
	    printf("C-Queue is : ");
	    do{
	    	printf("%d ",arr[i]);
	    	i=(i+1)%MAX;
	    }while(i!=rear);
	    puts("\n");
	}	
}
