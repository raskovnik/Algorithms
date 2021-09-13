#include <stdio.h>

void swap(int index1, int index2, int array[]) {
    int temp_holder = array[index2];
    array[index2] = array[index1];
    array[index1] = temp_holder;
}

int insertion_sort(int N, int list[N]) {
    for (size_t i = 1; i <= N; ++i){
        int value_to_sort = list[i];

        while (list[i - 1] > value_to_sort && i > 0) {
            swap(i, i-1, list);
            i = i - 1;
        }
    }

    for (size_t i = 0; i < N; ++i) {
        printf("%d ", list[i]);
    }
}


int main() {
    int list[15] = {5,6,5,1,5,7,8,1,2,4,6,7,8,9,0};
    int length = sizeof(list) / sizeof(list[0]);
    insertion_sort(length, list);
}