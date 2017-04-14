/****************************************************************************
   * heap.c
   *
   * Group members
   * Harvard ID: 30939506
   * Harvard ID: 50940144
   ***************************************************************************/
   
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "heap_helper.h"

int leftC(int n){
	return (2 * n) + 1;
}

int rightC(int n){
	return (2 * n) + 2;
}

int parent(int n){
	assert (n > 0);
	return (n - 1) / 2;
}

void swap(int *a, int *b) {
	int tmp = *a;
	*a = *b;
	*b = tmp;
}


heap *createHeap(int size) {
	heap *h =  (heap *) malloc(sizeof(heap));
	h->currSize = 0;
	h->maxSize = size;
	h->list = malloc(size * sizeof(int));

	return h;
}

// Insert node into heap
void insert(heap *h, int val) {
	// reallocate more space
	if (h->maxSize <= h->currSize) {
		h->maxSize <<= 1;
		h->list = realloc(h->list, h->maxSize * sizeof(int));
	}
	
	h->list[h->currSize] = val;
	int i = h->currSize;
	h->currSize++;

	// Move to appropriate position through swaps
	while (i && h->list[i] > h->list[parent(i)]) {
		swap(&(h->list[parent(i)]), &(h->list[i]));
		i = parent(i);
	}
}

void maxHeap(heap *h, int i) {
	int left = leftC(i);
	int right = rightC(i);
	int largest = i;

	if (left < h->currSize && h->list[left] > h->list[largest])
		largest = left;

	if (right < h->currSize && h->list[right] > h->list[largest])
		largest = right;

	if (largest != i) {
		swap(&(h->list[i]), &(h->list[largest]));
		maxHeap(h, largest);
	}
}

void frees(heap *h) {
	free(h->list);
	free(h);
}

