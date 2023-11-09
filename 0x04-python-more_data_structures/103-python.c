#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - func gets bytes ls_size of py
 * @p: Object in view
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t ls_size = 0, i = 0;
	char *my_st;

	my_st = NULL;
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	if (PyBytes_Asmy_stAndSize(p, &my_st, &ls_size) != -1)
	{
		printf("  ls_size: %zd\n", ls_size);
		printf("  trying my_st: %s\n", my_st);
		printf("  first %zd bytes:", ls_size < 10 ? ls_size + 1 : 10);
		while (i < ls_size + 1 && i < 10)
		{
			printf(" %02hhx", my_st[i]);
			i++;
		}
		printf("\n");
	}
}

/**
 * print_python_list - gives data of the PyListObject
 *
 * @p: the PyObject
 */

void print_python_list(PyObject *p)
{
	PyObject *item;
	Py_ssize_t ls_size = 0;
	int i = 0;

	if (PyList_CheckExact(p))
	{
		ls_size = PyList_Size(p);

		printf("[*] Python list info\n");
		printf("[*] ls_size of the Python List = %zd\n", ls_size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		while (i < ls_size)
		{
			item = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			i++;
		}
	}
}
