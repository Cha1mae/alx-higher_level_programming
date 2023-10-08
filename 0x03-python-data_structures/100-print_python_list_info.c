#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

/**
  * Trying to see if this is a correct 
  * Function to print information about a Python list
  *
**/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size_p, allocated, idx = 0;
	PyObject *l;

	size_p = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size_p);
	printf("[*] Allocated = %ld\n", allocated);
	while (idx < size_p)
	{
		l = PyList_GetItem(p, idx);
		printf("Element %ld: %s\n", idx, Py_TYPE(l)->tp_name);
		idx++;
	}
}

int main(void)
{
	PyObject *list;

	Py_Initialize();

	list = PyList_New(0);

	printf("Printing information about an empty list:\n");
	print_python_list_info(list);


	PyList_Append(list, PyLong_FromLong(42));
	PyList_Append(list, PyUnicode_DecodeUTF8("Hello", 5, NULL));
	PyList_Append(list, PyUnicode_DecodeUTF8("World", 5, NULL));

	printf("\nPrinting information about a list with elements:\n");
	print_python_list_info(list);

	Py_XDECREF(list);
	Py_Finalize();

    return 0;
}
