# Define variables for the archive name, executable, list file, and source files
ARCHIVE = distr.zip
EXECUTABLE = prog.exe
LISTFILE = files.lst
COMPILER = gcc    # Can be replaced with another compiler if needed
SRC_FILES = prog.c data.c  # Source files to compile


# Default target
# all: $(EXECUTABLE) $(LISTFILE) $(ARCHIVE)
all: build list archive

build: $(EXECUTABLE)
list: $(LISTFILE)
archive: build list $(ARCHIVE)

$(EXECUTABLE): $(SRC_FILES)
	@echo "Building file $(EXECUTABLE) ..."
	@$(COMPILER) $(SRC_FILES) -o $(EXECUTABLE)
	@echo "Successfully built file $(EXECUTABLE)"

$(LISTFILE): $(filter-out $(LISTFILE) $(ARCHIVE), $(wildcard *))  
	@echo "Creating $(LISTFILE) ..."
	@dir /B | findstr /V /C:"$(LISTFILE)" /C:"$(ARCHIVE)" > $(LISTFILE) 2> nul


$(ARCHIVE):
	@echo "Creating archive $(ARCHIVE) using 7z..."
	@7z a $(ARCHIVE) $(filter-out $(ARCHIVE), $(wildcard *))> nul 2>&1
	@echo "Archive $(ARCHIVE) created successfully"

clean:
	@echo "Cleaning up..."
	@del $(ARCHIVE) $(EXECUTABLE) $(LISTFILE) 2> nul || true

.PHONY: all build list archive clean
