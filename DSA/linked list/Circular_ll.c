#include <stdio.h>
#include <malloc.h>
struct Node
{
	int data;
	struct Node *next;
};
struct Node *head = NULL;
// Creation of  the circular linked list
struct Node *create(struct Node *head)
{
	struct Node *new_node, *ptr;
	int value;
	printf("\n-1 to the end\n");
	printf("Enter the data: ");
	scanf("%d", &value);
	while (value != -1)
	{
		new_node = (struct Node *)malloc(sizeof(struct Node));
		new_node->data = value;
		if (head == NULL)
		{
			new_node->next = new_node;
			head = new_node;
		}
		else
		{
			ptr = head;
			while (ptr->next != head)
			{
				ptr = ptr->next;
			}
			ptr->next = new_node;
			new_node->next = head;
		}
		printf("Enter the data: ");
		scanf("%d", &value);
	}
	return head;
}

// Insert at the beginning of the linked list
struct Node *insertAtBeg(struct Node *head)
{
	struct Node *new_node = malloc(sizeof(struct Node));
	int value;
	printf("Enter the value of the Node: ");
	scanf("%d", &value);

	new_node->data = value;
	struct Node *ptr = head;
	while (ptr->next != head)
	{
		ptr = ptr->next;
	}
	ptr->next = new_node;
	new_node->next = head;
	head = new_node;
	return head;
}

// Insert at the last of the linked list
struct Node *insertAtEnd(struct Node *head)
{
	struct Node *new_node = malloc(sizeof(struct Node));
	int value;
	printf("Enter the value of the Node: ");
	scanf("%d", &value);
	new_node->data = value;

	struct Node *ptr = head;
	while (ptr->next != head)
	{
		ptr = ptr->next;
	}
	ptr->next = new_node;
	new_node->next = head;
	return head;
}

// Delete at the begining
struct Node *deleteAtBeg(struct Node *head)
{
	struct Node *ptr = head;
	while (ptr->next != head)
	{
		ptr = ptr->next;
	}
	ptr->next = head->next;
	free(head);
	head = ptr->next;
	return head;
}

// delete at the end

struct Node *deleteAtEnd(struct Node *head)
{
	struct Node *ptr, *preptr;
	while (ptr->next != head)
	{
		preptr = ptr;
		ptr = ptr->next;
	}
	preptr->next = ptr->next;
	free(ptr);
	return head;
}

// Display the linked list
struct Node *display(struct Node *head)
{
	struct Node *ptr;
	ptr = head;
	while (ptr->next != head)
	{
		printf("\t %d", ptr->data);
		ptr = ptr->next;
	}
	printf("\t %d", ptr->data);
	return head;
}
int main()
{
	int choice;

	do
	{
		printf("\nEnter the choice: (1)create a circular linked list (2)Insert at the begining (3)Insert at the end (4)Delete at the begining (5)Delete at the end  (6)Display ");
		scanf("%d", &choice);
		switch (choice)
		{
		case 1:
			head = create(head);
			printf("Circular linked list created\n");
			break;

		case 2:
			head = insertAtBeg(head);
			break;
		case 3:
			head = insertAtEnd(head);
			break;
		case 4:
			head = deleteAtBeg(head);
			break;
		case 5:
			head = deleteAtEnd(head);
			break;
		case 6:
			head = display(head);
			break;
		}
	} while (choice != 7);
	return 0;
}
