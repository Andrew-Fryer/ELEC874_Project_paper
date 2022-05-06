rm *.aux *.log *.bbl *.blg

file="main"
latex_file="${file}.tex"

pdflatex "${latex_file}" &&
bibtex "${file}" &&
pdflatex "${latex_file}" &&
pdflatex "${latex_file}"
