#include <Python.h>
/**
 * print_python_list_info - this displays basic info about Python lists.
 * @p: PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int sz, tp, count;
	PyObject *obj;

	sz = Py_SIZE(p);
	tp = ((PyListObject *)p)->allocated;
	printf("[*] size of the Python List = %d\n", sz);
	printf("[*] Allocated = %d\n", tp);
	for (count = 0; count < sz; count++)
	{
		printf("Element %d: ", count);
		obj = PyList_GetItem(p, count);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
