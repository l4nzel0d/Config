# Define variables for the archive name, executable, list file, and source files
ARCHIVE = distr.zip
EXECUTABLE = prog.exe
LISTFILE = files.lst
COMPILER = gcc    # Can be replaced with another compiler if needed
SRC_FILES = prog.c data.c  # Source files to compile

# Get all files in the directory except files.lst and the archive
ALL_FILES = $(filter-out $(LISTFILE) $(ARCHIVE), $(wildcard *))

# Default target
all: $(EXECUTABLE) $(LISTFILE) archive

# Build target
$(EXECUTABLE): $(SRC_FILES)
	@echo "Building file $(EXECUTABLE) ..."
	@$(COMPILER) $(SRC_FILES) -o $(EXECUTABLE)
	@echo "Successfully built file $(EXECUTABLE)"

# File list target
$(LISTFILE): $(filter-out $(LISTFILE), $(wildcard *))  
	@echo "Creating $(LISTFILE) ..."
	@dir /B > $(LISTFILE) 2> nul

# Archive target
archive: $(filter-out $(ARCHIVE), $(wildcard *))  
	@echo "Creating archive $(ARCHIVE)..."

# Clean target
clean:
	@echo "Cleaning up..."
	@del $(ARCHIVE) $(EXECUTABLE) $(LISTFILE) 2> nul || true

.PHONY: all build archive clean
