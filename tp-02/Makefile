all:
	gcc -c -w ./src/DEQ.c -I ./include -o ./obj/LojaVirtual.o
	gcc -w ./apps/main.c ./obj/*.o -I ./include -o ./bin/programa

run:
	./bin/programa

clean:
	rm ./obj/*.o
	rm ./bin/*
