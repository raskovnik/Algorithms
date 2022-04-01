#include <stdio.h>

int first_occurrence(int arr[], int target, int n) {
    int left = 0, right = n - 1, result = -1;

    while (left <= right) {
        int mid = (left + right) / 2;
        if (arr[mid] == target) {
            result = mid;
            right = mid - 1;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }

    }

    return result;
}

int last_occurrence(int arr[], int target, int n) {
    int left = 0, right = n - 1, result = -1;
    
    while (left <= right) {
        int mid = (left + right) / 2;

        if (arr[mid] == target) {
            result = mid;
            left = mid + 1;
        } else if (arr[mid] < target) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    return result;
}

int main() {
    int array[] = {2, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 7};
    int n = sizeof(array) / sizeof(array[0]);
    printf("%d\n", first_occurrence(array, 5, n));
    return 0;
}