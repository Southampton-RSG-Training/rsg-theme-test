## Data
The data used in this lesson comes from a project observing a small mammal community in southern
Arizona, US. This is part of a project studying the effects of rodents and ants on the plant
community that has been running for almost 40 years. The rodents are sampled on a series of 24 plots,
with different experimental manipulations controlling which rodents are allowed to access which plots.
This is a real dataset that has been used in over 100 publications. It is published at [Ecological Archives](http://esapubs.org/archive/ecol/E090/118/) and can be found on [Portal Project Database](https://github.com/weecology/PortalData). This data is open and free to use for research purposes.

For the purposes of training, this data has been simplified a bit (you can still download the full dataset and work with it using exactly the same tools we will learn here). This simplified version of data is available from the [Portal Project Teaching Dataset](http://figshare.com/articles/Portal_Project_Teaching_Database/1314459). In this lesson, you will need to download the following five files from the [Portal Project Teaching Dataset](http://figshare.com/articles/Portal_Project_Teaching_Database/1314459):
-  [messy_survey_data.xls](/data/messy_survey_data.xls) - this is the main file we will work with. It includes messy survey data
(in Excel's `.xls` format) that you will clean during the lesson and use to learn some best practices in
data organisation.
- [surveys.csv](https://ndownloader.figshare.com/files/2292172) - the cleaned survey data
    Fields: `record_id`, `month`, `day`, `year`, `plot_id`, `species_id`, `sex`, `hindfoot_length`, `weight`
- [plots.csv](https://ndownloader.figshare.com/files/3299474) - clean information on plot number and type
    Fields: `plot_id`, `plot_type`
- [species.csv](https://ndownloader.figshare.com/files/3299483) - clean information on species codes and scientific names
    Fields: `species_id`, `genus`, `species`, `taxa`
- [combined.csv](https://ndownloader.figshare.com/files/10717186) - clean data from surveys, plots and species data
files combined into one clean file (a good example of what a clean data file should look like)
Fields: `record_id`, `month`, `day`, `year`, `plot_id`, `species_id`, `sex`, `hindfoot_length`, `weight`, `genus`,
`species`, `taxa`, `plot_type`

## Software

To interact with spreadsheets, you can use various software - for example Microsoft Excel,
LibreOffice, Gnumeric, OpenOffice.org, Google Spreadsheets. Commands may differ a bit between programs,
but the general ideas for thinking about spreadsheets are the same.

For this lesson, if you do not have a spreadsheet program already, you can use a free and open source tool
[LibreOffice](https://www.libreoffice.org/download/libreoffice-fresh/)
as it can open Excel spreadsheets, which is the format of the data we will work with during the lesson
(also all examples used refer to Excel).

### Windows

- Download the Installer
  - Install LibreOffice by going to [the installation page](https://www.libreoffice.org/download/libreoffice-fresh/). The version for Windows should automatically be selected. Click Download Version X.X.X (whichever is the most recent version). You will go to a page that asks about a donation, but you do not need to make one. Your download should begin automatically.
- Install LibreOffice
- Once the installer is downloaded, double click on it and LibreOffice should install.

### Mac OS X

- Download the Installer
  - Install LibreOffice by going to [the installation page](https://www.libreoffice.org/download/libreoffice-fresh/). The version for Mac should automatically be selected. Click Download Version X.X.X (whichever is the most recent version). You will go to a page that asks about a donation, but you do not need to make one. Your download should begin automatically.
- Install LibreOffice
- Once the installer is downloaded, double click on it and LibreOffice should install.

### Linux

- Download the Installer
  - Install LibreOffice by going to [the installation page](https://www.libreoffice.org/download/libreoffice-fresh/). The version for Linux should automatically be selected. Click Download Version X.X.X (whichever is the most recent version). You will go to a page that asks about a donation, but you do not need to make one. Your download should begin automatically.
- Install LibreOffice
- Once the installer is downloaded, double click on it and LibreOffice should install.



