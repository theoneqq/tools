#include <stdio.h>
#include "byte.h"

void show_bytes(byte_p start, size_t len) {
	for (size_t i = 0; i < len; ++i) {
		printf("%.2x ", start[i]);
	}
	printf("\n");
}

void show_int(int x) {
	show_bytes((byte_p) &x, sizeof(int));
}

void show_float(float x) {
	show_bytes((byte_p) &x, sizeof(float));
}

void show_pointer(void* x) {
	show_bytes((byte_p) &x, sizeof(void *));
}

