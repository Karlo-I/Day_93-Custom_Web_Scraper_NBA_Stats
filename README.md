Below is a self-reflection I have submitted to the course provider after completing the project, which I believe will help provide background for this repository.

Reflection:

I approached this project by starting with locating the previous tutorials on web scraping and saving data in a CSV file, then relearning the topics covered.

There are several approaches to web scraping, such as using either the BeautifulSoup module or the Selenium module. I opted for the latter as it is the more advanced and interactive tool.

I then set up the Selenium driver in the IDE.

Next, I began looking at each website provided in the tutorial to decide which one to use and which pieces of data to scrape for this project. I chose ‘www.nba.com/stats’ because it appeared to be the easiest site to navigate and extract information from, such as top players in terms of points, steals, blocks, and rebounds. Additionally, I am a big fan of basketball.

I then started writing the code with a bit of help from ChatGPT to get me started.

Scraping data from the website is relatively straightforward, but the biggest challenge is figuring out the exact path to copy from each element.

After figuring out how to make the code work for the top players in terms of points per game, I replicated the code for other statistics (e.g., assists, steals, and rebounds per game).

The next challenge was writing the data into a CSV file.

At this point, I sought help from ChatGPT to suggest the code needed to include all the statistical data in one CSV file. This was resolved by creating one table for all the data.

Once I got the code to work, I created another Python script that generates a CSV file with the different statistical data separated into different tables, as an alternative.

Finally, before committing and publishing the code on GitHub, I cleaned up and simplified the code by assigning the XPATHs as ‘global variables,’ deleting unnecessary comments I had made earlier, and updating the wording of some of the comments I wanted to keep.
