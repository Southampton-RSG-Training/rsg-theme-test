if (dir.exists(paste(getwd(), "/_episodes_rmd/", sep=''))) {
    epdir <- paste(getwd(), "/_episodes_rmd/", sep='')
} else if (dir.exists(paste(getwd(), "/collections/_episodes_rmd/r-novice/", sep=''))) {
    epdir <- paste(getwd(), "/collections/_episodes_rmd/r-novice/", sep='')
}

data_raw_path <- paste(getwd(), "/data_raw/", sep='')
## file structure
if (!dir.exists(data_raw_path)) dir.create(data_raw_path)

if (!file.exists("data_raw/surveys.csv")) {
    download.file("https://ndownloader.figshare.com/files/2292172",
                  "data_raw/surveys.csv")
}
if (!file.exists("data_raw/species.csv")) {
    download.file("https://ndownloader.figshare.com/files/3299483",
                  "data_raw/species.csv")
}
if (!file.exists("data_raw/plots.csv")) {
    download.file("https://ndownloader.figshare.com/files/3299474",
                  "data_raw/plots.csv")
}
if (!file.exists("data_raw/portal_data_joined.csv")) {
    download.file("https://ndownloader.figshare.com/files/2292169",
                  "data_raw/portal_data_joined.csv")
}

if (!file.exists("data_raw/portal_mammals.sqlite")) {
    download.file("https://ndownloader.figshare.com/files/2292171",
                  "data_raw/portal_mammals.sqlite")
}


## knitr options
library(knitr)
library(methods)
library(shiny)
suppressPackageStartupMessages(library(tidyverse))
knitr::opts_chunk$set(results='hide', comment = ">", purl = FALSE, fig.keep='last')

base_url <- "" # keep as is
fig_path <- "fig/" # Output path for figures

# If the document is currently being knit, do this; skip it in normal execution
if (!is.null(knitr::current_input())){
  # Set base directories
  knitr::opts_knit$set(base.url = base_url)

  # Set figure directories
  knitr::opts_chunk$set(fig.path = fig_path,
                      cache.path = '../cache/',
                      message=FALSE, warning=FALSE,
                      cache = FALSE)
}


### Custom hooks
## hook for challenges answers

# If we are in an answer block indent by one

hook_chunk <- knitr::knit_hooks$get("chunk")  # save the old hook
knitr::knit_hooks$set(chunk = function(x, options) {
  if (isTruthy(options$answer)) {
    x <- gsub('```r', '', x)
    x <- gsub('```', '', x)
    indent <- options$indent
    if(is.null(indent)) {indent <- ''}
    paste(c(paste(paste(indent, '> ', sep=''),
                  c('## Solution',
                    unlist(strsplit(x, '\n'))
                  ),
                  sep = ''),
            '{: .solution}'),
          collapse = '\n')
  } else {
    hook_chunk(x, options)
  }
})

# engine for targeting SWC markdown
eng_text_answer <- function(options){
    paste(
          c(paste('> ',
                  c('## Solution',
                    '',
                    unlist(strsplit(options$code, '\n'))
                  ),
                  sep = ''),
            '{: .solution}'),
          collapse = '\n')
}

knitr::knit_engines$set(text_answer = eng_text_answer)

library(needs)
prioritize(dplyr)