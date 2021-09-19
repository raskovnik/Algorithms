#include <stdio.h>
#include <stdlib.h>

int comparator(const void * a, const void * b) {
    return (*(int*)a - *(int*)b);
}

void find_pair(int arr[], int n, int target) {
    qsort(arr, n, sizeof(int), comparator);

    int low = 0, high = n - 1;
    

    while (low < high) {
        if (arr[low] + arr[high] == target) {
            printf("Pair found: %d, %d\n", arr[low], arr[high]);
            return;
        }
        if (arr[low] + arr[high] < target) low++;
        else high--;
    }
    puts("Pair not found");
}

int main() {
    int arr[] = {3, 5, 2, 5, 6, 7, 7,4};
    int target = 10;
    int n = sizeof(arr) / sizeof(arr[0]);

    find_pair(arr, n, target);
}