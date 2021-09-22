#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return *(int*)a - *(int*)b;
}

void find_max(int arr[], int n) {
    qsort(arr, n, sizeof(int), compare);

    (arr[0] * arr[1]) > (arr[n - 1] * arr[n - 2])?printf("The pair is %d and %d\n", arr[0], arr[1]): printf("The pair is %d and %d\n", arr[n - 1], arr[n - 2]);
}

int main() {
    int arr[]  = {-10, -3, 6, 5, -20};
    int n = sizeof(arr) / sizeof(arr[0]);

    find_max(arr, n);
}