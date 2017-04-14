CC=clang

CFLAGS=-c -Wall -g

all: kk

kk: kk.o kk_helper.o heap.o
	$(CC) kk.o kk_helper.o heap.o -o kk

kk.o: kk.c
	$(CC) $(CFLAGS) kk.c

kk_helper.o: kk_helper.c
	$(CC) $(CFLAGS) kk_helper.c

heap.o: heap.c
	$(CC) $(CFLAGS) heap.c


clean:
	rm -f *.o kk