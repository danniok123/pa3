all: clean kk

strassen: karp.c
	gcc kk_helper.c kk.c -o kk -I.

clean:
	rm -f kk