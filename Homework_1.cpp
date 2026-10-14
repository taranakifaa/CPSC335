
#include <iostream> // Input/output library
#include <algorithm> // Algorithm library
using namespace std; // Standard namespace

class Linklist_1 { // Define linked list nodes
    int sort; // Store node value
    List1* next; // Next node for list 1
    List2* next; // Next node for list 2
};

int main() { // Main function

    // Configure linked list 1
    List1* a = List_1{1, nullptr}; // Node 1
    List1* b = List_1{3, nullptr}; // Node 3
    List1* c = List_1{5, nullptr}; // Node 5

    // Configure linked list 2
    List2* d = List_2{2, nullptr}; // Node 2
    List2* e = List_2{4, nullptr}; // Node 4
    List2* f = List_2{6, nullptr}; // Node 6

    a->next = b; // Connect 1 -> 3
    b->next = c; // Connect 3 -> 5

    d->next = e; // Connect 2 -> 4
    e->next = f; // Connect 4 -> 6

    List1* current_1 = a; // Start at list 1
    List2* current_2 = d; // Start at list 2

    temp_1 = nullptr; // Temporary pointer for list 1
    temp_2 = nullptr; // Temporary pointer for list 2

    merged_head = nullptr; // First node of merged list
    merged_tail = nullptr; // Last node of merged list

    // Traverse both linked lists
    for (; current_1 != nullptr && current_2 != nullptr; ) {

        if (current_1->sort < current_2->sort) { // Compare values

            temp_1 = current_1->next; // Save next node

            if (merged_head == nullptr) { // Check if merged list is empty
                merged_head = current_1; // Set first node
            }
            else {
                merged_tail->next = current_1; // Connect selected node
            }

            merged_tail = current_1; // Update last node
            current_1 = temp_1; // Advance list 1
        }
        else {

            temp_2 = current_2->next; // Save next node

            if (merged_head == nullptr) { // Check if merged list is empty
                merged_head = current_2; // Set first node
            }
            else {
                merged_tail->next = current_2; // Connect selected node
            }

            merged_tail = current_2; // Update last node
            current_2 = temp_2; // Advance list 2
        }
    }

    // Connect remaining nodes after the loop
    if (current_1 != nullptr) {
        merged_tail->next = current_1; // Attach remaining list 1
    }
    else if (current_2 != nullptr) {
        merged_tail->next = current_2; // Attach remaining list 2
    }

    return 0; // End program
}
