from linked_list import LinkedList

my_linked_list = LinkedList()

my_linked_list.insert_node(9)
my_linked_list.insert_node(3)
my_linked_list.insert_node(6)
my_linked_list.insert_node(15)

my_linked_list.print_elements()


print(my_linked_list.delete_node(15))

my_linked_list.print_elements()
