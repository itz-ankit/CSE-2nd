/*
Q2) Implementation of a Stack using an Array in C with the following features:
    -> Push element
    -> Pop element
    -> Peek element
*/
#include <stdio.h>
#define MAX 50 // Maximum number of elements that can be stored

int top = -1, stack[MAX];
void push();
void pop();
void display();

void main()
{
    int choice;

    while (1)
    {
        printf("\n\nStack Menu: Which operation do you want to perform?");
        printf("\n1.Push\n2.Pop\n3.Display\n4.Exit");
        printf("\nEnter your choice(1-4): ");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1:
                push();
                break;
            case 2:
                pop();
                break;
            case 3:
                display();
                break;
            case 4:
                exit(0);

            default:
                printf("\nWrong Choice.");
        }
    }
}

void push()
{
    int val;

    if (top == MAX - 1)
    {
        printf("\nStack is full. ");
    }
    else
    {
        printf("\nEnter element to push: ");
        scanf("%d", &val);
        top = top + 1;
        stack[top] = val;
    }
}

void pop()
{
    if (top == -1)
    {
        printf("\nStack is Empty.");
    }
    else
    {
        printf("\nDeleted element is %d", stack[top]);
        top = top - 1;
    }
}

void display()
{
    int i;

    if (top == -1)
    {
        printf("\nStack is Empty.");
    }
    else
    {
        printf("\nStack is : \n");
        for (i = top; i >= 0; --i)
        {
            printf("%d\n", stack[i]);
        }
    }
}
