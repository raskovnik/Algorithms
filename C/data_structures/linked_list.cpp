#include <cstddef>

struct Node {
    int data;
    Node* link;

};

int main() {
    Node* A;
    A = NULL;

    Node* temp = new Node();
    temp -> data = 2;
    temp -> link = NULL;

    A = temp;
}