#include <stdio.h>
#include <stdlib.h>
struct Node
{
    int data;
    struct Node *prev;
    struct Node *next;
};

struct Node *getTail(struct Node *head)
{
    if (head == NULL)
        return head;
    struct Node *temp = head;
    while (temp->next != NULL)
        temp = temp->next;
    return temp;
}

struct Node *getIndex(struct Node *head, int x)
{
    struct Node *temp = head;
    int i;
    for (int i = 0; i != x; i++)
        temp = temp->next;
    return temp;
}

struct Node *insertBeg(struct Node *head, int num)
{
    struct Node *temp = malloc(sizeof(struct Node));
    temp->data = num;
    temp->prev = NULL;
    temp->next = head;
    if (head != NULL)
        head->prev = temp;
    return temp;
}

struct Node *insertEnd(struct Node *head, int num)
{
    if (head == NULL)
        return insertBeg(head, num);
    struct Node *temp = malloc(sizeof(struct Node));
    struct Node *tail = getTail(head);
    temp->data = num;
    tail->next = temp;
    temp->prev = tail;
    temp->next = NULL;
    return head;
}

struct Node *insertMid(struct Node *head, int num, int x)
{
    if (x == 0)
        return insertBeg(head, num);
    struct Node *temp = malloc(sizeof(struct Node));
    struct Node *node = getIndex(head, x);
    temp->data = num;
    node->prev->next = temp;
    temp->prev = node->prev;
    temp->next = node;
    node->prev = temp;
    return head;
}

struct Node *deleteBeg(struct Node *head)
{
    if (head == NULL)
        return head;
    struct Node *temp = head->next;
    if (temp != NULL)
        temp->prev = NULL;
    free(head);
    return temp;
}

struct Node *deleteEnd(struct Node *head)
{
    if (head == NULL)
        return head;
    struct Node *tail = getTail(head);
    if (tail->prev == NULL)
    {
        tail = NULL;
        return tail;
    }
    tail->prev->next = NULL;
    free(tail);
    return head;
}

struct Node *deleteMid(struct Node *head, int x)
{
    if (x == 0)
        return deleteBeg(head);
    struct Node *node = getIndex(head, x);
    if (node->next == NULL)
        return deleteEnd(head);
    node->prev->next = node->next;
    node->next->prev = node->prev;
    free(node);
    return head;
}

struct Node *create(int x)
{
    struct Node *head = NULL;
    int i;
    for (i = 1; i <= x; i++)
        head = insertEnd(head, i);
    return head;
}

void display(struct Node *head)
{
    struct Node *temp = head;
    puts("The Linked List:");
    while (temp != NULL)
    {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    puts("");
}

int main()
{
    struct Node *head = malloc(sizeof(struct Node));
    int num, x, c;
    puts("Enter how many numbers you want to insert into the initial linked list");
    scanf("%d", &num);
    head = create(num);
    display(head);
    while (1)
    {
        puts("Enter 0 to display,1 to insert at front,2 to insert at end,3 to insert at middle,");
        puts("4 to delete at front,5 to delete at end,6 to delete at middle,");
        puts("Enter anything else to exit.");
        scanf("%d", &c);
        switch (c)
        {
        case 1:
            puts("Enter the number to insert :");
            scanf("%d", &num);
            head = insertBeg(head, num);
            display(head);
            break;
        case 2:
            puts("Enter the number to insert :");
            scanf("%d", &num);
            head = insertEnd(head, num);
            display(head);
            break;
        case 3:
            puts("Enter the number to insert :");
            scanf("%d", &num);
            puts("Enter the index to insert :");
            scanf("%d", &x);
            head = insertMid(head, num, x);
            display(head);
            break;
        case 4:
            head = deleteBeg(head);
            display(head);
            break;
        case 5:
            head = deleteEnd(head);
            display(head);
            break;
            break;
        case 6:
            puts("Enter index to delete :");
            scanf("%d", &x);
            head = deleteMid(head, x);
            display(head);
            break;
            break;
        case 0:
            display(head);
            break;
        default:
            puts("Exited successfully");
            return (0);
        }
    }
}