> [Back](../README.md)
<div style="text-align: right"> Group C</div>
<div style="text-align: right"> April 26th 2024</div>

<h2> Project Proposal - Shrine & Temple Crowdedness Tracker </h2>

<h3>Abstract</h3>
<div style="text-align: justify; text-indent: 36px">   Whilst Japan suffers from over-tourism, it is also dependent on tourists' economic benefits. Especially in its history-rich city, Kyoto, shrines and temples are impacted the most. In order for both Japan and tourists to co-exist, this project aims to address the causality of over-tourism, tourist density. This project would present a resolution through a route-suggesting application that prevents tourists from visiting crowded shrines or temples, making it more crowded, intensifying the problem. </div>
<br>

<h3>Background</h3>
<div style="text-align: justify; text-indent: 36px">   With an average figure of 25 million visiting every year before the COVID-19 pandemic, Japan has long been renowned for its beauty and rich cultural heritage among tourists. After the pandemic significantly disrupted the global tourism industry, including Japan, the country soon recovered, accounting for 25 million of visitors in 2022 which is almost the same as pre-pandemic figures (Japan Tourism Statistics, 2024). With such a large number of travelers, the problem of over tourism such as buses being overly crowded which made it hard for local elderly and those with baby strollers to utilize them, poor behaviors including littering, trespassing on private land has surfaced, typically in Kyoto (Mainichi Daily News, 2023). This problem of over tourism has come to our attention to provide assistance in countermeasures by managing crowds in popular tourist areas, especially shrines and temples. By developing an application, we aim to provide interactive solutions to tourists who wish to explore Japan’s lovely history, hence easing the tourist crisis Japan is suffering from. </div>
<br>

<h3>Introduction</h3>
<div style="text-align: justify; text-indent: 36px">To address the problem of over tourism we aim to create an application that makes recommendations to users which is designed to find shrines and temples based on real-time crowdedness. The main functionality of this app will be to recommend the best routes to the destination by showing the user how to avoid crowdedness using real-time information and the forecast of the shrine or temple that the user is considering visiting. This will be part of the categories the user can pick from to find the destination they want to go to, which ultimately works as a filtered search. We will also include functions such as displaying the nearest shrine or temple based on their current location, the distance to the destination from the current location, and the transportation prices to get there. 
</div>
<br>


<h3>Detailed Features</h3>
<div style="text-align: justify; text-indent: 36px">In detail, our project is aiming to realize a few features. The main feature would allow the user to choose, based on their preference, the shrines and temples they would want to visit. Then, the app would recommend a visiting route with consideration of the crowdedness data. The chosable preferences, currently, would include worshiping gods, ratings, reviews, distance, price, and crowdedness. The list is evolvable depending on available data from shrine and temple databases. Although this feature is potentially useful, however, it alone as an application is not complete.
</div>

<div style="text-align: justify; text-indent: 36px">There are secondary features that the application would like to implement to make the experience more complete. One of them would be shrine and temple information-look up. The user should be able to see the information such as address, operating hours, worshiping gods, built era before they make decisions on which to visit, or simply, they would want to look up the information. Similarly, there may be cases that the user is not clear about their preference for shrines and temples as they simply might want to explore. Another feature would allow the user to explore shrines and temples by categories. An explore tab in the application would list different types of temples for the user to read in and explore. If they are interested, the user is then led to use the main feature to visit the shrines or temples that appeal to their interests.
</div>

<div style="text-align: justify; text-indent: 36px">For this application to be acceptable for tourists, the project plans to integrate general tourist-oriented features to boast the entertainment aspect. There are features that are more desirable than necessary such as creating accounts that record achievement, and taking part in quiz sections. Users can create an account, add favorite shrines and temples and log those that they have been to and depending on this, the application records a streak like visiting several shrines and temples for some consecutive days. In addition, it will store quiz achievement and stamps collected from the shrines that the user visited. The quiz section includes trivial questions on history, architecture, and traditions and achievement would be rewarded. A score board featuring the number of achievements of the application users will also be implemented in the future. 
</div>
<br>

<h3>Limitation</h3>
<div style="text-align: justify; text-indent: 36px">Since the project is planning to mostly be reliant on APIs to collect crowdedness data, there are some potential sustainability issues for this application. For example, if the API went offline, then the application can no longer fetch the crowdedness data that the recommendation system needs. Such an event would cause the application’s main feature to be non-functional. In addition, due to the reliance, if the API decided to make upcharge to their request calls, for a real project with limited budget, this would not be sustainable as well. While acknowledging this drawback, considering the cost of creating a data collection system that is independent, such a project is more unfeasible. 
</div>
<br>

<h3>Methodology</h3>
<div style="text-align: justify; text-indent: 36px">In discussion for what platform to host and serve this application, the decision should be dependent on how the application is designed to be used by the user. This application focuses on how a tourist can avoid crowded areas in real-time. The real-time factor suggests that the device the user is most probable to carry is limited to their smartphone. Due to the limited selection of devices, this application is more preferably be developed as an app on IOS/Android, or a web app which is accessible from any mobile devices. Considering the time limitation of this project, creating the application on duo-platform is not wise in time-management. A web app seems to be the most appropriate solution. 
</div>

<div style="text-align: justify; text-indent: 36px">With some research, we have discovered that there are apps on both IOS and Android that can serve a web app as a normal smartphone application. The team would be looking into the possibility of such deployment. However, in terms of consistency, remaining as a web app would be easier to manage.
</div>
<br>


<h3>References</h3>
<div style="text-indent: -36px; padding-left: 36px">  
[1] “Data list | Japan Tourism Statistics | Japan National Tourism Organization (JNTO),” Jnto.go.jp, 2024. https://statistics.jnto.go.jp/en/graph/#graph--inbound--travelers--transition
</div>
‌
<div style="text-indent: -36px; padding-left: 36px">  
[2] “News Navigator: What exactly is the ‘overtourism’ problem in Kyoto?,” Mainichi Daily News, Nov. 14, 2023. Available: https://mainichi.jp/english/articles/20231114/p2a/00m/0op/016000c
</div>

