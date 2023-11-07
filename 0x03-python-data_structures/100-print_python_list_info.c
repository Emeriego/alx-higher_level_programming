#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - is the main func
 * @p: ptr to object
 * Return: returns as specified
 */
void print_python_list_info(PyObject *p)
{
	int count;
	long int sz;
	
	sz = PyList_Size(p);
	printf("[*] size of the Python List = %ld\n", sz);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (count = 0; count < sz; count++)
	{
		printf("Element %d: %s\n", count, Py_TYPE(PyList_GetItem(p, count))->tp_name);
	}
}
