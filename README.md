Digital Humanities Project


Project team: Hadas Shidlovski, Rinat Dior and Tal Hekmon

The development of the project included 4 main stages:
1. Data collection
2. Processing of the Information
3. Displaying the results
4. Building a site

1. Collecting the Information:
First, we collected information about the immigration to Israel over the past 10 years from the website of the Ministry of Immigration.
Because some of the files were not of the kind we could work with (Excel, CSV, etc), we wrote a Python program using the Pandas library, 
which, given an HTML link that contains a table of data, collects the data from the link itself, creates an Excel file with that data
and downloads it automatically.
 
2. Processing of the information:
Due to differences in the structure of the tables over the years, we had to edit them accordingly.
First, we arranged the tables with OpenRefine, removed unnecessary columns, and arranged the columns to be the same throughout the years.
Finally, we wrote another Python program with the help of the GoSlate library, which translates the Excel files we created
from Hebrew into English to fit the file format needed in the visual tool we used, Tableau.
 
3. Tableau construction:
For each of data we built online interactive maps using Tableau, and using that tool we could visualize the immigration stats
using maps and graphs.
 
4. Building the site:
In order to present the project conveniently, we have built a site using the Wix platform for building sites.
Among other things, we worked on designing the site, building the content, adding the files we used, etc.
