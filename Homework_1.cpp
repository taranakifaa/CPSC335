#include <iostream>
#include <algorithm>
using namespace std;

class Linklist_1 {
 int sort;
 Node* next; // defining our linked list 1
};

class Linklist_2 {
  int sort;
Node* next; // defining our linked list 2
};

int main() {
  // Connecting our  nodes (let's say we have three values in linked list 1 and 2)
    Linklist_1* a = Linklist_1{1, nullptr};
    Linklist_1* b = Linklist_1{3, nullptr};
    Linklist_1* c = Linklist_1{5, nullptr};

    Linklist_2* d = Linklist_1{2, nullptr};
    Linklist_2* e = Linklist_1{4, nullptr};
    Linklist_2* f = Linklist_1{6, nullptr};

  //defining Linked list 1 sequence 
    a->next = b;
    b->next = c;

  //defining Linked list 2 sequence
    d->next = e;
    e->next = f;

  Node* current_1 = a; // start at link list 1
  Node* current_2 = d; // start at link list 2
  
  for(Node* current_1 = a; current_1 != nullptr; current_1 = current_1->next && Node* current_2 = d; current_2 != nullptr; current_2 = current_2->next){
  if(Node* current_1 < Node* current_2){
    
  }
    
  }
  
}
