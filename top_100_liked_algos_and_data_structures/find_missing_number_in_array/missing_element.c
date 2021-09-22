#include <stdio.h>

int missing_element(int list[], int n) {

    int total = 0;
    for (int i = 0; i < n; i++) {total += list[i];}
    return (n + 1) + n *(n + 1) / 2 - total;

}

int main() {
    int list[] = {3, 4, 2, 5, 6};
    int n = sizeof(list)/sizeof(list[0]);
    printf("The missing element is %d\n",missing_element(list, n) );
}