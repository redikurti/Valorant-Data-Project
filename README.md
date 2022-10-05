# Proposal

For my Python Programming project I would also like to do a statistical analysis of different player and champion stats of the video game Valorant. This is a first-person shooter game that I play frequently and I always wanted to make some sort of project in it. Moreover, I looked at the example given for this class and someone made a project where they analyzed a different video game called Call of Duty. I would gather data from tracker.gg/Valorant and use this to gain inside information on things such as: which champions performs better on which maps, gun accuracy and usage, player data regarding body-shot or head-shots etc. I think this would be quite a fun project for me as I am really invested in the game. I still need to structure the analysis I would do in this project but that would come after a closer inspection to the data provided and the data that is accessible.


# Execution Plan

- By the end of week 4, read and learn about the BeautifulSoup module and figure out how to access information from the website.
- By the end of week 5, learn the html of the website and start working on the web scrapper.
- By the end of week 6, finish the web scrapper and create/update/clean the dataframe. Have all the data.
- By the end of week 7, start analyzing and visualizing the data using matplotlib and seaborn. Figure out how seaborn works as we already learned matplotlib in class.
- By the end of week 8, start creating the linear regreation model using sklearn module.
- Finally, evaluate the prediction model and work on video presentation.

# Research Project 

Hello gamers and viewers!!! 

In my final project for the Python class I decided to do a data analysis/visualization about the video game Valorant.
Initially I looked at a few websites like blitz and tracker to get my data but ultimately decided to scrape my Valorant player data from https://tracker.gg/valorant. This is one of the few websites which has access to the official Riot API, Riot is the company that developed and owns the game, so the data is very accurate. I wanted to see if we can build a model that predicts the win percentage of a player based on information we get from the website. This is a tactical shooter game where aim, strategy, ability usage and co-operation with teammates are key to achieve victory. 

Research Question: How relevant are statistics like Wins, Kills, Headshots, Deaths, Assists, Score/Round, Kills/Round, First Bloods, Aces, Clutches, Flawless, Most Kills (Match), Damage/Round, K/D Ratio, Headshot% in predicting the win percentage of a player in the video game Valorant?

# Conclusion 

In conclusion, I looked at over 5000 of the best players in Valorant and managed to model the data using a linear regression model which can predict the Win % of a given player ~80% of the time with a 1.6% absolute error given that players	Wins, Kills, Headshots, Deaths, Assists, Score/Round, Kills/Round, First Bloods, Aces, Clutches, Flawless, Most Kills (Match), Damage/Round, K/D Ratio, Headshot%.

#### NOTE

Keep in mind that if you rerun the code in 'valorant_data_analysis', since we split the data randomly into the testing and training subsets, then you might get different coefficients and different values for our evaluation metrics. However, I run the model over a for-loop and got the mean of all the values for R-Squared and we end up in the range from 78%-85%. THis is all good as it is higher that 70% which is the cut for a good value of R-Squared.

#### NOTE ABOUT DATA

Since my data is less than 1MB, per the instructions, I pushed them into Github. 