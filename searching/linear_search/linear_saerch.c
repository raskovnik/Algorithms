#include <stdio.h>
#define SIZE 7

int linear_search(int list[SIZE], int item) {
    int index = 0;
    int found = 0;

    while (index < SIZE && found == 0) {
        if (list[index] == item) {
            found = 1;
        } else {index++;}
    }
    return found;
}

int my_linear_search(int list[SIZE], int item) {
    for(int i; i < SIZE; i++) {
        if (list[i] == item) {return 1;}
    }
    return 0;
}
int main() {
    int a[SIZE] = {1,2, 3, 4, 5,6,7};
    int result = my_linear_search(a, 5);
    printf("%d\n", result);

}
