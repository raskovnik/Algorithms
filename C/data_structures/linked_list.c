#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>

struct Node {
    int data;
    struct Node* link;

};

struct Node* head;

void insert(int x) {
    struct Node* temp = (struct Node*)malloc(sizeof(struct Node*));
    temp -> data = x;
    temp -> link = head;
    head = temp;
}

void print() {
    struct Node* temp = head;
    printf("List is: ");
    while (temp != NULL) {
        printf(" %d", temp -> data);
        temp = temp -> link;
    }

    printf("\n");
}

int main() {
    head = NULL;
    printf("Input number of numbers:\n");
    int n, i, x;
    scanf("%d", &n);
    for (i = 0; i<n; i++) {
        printf("Enter the number: \n");
        scanf("%d", &x);
        insert(x);
        print();
    }
} 