from linked_list import LinkedList

my_linked_list = LinkedList()

my_linked_list.insert_node(9)
my_linked_list.insert_node(3)
my_linked_list.insert_node(6)

print(my_linked_list.head.next.next.value)

