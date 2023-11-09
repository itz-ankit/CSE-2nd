#include <stdio.h>
#include <stdlib.h>
struct Node
{
    int data;
    struct Node *next;
};
// Initialize the top of the stack struct
struct Node *top = NULL;
// Function to push an element onto the stack void
void push(int value)
{
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    if (newNode == NULL)
    {
        printf("Stack overflow!\n");
        return;
    }
    newNode->data = value;
    newNode->next = top;
    top = newNode;
    printf("%d pushed onto the stack.\n", value);
}
// Function to pop an element from the stack
void pop()
{
    if (top == NULL)
    {
        printf("Stack Underflow!\n");
        return;
    }
    struct Node *temp = top;
    top = top->next;
    int
        poppedValue = temp->data;
    free(temp);
    printf("%d popped from the stack.\n", poppedValue);
}
// Function to display the elements of the stack void
void display()
{
    struct Node *current =
        top;
    if (current == NULL)
    {
        printf("Stack Underflow!\n");
        return;
    }
    printf("Stack elements: ");
    while (current != NULL)
    {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}
void main()
{
    int choice, value;
    while (1)
    {
        printf("\nStack Operations: 1.Push  2.Pop   3.Display   4.Exit  Enter your choice: ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("Enter the value to push onto the stack: ");
            scanf("%d", &value);
            push(value);
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
            printf("Invalid choice. Please enter a valid option.\n");
        }
    }
}