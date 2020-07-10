
all: indexing index search

indexing: EvenOddIndex.py
	mpiexec -n 3 python EvenOddIndex.py

index: 4threadsIndex.py
	mpiexec -n 4 python 4threadsIndex.py


search: search.py
	mpiexec -n 3 python search.py

