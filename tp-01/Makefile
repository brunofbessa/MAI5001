all:
	gcc -c ./src/LojaVirtual.c -I ./include -o ./obj/LojaVirtual.o
	gcc ./apps/main.c ./obj/.o -I ./include -o ./bin/programa

run:
	./bin/programa

clean:
	rm ./obj/*.o
	rm ./bin/*

	gcc -c ./src/arvore_binaria.c -I ./include -o ./obj/arvore_binaria.o
	gcc ./apps/main.c ./obj/.o -I ./include -o ./bin/programa
