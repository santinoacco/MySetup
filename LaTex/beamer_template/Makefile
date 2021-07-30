file=HEP_update_Noacco
#file=QTask_Update
#file=main_minimal
#file=$1

src= $(file).tex
#src= $(file).tex commands.tex sections/title.tex sections/lhc.tex sections/neuralnetworks.tex sections/method.tex sections/results.tex sections/abstract.tex sections/acknowledgements.tex sections/conclusion.tex
#figs=

#force: cleanall $(file).pdf

all: $(file).pdf clean

$(file).pdf: $(src)
	pdflatex $(file) ; bibtex $(file) ; pdflatex $(file) ; pdflatex $(file) 
	#xelatex $(file) ; bibtex $(file) ; xelatex $(file) ; xelatex $(file) 
	#lualatex $(file); bibtex $(file) ; lualatex $(file) ; lualatex $(file) 
	#xetex $(file) ; bibtex $(file) ; xetex $(file) ; xetex $(file) 

view:	
	okular $(file).pdf &


cleanall: clean
	rm $(file).pdf

clean:
	rm -f *.toc
	rm -f *.out
	rm -f *.log
	rm -f *.aux
	rm -f *.blg
	rm -f *.bbl
	rm -f *.snm
	rm -f *.nav



