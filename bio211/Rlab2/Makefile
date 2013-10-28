LAB_FILE='lab2'

all: build
	 evince $(LAB_FILE).pdf

build:
	 python $(LAB_FILE).py
	 R CMD Sweave $(LAB_FILE).Rnw
	 pdflatex $(LAB_FILE).tex
	 pdflatex $(LAB_FILE).tex

clean:
	rm -f $(LAB_FILE).tex
	rm -f *.pdf
	rm -f *.aux
	rm -f *.log
	rm -f *.csv
	rm -f *.png
