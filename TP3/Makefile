COMPILER = gcc
FILESYSTEM_FILES = main.c

build: $(FILESYSTEM_FILES)
	$(COMPILER) $(FILESYSTEM_FILES) -o fylesystem `pkg-config fuse --cflags --libs`
	echo 'To Mount: ./fylesystem -f [mount point]'

clean:
	rm fylesystem