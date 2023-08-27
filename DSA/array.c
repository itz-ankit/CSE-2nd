/*
Q1) Implementation of an Array using a Menu-Driven C program with the following features:
    -> Insert element,
    -> Delete element,
    -> Display element.
*/
#include <stdio.h>

void display(int arr[100], int size)
{
    for (int i = 0; i < size; i++)
    {
        printf("%d ", arr[i]);
    }
}

void insert(int arr[100], int size)
{
    int pos, value;
    printf("Enter the position: ");
    scanf("%d", &pos);
    printf("Enter the value: ");
    scanf("%d", &value);
    for (int i = size - 1; i >= pos - 1; i--)
    {
        arr[i + 1] = arr[i];
    }
    arr[pos - 1] = value;
    size++;
    display(arr, size);
}

void deletion(int arr[100], int size)
{
    int pos;
    printf("Enter the position: ");
    scanf("%d", &pos);
    for (int i = pos - 1; i < size - 1; i++)
    {
        arr[i] = arr[i + 1];
    }
    size--;

    display(arr, size);
}

int main()
{
    int size;
    printf("Enter the size of array: ");
    scanf("%d", &size);
    int arr[100];
    printf("Enter the elements of the array: ");
    for (int i = 0; i < size; i++)
    {
        scanf("%d", &arr[i]);
    }
    int choice;
    while (1)
    {

        printf("\nSelect operaton: 1.Insert 2. Delete 3.Display 4.Exit :\n");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            insert(arr, size);
            size++;
            break;
        case 2:
            deletion(arr, size);
            size--;
            break;
        case 3:
            display(arr, size);
            break;
        case 4:
            exit(0);
            printf("Exit successfully");
            break;
        }
    }
}
