all: build
	 evince test.pdf

build:
	 R CMD Sweave test.Rnw
	 pdflatex test.tex
	 pdflatex test.tex

clean:
	rm -f *.pdf
	rm -f *.aux
	rm -f *.log
