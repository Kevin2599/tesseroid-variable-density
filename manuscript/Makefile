# Build the PDF of the manuscript.
#
# Commands:
#
#	make            Compile PDF in the output folder
#	make show       Show the generated PDF (only Linux and Mac)
#	make wc         Count the number of words in the generated PDF
#	make clean      Delete all generated files
#	make greyscale  Generates a greyscale version of the PDF


# CONFIGURATION
###############################################################################

# The name of the main .tex file to build.
# Other files can be included into this one.
PROJECT = manuscript

# Folder with the Latex source files
SRC = .

# Folder where the figure files are (will assume they are PDF format)
FIGS = figures

# Folder where the BibTex .bib files are
BIB = .

# Folder where the .cls .bst and .sty style files are
STYLES = $(SRC)

# Folder where output will be placed
OUTPUT = output

### File Types (for dependencies)
TEX_FILES = $(shell find $(SRC) -maxdepth 1 -name '*.tex')
BIB_FILES = $(shell find $(BIB) -maxdepth 1 -name '*.bib')
STY_FILES = $(shell find $(STYLES) -maxdepth 1 -name '*.sty')
CLS_FILES = $(shell find $(STYLES) -maxdepth 1 -name '*.cls')
BST_FILES = $(shell find $(STYLES) -maxdepth 1 -name '*.bst')
FIGS_PDF_FILES = $(shell find $(FIGS) -maxdepth 1 -name '*.pdf')

### Compilation Flags
LATEX_FLAGS  = -halt-on-error -output-directory $(OUTPUT)/

### Standard PDF Viewers
UNAME := $(shell uname)
ifeq ($(UNAME), Linux)
PDFVIEWER = evince
endif
ifeq ($(UNAME), Darwin)
PDFVIEWER = open
endif


# MAIN TARGETS
###############################################################################

all: $(OUTPUT)/$(PROJECT).pdf

show: all
	@ # Redirect stdout and stderr to /dev/null for silent execution
	@ (${PDFVIEWER} $(OUTPUT)/$(PROJECT).pdf > /dev/null 2>&1 & )

wc: all
	@ pdftotext $(OUTPUT)/$(PROJECT).pdf - | wc -w

greyscale: $(OUTPUT)/$(PROJECT).pdf
	gs \
   -sDEVICE=pdfwrite \
   -sProcessColorModel=DeviceGray \
   -sColorConversionStrategy=Gray \
   -dOverrideICC \
   -o $(OUTPUT)/$(PROJECT)-greyscale.pdf \
   -f $(OUTPUT)/$(PROJECT).pdf

### Proselint
# This target runs proselint (a grammar checker) on manuscript.tex.
proselint:
	@ proselint $(SRC)/$(PROJECT).tex

### Clean
# This target cleans the temporary files generated by the tex programs in
# use. All temporary files generated by this makefile will be placed in OUTPUT
# so cleanup is easy.
clean:
	rm -rf $(OUTPUT)/ *.aux

$(OUTPUT)/:
	mkdir -p $(OUTPUT)/

$(OUTPUT)/$(PROJECT).aux: $(TEX_FILES) $(STY_FILES) $(CLS_FILES) $(FIGS_PDF_FILES) | $(OUTPUT)/
	pdflatex $(LATEX_FLAGS) $(SRC)/$(PROJECT)
	cp $@ .
	# Copy the aux file next to the tex file for Vim completion purposes

$(OUTPUT)/$(PROJECT).bbl: $(BIB_FILES) $(BST_FILES) | $(OUTPUT)/$(PROJECT).aux
	cp $(BIB_FILES) $(BST_FILES) $(OUTPUT)
	cd $(OUTPUT) && bibtex $(PROJECT)
	pdflatex $(LATEX_FLAGS) $(SRC)/$(PROJECT)

$(OUTPUT)/$(PROJECT).pdf: $(OUTPUT)/$(PROJECT).aux $(OUTPUT)/$(PROJECT).bbl
	pdflatex $(LATEX_FLAGS) $(SRC)/$(PROJECT) 1>/dev/null
