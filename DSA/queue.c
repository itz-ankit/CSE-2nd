/* 
Q4) Menu Driven C Program to implement queue using array 
*/

#include <stdio.h>
#include <stdlib.h>
#define MAX 20

int queue_arr[MAX];
int rear = -1;
int front = -1;

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
            printf("Input the element for adding in queue : ");
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
            printf("Wrong choice\n");
        }
    }

    return 0;
}

void insert(int item)
{
    if (rear == MAX - 1)
    {
        printf("Queue Overflow\n");
        return;
    }
    if (front == -1)
        front = 0;
    rear = rear + 1;
    queue_arr[rear] = item;
}

void del()
{
    int item;
    if (front == -1 || front == rear + 1)
    {
        printf("Queue Underflow\n");
        return;
    }
    item = queue_arr[front];
    front = front + 1;
    return;
}

void display()
{
    int i;
    if (front == -1 || front == rear + 1)
    {
        printf("Queue is empty\n");
        return;
    }
    printf("Queue is : ");
    for (i = front; i <= rear; i++)
        printf("%d  ", queue_arr[i]);
    puts("\n");
}