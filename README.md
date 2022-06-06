# scraping-striver-sde-sheet

I wanted to get the questions on Striver's SDE sheet on a word file, but it was too difficult to copy paste the questions from the website.
So, I hacked together this selenium code on python to scrape the questions from the website. However, there were a few complications to use this code. 
Firstly, when the website runs user has to close the pop-up asking for notifications. Next you must close the ad on the bottom of the page. 
Now the code will wait for 15 seconds and will print the list of questions.
