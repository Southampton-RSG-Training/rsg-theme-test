# RMarkdown files
RMD_SRC = $(filter-out README.md, $(wildcard *.Rmd))

all: pages

pages: ${RMD_SRC} _site.yml
	R -q -e 'if (!requireNamespace("remotes", quietly=FALSE)) install.packages("remotes", repos="https://cran.rstudio.com/"); remotes::install_deps()'
	R -q -e 'if (!requireNamespace("rmarkdown", quietly=FALSE)) install.packages("rmarkdown", repos="https://cran.rstudio.com/", rebuild=TRUE);'
	R -q -e 'rmarkdown::render_site()'

check-spelling:
	Rscript -e "source('check-spelling.R')"
