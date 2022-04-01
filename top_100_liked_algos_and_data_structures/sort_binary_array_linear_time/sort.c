#include <stdio.h>

void sort(int arr[], int n) {
    int k = 0;
    for (int i=0; i<n; i++) {
        if (arr[i] == 0) {
            arr[k] = 0;
            k++;
        }
    }

    for (int i=k; i<n; i++) {
        arr[i] = 1;
    }

    for (int i=0; i < n; i++) {
        printf(" %d ", arr[i]);
    }
    printf("\n");
}

void main() {
    int arr[] = {1, 0, 1, 1,1, 0, 0, 0, 0, 1, 1, 0, 1, 0};
    int n = sizeof(arr) / sizeof(arr[0]);
    sort(arr, n);
}