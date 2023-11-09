#include <stdio.h>
#include <stdlib.h>
struct Node
{
    int data;
    struct Node *next;
};
struct Queue
{
    struct Node *front;
    struct Node *rear;
};
struct Node *createNode(int data)
{
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    if (!newNode)
    {
        printf("Memory allocation failed\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}
struct Queue *createQueue()
{
    struct Queue *queue = (struct Queue *)malloc(sizeof(struct Queue));
    if (!queue)
    {
        printf("Memory allocation failed\n");
        exit(1);
    }
    queue->front = queue->rear = NULL;
    return queue;
}
int isEmpty(struct Queue *queue)
{
    return (queue->front == NULL);
}
void enqueue(struct Queue *queue, int data)
{
    struct Node *newNode =
        createNode(data);
    if (isEmpty(queue))
    {
        queue->front = queue->rear = newNode;
    }
    else
    {
        queue->rear->next = newNode;
        queue->rear = newNode;
    }
}
int dequeue(struct Queue *queue)
{
    if (isEmpty(queue))
    {
        printf("Queue is empty\n");
        exit(1);
    }
    int data = queue->front->data;
    struct Node *temp = queue->front;
    queue->front = queue->front->next;
    free(temp);
    return data;
}
void display(struct Queue *queue)
{
    if (isEmpty(queue))
    {
        printf("Queue is empty\n");
        return;
    }
    struct Node *current = queue->front;
    printf("Queue: ");
    while (current != NULL)
    {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}
int main()
{
    struct Queue *queue =
        createQueue();
    int choice, data;
    while (1)
    {
        printf("1.Enqueue  2.Dequeue    3.Display   4.Quit  Enter your choice: ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("Enter data to enqueue: ");
            scanf("%d", &data);
            enqueue(queue,
                    data);
            break;
        case 2:
            if (isEmpty(queue))
            {
                printf("Queue is empty\n");
            }
            else
            {
                printf("Dequeued element: %d\n", dequeue(queue));
            }
            break;
        case 3:
            display(queue);
            break;
        case 4:
            exit(0);
        default:
            printf("Invalid choice. Please try again.\n");
        }
    }
    return 0;
}