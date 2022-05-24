typedef struct node{
    int data;
    struct node * next;
} node;

void print_list(node * head);
node * create_node(int data, node * next);
void append_node(node * head, int data);
void insert_node(node * head, int index, int data);
void delete_node(node * head, int data);
void free_list(node * head);