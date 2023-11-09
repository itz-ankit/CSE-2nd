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

struct Node *treeify()
{
    int data;
    printf("Enter data (or -1 for NULL): ");
    scanf("%d", &data);

    if(data==-1)
    {
        return NULL;
    }
    else{
        struct Node* root = newNode(data);
        printf("Enter left child of %d\n", data);
        root->left = treeify();
        printf("Enter right child of %d\n", data);
        root->right = treeify();
        return root;
    }
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
    struct Node *root = treeify();

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