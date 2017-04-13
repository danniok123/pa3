/****************************************************************************
   * kk.c
   *
   * Group members
   * Harvard ID: 30939506
   * Harvard ID: 50940144
   ***************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include "karp_helper.h"

// global variables
FILE *file; 

int main(int argc, char* argv[]) {
	if (argc != 2) {
		printf("Usage: ./kk inputfile\n");
		return 0;
	} else {
		// saves command-line arguments 
		file = fopen(argv[1], "r");
	}

	if (file == NULL) {
      fprintf(stderr, "can't open %s\n", argv[1]);
    } else {
		// inputs content from file to A and B matrices
		for (int i = 0; i < 100; i++) {
			fscanf(file, "%d", ??);
		}
	}
      
}