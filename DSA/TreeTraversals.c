#include <stdlib.h>
#include <stdio.h>

struct Node
{
    struct Node *left;
    struct Node *right;
    int data;
};

struct Node *newNode(int data)
{
    if (data == -1)
        return NULL;
    struct Node *node = (struct Node *)malloc(sizeof(struct Node));
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return node;
}

struct Node *treeify(int arr[], int size, int i)
{
    // left=i*2+1
    // right=i*2+2
    struct Node *currNode = newNode(arr[i]);
    if (i * 2 + 1 < size)
        currNode->left = treeify(arr, size, i * 2 + 1);
    if (i * 2 + 2 < size)
        currNode->right = treeify(arr, size, i * 2 + 2);
    return currNode;
}


void inOrder(struct Node *root)
{
    if (root != NULL)
    {
        inOrder(root->left);
        printf("%d ", root->data);
        inOrder(root->right);
    }
}

void preOrder(struct Node *root)
{
    if (root != NULL)
    {
        printf("%d ", root->data);
        preOrder(root->left);
        preOrder(root->right);
    }
}

void postOrder(struct Node *root)
{
    if (root != NULL)
    {
        postOrder(root->left);
        postOrder(root->right);
        printf("%d ", root->data);
    }
}

void printArray(int arr[], int size)
{
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main()
{
    int n, i;

    puts("Enter size of array:");
    scanf("%d", &n);

    int *arr = malloc(sizeof(int) * n);
    puts("Enter elements array:(-1 for empty node)");

    for (i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    printf("Original array: ");
    printArray(arr, n);

    struct Node *root = treeify(arr, n, 0);

    // traversals

    printf("IN ORDER TRAVERSAL: ");
    inOrder(root);
    printf("\n");

    printf("PRE ORDER TRAVERSAL: ");
    preOrder(root);
    printf("\n");

    printf("POST ORDER TRAVERSAL: ");
    postOrder(root);
    printf("\n");

    return 0;
}