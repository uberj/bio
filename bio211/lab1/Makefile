
TEXFILE="lab_report_1"
#TEXFILE="test_python"
all: clean
	pdflatex $(TEXFILE).tex
	python $(TEXFILE).sympy
	pdflatex $(TEXFILE).tex
	evince $(TEXFILE).pdf

quick: clean
	pdflatex $(TEXFILE).tex
	evince $(TEXFILE).pdf

clean:
	-rm -f $(TEXFILE).log
	-rm -f $(TEXFILE).aux
