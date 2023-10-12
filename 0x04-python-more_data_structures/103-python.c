#include <Python.h>
#include <stdio.h>

/**
 * print_python_list -
 * @p: -
*/

void print_python_list(PyObject *p) {
    int i;
    PyObject *item;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < PyList_Size(p); i++) {
        item = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
        
        if (PyBytes_Check(item)) {
            printf("[.] bytes object info\n");
            printf("  size: %ld\n", PyBytes_Size(item));
            printf("  trying string: %s\n", PyBytes_AsString(item));
            printf("  first %ld bytes: ", PyBytes_Size(item) < 10 ? PyBytes_Size(item) : 10);
            for (int j = 0; j < PyBytes_Size(item) && j < 10; j++) {
                printf("%02x ", (unsigned char)PyBytes_AsString(item)[j]);
            }
            printf("\n");
        }
        else if (!PyUnicode_Check(item) && !PyFloat_Check(item) && !PyList_Check(item) && !PyTuple_Check(item)) {
            printf("[.] %s object info\n", Py_TYPE(item)->tp_name);
            printf("  [ERROR] Invalid %s Object\n", Py_TYPE(item)->tp_name);
        }
    }
}
/**
 * print_python_bytes -
 * @p: -
*/
void print_python_bytes(PyObject *p) {
    Py_ssize_t i, size;
    char *string;

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", PyBytes_Size(p));
    printf("  trying string: %s\n", PyBytes_AsString(p));

    size = PyBytes_Size(p) < 10 ? PyBytes_Size(p) : 10;
    string = PyBytes_AsString(p);

    printf("  first %ld bytes: ", size);
    for (i = 0; i < size; i++) {
        printf("%02x ", (unsigned char)string[i]);
    }
    printf("\n");
}
