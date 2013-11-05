
TEXFILE="lab_report_1"
TEX=pdflatex -shell-escape
#TEXFILE="test_python"
basic:
	$(TEX) $(TEXFILE).tex

all: clean basic sympy display
	echo 'Done.'

build: basic sympy
	echo 'Done.'

display:
	evince $(TEXFILE).pdf

sympy:
	python $(TEXFILE).sympy
	$(TEX) $(TEXFILE).tex

bibtex:
	bibtex $(TEXFILE)
	$(TEX) $(TEXFILE).tex
	$(TEX) $(TEXFILE).tex

quick: clean
	$(TEX) $(TEXFILE).tex
	evince $(TEXFILE).pdf

clean:
	-rm -f $(TEXFILE).log
	-rm -f $(TEXFILE).aux
	-rm -f *.pyc
	-rm -f *.log
	-rm -f *.bbl
	-rm -f *.sout
	-rm -f *.blg
	-rm -f *.sympy
	-rm -f *.4ct
	-rm -f *.4tc
	-rm -f *.dvi
	-rm -f *.idv
	-rm -f *.lg
	-rm -f *.tmp
	-rm -f *.xref
	-rm -rf sympy-plots-for-lab_report_1.tex/

