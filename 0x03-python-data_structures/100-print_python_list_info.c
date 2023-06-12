#include "lists.h"

/**
 * print_python_list_info – lists to be printed
 * @p: an object list
 */
void print_python_list_info(PyObject *p)
{
	int size_node, allocation_memory, initial;
	PyObject *object_check;

	size_node = Py_SIZE(p);
	allocation_memory = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size_node);
	printf("[*] Allocated = %d\n", allocation_memory);

	for (initial = 0; initial < size_node; initial++)
	{
		printf("Element %d: ", initial);

		obj_check = PyList_GetItem(p, initial);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}

