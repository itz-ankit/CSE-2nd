#include<stdio.h>
#define MAX_SIZE 10

void quicksort(int arr[MAX_SIZE],int first,int last){
   int i, j, p, temp;
   if(first<last){
      p=first;
      i=first;
      j=last;
      while(i<j){
         while(arr[i]<=arr[p]&&i<last)
         i++;
         while(arr[j]>arr[p])
         j--;
         if(i<j){
            temp=arr[i];
            arr[i]=arr[j];
            arr[j]=temp;
         }
      }
      temp=arr[p];
      arr[p]=arr[j];
      arr[j]=temp;
      quicksort(arr,first,j-1);
      quicksort(arr,j+1,last);
   }
}
int main(){
   int n, arr[MAX_SIZE];
   printf("Enter your number of elements: ");
   	scanf("%d",&n);
   printf("Enter %d elements: ", n);
   for(int i=0;i<n;i++)
   	scanf("%d",&arr[i]);
   quicksort(arr,0,n-1);
   printf("Sorted array: ");
   for(int i=0;i<n;i++)
  	 printf(" %d",arr[i]);
   return 0;
}
