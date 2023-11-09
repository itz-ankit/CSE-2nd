#include <stdio.h>
#define MAX_SIZE 10
void insertionSort(int arr[MAX_SIZE], int n)
{
    int i, key, j;
    for (i = 1; i < n; i++)
    {
        key = arr[i];
        j = i - 1;

        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}
void selectionSort(int arr[MAX_SIZE], int n) {
    int i, j, minIndex, temp;
    
    for (i = 0; i < n - 1; i++) {
        
        minIndex = i;
        for (j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        
        temp = arr[minIndex];
        arr[minIndex] = arr[i];
        arr[i] = temp;
    }
}
void BubbleSort(int arr[MAX_SIZE], int n)
{
	for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main()
{
    int n, arr[MAX_SIZE];
    printf("Enter the size of the array: ");
    scanf("%d", &n);
    printf("Enter the elemnts of the array: ");
    for (int i = 0; i < n; ++i)
    {
        scanf("%d", &arr[i]);
    }
    printf("Original array: \n");
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }
    int choice;
    printf("\nEnter your choice: (1) for Selection Sort (2) for Insertion Sort and (3) for Bubble Sort: \n");
    scanf("%d", &choice);
	switch(choice)
    {
    	case 1:
			insertionSort(arr, n);
			break;
		case 2:
			selectionSort(arr, n);
			break;
		case 3:
			BubbleSort(arr, n);
			break;
		default:
			printf("Invalid choice");
			return(0);	  
    }
    printf("\nSorted array: \n");
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }

    return 0;
}
