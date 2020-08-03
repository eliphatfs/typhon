# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:46:59 2020

@author: eliphat
"""
from . import impl
from ..type_system.base_types import PyStr, PyNone


impl("input", tuple(), PyStr, tuple(), """
    char * line = NULL;
    FILE * stream = stdin;
    size_t zn = 0;
    size_t * n = &zn;
    char ** lineptr = &line;
    char * bufptr = NULL;
    char * p = bufptr;
    size_t size;
    int c;

    bufptr = *lineptr;
    size = *n;

    c = fgetc(stream);
    if (bufptr == NULL) {
        bufptr = malloc(128);
        size = 128;
    }
    p = bufptr;
    while(c != EOF) {
        if ((p - bufptr) > (size - 1)) {
            size = size + 128;
            bufptr = realloc(bufptr, size);
        }
        *p++ = c;
        if (c == '\\n') {
            break;
        }
        c = fgetc(stream);
    }

    *p++ = '\\0';
    *lineptr = bufptr;
    *n = size;
    return *lineptr;
""", inc=("stdio.h", "stdlib.h"), inl=False)
impl("print", (PyStr,), PyNone, ("x"), 'printf("%s\\n", x);', "stdio.h")
