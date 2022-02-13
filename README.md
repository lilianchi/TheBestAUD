### lost or found?
As of 2018, Craigslist has surmounted over 60 million users with over 50 billion pageviews per month and over 80 million ads posted on Craigslist monthly (expandedramblings.com). Craigslist is one of the most popular classified advertisements website used for 
viewing and posting advertisements. Its goal is to help people easily find, buy, or sell anything. However, with these incredibly high user-visitation numbers, comes neglected 
improvement on user-interface areas within less popular pages. As hired consultants for Craigslist, we were asked to improve the ad-viewers’ experience by analyzing Craigslist’s business model and process of the platform to find improvements and solutions for this proposal with a demo implementation.

After reviewing Craigslist’s platform and interface, we discovered an area of improvement that would greatly improve the user-experience. Within Craiglist’s site “lost+found”, there is no option for posts to be automatically labeled as lost or found. Currently, advertisers/posters manually label their posts as lost or found which is an additional step that takes time. In addition to this, it’s not required that advertisers/posters label their post as lost or found, so the current sort by functionality doesn’t encompass all the posts. By having the ad be automatically labeled as lost or found, it helps the advertisers to save time and ensures all posts are accurately labeled. 
As users looking within this section are clearly visiting this site with the clear intention of either viewing the site in terms of “lost” or “found”, we identified this as a problem that we could solve. 

Not only would this greatly improve the advertising experience, but also would improve the user-experience as well. This subsection improvement is a win-win that benefits all parties once the improvement has been implemented.

### Programming language
Python

### Authors
* Kai-Duan Chang
* Li-Ci Chuang
* Meghan Harris
* Su-Tien Lee
* Yen-Tsz Huang
* Yi-Hsuan Hsu

### Business Objectives
1. Provide users with the ability to search for all ads via lost or found.
2. provide users with quick links to specific posts based on the most popular topics.
3. Include a third component that utilizes image recognition to provide keyword sub-topics within the most popular topics.

### Data Analysis
1. Web Scraping
    * Craigslist_LAF_LA
    * Craigslist_LAF_WL
3. Classification Models
    * Data Processing
    * TFIDF Vectorizing
    * Model
      1. Naive Bayes model Accuracy 74.92%
      2. Decision Tree Model Accuracy 70.57%
      3. Random Forest Model Accuracy 66.22%
      4. SVM model Accuracy
4. Evaluation (Confusion Matrix)
5. Topic Model
6. Image Recognition

### Validation
To ensure our model was performing correctly, we separated our data into separate train, test, and validation sets.
Once we had our validation sets, we evaluated all our models based on the train, test, and validation datasets. We found that all the models improved significantly with the addition of a validation set. However, the best model was the SVM model (which was also the best model from our earlier model analysis). It should be noted that with the addition of the validation set that our accuracy improved almost over 20%!

### Conclusion
In conclusion, our analysis allows Craigslist to improve their user-experience by allowing ads within the lost + found section to be automatically filtered into lost or found without manual entry. Not only this, but we also took it a step further to allow users the option to “quick link” to the most popular topics within the lost + found section to allow users to find posts much faster and easier. In addition to this, we utilized image recognition on posts within the most popular topics to further label and distinguish posts from another to further improve user-experience.
We wholeheartedly believe that this project and model improves user-experience and brings value both to the user and to Craigslist. We not only considered what best benefits the user and Craigslist respectively, but also researched and understood the user behavior to best optimize value within the “lost+found” page. By increasing the amount of efficient and accurate posts, this then increasing the credibility, which could in turn increase the number of users. With an increased number of users, Craigslist will be able to have an increase in advertisers, which would increase the amount of revenue for Craigslist.

