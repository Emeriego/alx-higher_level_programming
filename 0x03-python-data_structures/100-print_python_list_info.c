#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - is the main func
 * @p: ptr to object
 * Return: returns as specified
 */
void print_python_list_info(PyObject *p)
{
	int c;
	long int sz;

	sz = PyList_Size(p);
	printf("[*] size of the Python List = %ld\n", sz);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (c = 0; c < sz; c++)
	{
		printf("Element %d: %s\n", c, Py_TYPE(PyList_GetItem(p, c))->tp_name);
	}
}
