#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *left;
    struct Node *right;
};

struct Node* createNode(int data)
{
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

void preorderTrav(struct Node *curr)
{
    if (curr == NULL)
    {
        return;
    }
    printf("%d ", curr->data);
    preorderTrav(curr->left);
    preorderTrav(curr->right);
}

void inorderTrav(struct Node *curr)
{
    if (curr == NULL)
    {
        return;
    }
    inorderTrav(curr->left);
    printf("%d ", curr->data);
    inorderTrav(curr->right);
}

void postorderTrav(struct Node *curr)
{
    if (curr == NULL)
    {
        return;
    }
    postorderTrav(curr->left);
    postorderTrav(curr->right);
    printf("%d ", curr->data);
}

int main()
{
    struct Node *root = createNode(1);
    root->left = createNode(2);
    root->right = createNode(3);
    root->left->left = createNode(4);
    root->left->right = createNode(5);
    printf("preorder traversal of the binary tree: \n");
    preorderTrav(root);
    printf("\nInorder traversal of the binary tree: \n");
    inorderTrav(root);
    printf("\nPostorder traversal of the binary tree is: \n");
    postorderTrav(root);
    return 0;
}
