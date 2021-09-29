## Wikinews
Wikipedia is an important knowledge database which nowadays has over [five billion visits per month](https://de.statista.com/statistik/daten/studie/1021463/umfrage/anzahl-der-visits-pro-monat-von-wikipediaorg/). A [survey in 2016 on the platform](https://arxiv.org/abs/1702.05379) indicates, that topics which pop up in news media are frequently searched on Wikipedia. Readers of newspaper articles may use Wikipedia to gain additional knowledge about specific topics mentioned in the news. In this project we investigated whether news articles influence the views of Wikipedia sites using data of the [New York Times](https://developer.nytimes.com/) and [The Guardian](https://open-platform.theguardian.com/). We developed concepts to gather the key topics of news articles and to restrict our analysis to relevant content. Moreover we introduce a matching procedure to connect news topics with Wikipedia pages. After applying our methods we find a positive correlation between news occurrencesand related Wikipedia sites for a majority of the topics. [We explain our methods and discuss our findings in a report (not published yet)](https://github.com/lukasmoldon/wikinews/blob/master/paper.pdf).

## Data
### Data from the news
Due to the [terms and conditions](https://www.theguardian.com/open-platform/terms-and-conditions) of TheGuardian, it is practically impossible to provide access to our dataset without violating their policy (see paragraph 5 - Lifecycle of OP Content). However, you can create your own dataset with a personal API key and our code, [which will be explained below](https://github.com/lukasmoldon/wikinews#How-to-use). In our research project we created and used the following datasets:

|file suffix|restrictions|articles (nyt)|articles (theguardian)|
|----------------|-------------------------------|-----------------------------|-----------------------------|
|none|published in 2001 or later |2.953.454|2.096.574|
|_reduced|world news articles published in 2001 or later|213.535|168.328|
|_partition|world news articles published in January 2001|678|603|
|_ground_truth|randomly selected world news articles published in 2001 or later **manually labeled** with related wikipedia links (for measuring accuracy of matching algorithms)|200|200|
### Data from Wikipedia
In our research project we did not create a dataset of Wikipedia data, but requested necessary information from the Wikipedia API in real time on demand. If you want to access this data you can [use our code](https://github.com/lukasmoldon/wikinews/blob/master/api_wikipedia.py) to explore wikipedia pageview counts manually and to compare it with our results, you can use [this web-interface](https://pageviews.toolforge.org/?project=en.wikipedia.org&platform=all-access&agent=user&redirects=0&start=2019-01-01&end=2019-12-31&pages=) for single requests instead of calling the API.

## Code
:arrow_forward: For more detailed information, use the corresponding link to the [docsring](https://numpydoc.readthedocs.io/en/latest/format.html) at the end of each descirption.
* **TextPreprocessing.py** - Contains functions which preprocess text from news articles, including stopword removal and stemming. It also provides more sophisticated methods of linguistics theory to preprocess text, which were discarded for our project.
* **api_nyt.py** - Computes the dataset of NYT articles by accessing the API from The New York Times Developer Network.
* **api_theguardian.py** - Computes the dataset of TheGuardian articles by accessing the API from The Guardian Open Platform.
* **api_wikipedia.py** - Provides all functions which will be used in our analysis to access the Wikipedia API (requesting daily pageview statistics of Wikipedia articles, searching related Wikipedia articles and requesting creation dates of articles).
* **createTables.py** - Represents the main file with general functionalities, like creating yearly datasets or computing a subset of keywords ([see below](https://github.com/lukasmoldon/wikinews#How-to-use)).
* **graphics.py** - Contains all functions which create plots for our paper.
* **manage_articles.py** - Contains functions to handle article datasets, including more sophisticated methods like the co-occurrence.
* **matching.py** - Includes all matching approaches from our paper, where news meda topics get matched with Wikipedia articles.
* **multiprocessingSamples.py** - This script computes a set of random article datasets, where publication dates were shuffled, using a multiprocessing approach for servers.
* **notebook.ipynb** - Here we apply many different methods from our repository on the datasets to provide an overview on the code functionalities.
* **statistics.py** - Collection of statistical functions which we use in our project, e.g. for measuring correlation or computing confidence intervals.
* **timeseries.py** - Class and methods to store and manage daily wikipedia counts.
* **word.py** - Class to add additional information to a keyword like timeseries of the news and Wikipedia, co-occurrences and the matched Wikipedia site.

## How to use
* **1.** Request API keys for [The New York Times Developer Network](https://developer.nytimes.com/get-started) and [The Guardian Open Platform](https://open-platform.theguardian.com/access/)
* **2.** Use your API keys and the function calls at the bottom of `api_nyt.py` ([here](https://github.com/lukasmoldon/wikinews/blob/master/api_nyt.py#L78-L81)) and `api_theguardian.py` ([here](https://github.com/lukasmoldon/wikinews/blob/master/api_theguardian.py#L93-L96)) to start downloading the datasets
* **3.** You can now create yearly datasets and compute top and most interesting keywords using the function calls [here (without multiprocessing)](https://github.com/lukasmoldon/wikinews/blob/master/createTables.py#L13-L43) and [here (using multiprocessing)](https://github.com/lukasmoldon/wikinews/blob/master/createTables.py#L171-L190)
## Results

All results are stored [here](https://github.com/lukasmoldon/wikinews/tree/master/results) and get explained in our [paper](https://github.com/lukasmoldon/wikinews/blob/master/paper.pdf). Below you can find exemplary results for the NYT dataset in 2019.

### Maximum Interestingness 2019 - New York Times

- These tables only consider keywords in articles, which have been categorized as 'world news articles' by the
respective newspaper. 
- The table lists all keywords which fulfill the following two conditions at the same time in at least one calendar week:
	- 1. Keyword was mentioned at least 10 times in the news in a week.
	- 2. Keyword was not mentioned in the respective calendar week before (maximum/infinite changerate of news mentions).
- Additionally calendar weeks, where these keywords have a changerate of at least 5, are also given.
- **Column 1:** The row number, the table is sorted  by the first appearing calendar week of each keyword.
- **Column 2:** The name of the keyword
- **Column 3:** The changerates, which fulfill the conditions (as described above): The first value in front of the brackets represents the corresponding calendar week number. The first value within the brackets represents the total frequency of the keyword in that week. The second value represents the changerate compared to the week before.
- **Column 4:** The computed query for our advanced keyword matching approach
- **Column 5:** The name* of the resulting Wikipedia article computed from our advanced keyword matching approach. Here we use column 4 as query for the API call.

(* use the link https://en.wikipedia.org/wiki/_PLACEHOLDER_ and replace the placeholder by the name)

|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | charges | 2: [12, inf], 4: [12, 6.0] | charges former court | Impeachment |
| 2. | officials | 2: [14, inf], 43: [11, 11.0] | officials say u.s. | Utah_Data_Center |
| 3. | court | 2: [10, inf], 51: [16, inf] | court supreme former | Supreme_Court_of_the_United_States |
| 4. | venezuela | 4: [20, 10.0], 18: [16, inf] | venezuela maduro opposition | Nicolás_Maduro |
| 5. | maduro | 4: [16, 8.0], 8: [19, inf], 18: [10, inf] | maduro venezuela president | Nicolás_Maduro |
| 6. | help | 5: [10, inf], 25: [10, 5.0] | help american trump | Ivanka_Trump |
| 7. | election | 7: [12, 12.0], 11: [10, 10.0], 13: [14, 14.0], 25: [10, inf] | election minister prime | Prime_Minister_of_the_United_Kingdom |
| 8. | report | 10: [10, inf] | report says government | Mueller_report |
| 9. | black | 10: [11, inf] | black south africa | South_Africa |
| 10. | border | 11: [10, 10.0], 14: [12, inf], 46: [12, 12.0] | border trump migrants | Trump_administration_migrant_detentions |
| 11. | vote | 11: [11, inf], 37: [10, 5.0], 50: [10, inf] | vote brexit election | Causes_of_the_vote_in_favour_of_Brexit |
| 12. | christchurch | 11: [14, inf] | christchurch zealand mosques | Christchurch_mosque_shootings |
| 13. | mosques | 11: [14, inf] | mosques zealand two | Christchurch_mosque_shootings |
| 14. | massacre | 11: [11, inf] | massacre zealand christchurch | Christchurch_mosque_shootings |
| 15. | erdogan | 14: [10, inf] | erdogan president turkey | Recep_Tayyip_Erdoğan |
| 16. | leaders | 14: [11, 5.5], 49: [10, inf] | leaders president trump | Donald_Trump |
| 17. | india | 15: [15, 7.5], 18: [11, inf], 20: [10, 10.0], 51: [17, 5.67] | india modi pakistan | 2014_India–Pakistan_floods |
| 18. | assange | 15: [10, inf] | assange julian wikileaks | Indictment_and_arrest_of_Julian_Assange |
| 19. | north | 16: [13, 6.5], 25: [26, inf], 40: [11, 11.0] | north korea trump | North_Korea–United_States_relations |
| 20. | notre-dame | 16: [33, inf] | notre-dame cathedral fire | Notre-Dame_de_Paris_fire |
| 21. | cathedral | 16: [32, inf] | cathedral notre-dame fire | Notre-Dame_de_Paris_fire |
| 22. | paris | 16: [14, inf], 40: [10, inf] | paris police fire | Paris_Police_Prefecture |
| 23. | sri | 16: [16, inf] | sri lanka attacks | 2019_Sri_Lanka_Easter_bombings |
| 24. | lanka | 16: [12, inf] | lanka sri attacks | 2019_Sri_Lanka_Easter_bombings |
| 25. | attacks | 17: [32, 8.0], 38: [10, inf] | attacks sri lanka | 2019_Sri_Lanka_Easter_bombings |
| 26. | sunday | 17: [17, inf] | sunday sri lanka | 2019_Sri_Lanka_Easter_bombings |
| 27. | putin | 17: [10, inf] | putin russia president | Vladimir_Putin |
| 28. | protest | 18: [11, inf], 27: [10, 5.0], 30: [10, inf] | protest hong kong | 2019–20_Hong_Kong_protests |
| 29. | opposition | 18: [12, inf] | opposition leader venezuela | Juan_Guaidó |
| 30. | guaidó | 18: [12, inf] | guaidó venezuela juan | Juan_Guaidó |
| 31. | crisis | 18: [12, inf] | crisis political venezuela | Crisis_in_Venezuela_during_the_Bolivarian_Revolution |
| 32. | fani | 18: [10, inf] | fani cyclone india | Cyclone_Fani |
| 33. | iraq | 19: [11, inf] | iraq iran u.s. | Iran–Iraq_War |
| 34. | last | 19: [10, inf] | last year month | The_Last_Month_of_the_Year |
| 35. | forces | 21: [10, 5.0], 31: [10, inf] | forces u.s. syria | Syrian_Democratic_Forces |
| 36. | union | 21: [12, 6.0], 42: [10, inf] | union european brexit | Brexit |
| 37. | political | 22: [10, 5.0], 29: [14, 14.0], 42: [10, 5.0], 51: [12, inf] | political minister president | Minister_President_of_Prussia |
| 38. | boat | 22: [13, inf] | boat fishing people | Traditional_fishing_boat |
| 39. | wife | 22: [10, inf] | wife former husband | Trophy_wife |
| 40. | iran | 24: [13, inf] | iran u.s. trump | Iran–United_States_relations |
| 41. | shooting | 25: [12, inf] | shooting police zealand | Christchurch_mosque_shootings |
| 42. | must | 25: [11, inf] | must court former | Supreme_Court_of_the_United_States |
| 43. | climate | 25: [10, inf] | climate change president | United_Nations_Climate_Change_conference |
| 44. | mexico | 25: [10, 10.0], 45: [10, inf] | mexico president trump | Donald_Trump |
| 45. | around | 25: [10, inf] | around world china | Around_the_World_in_Eighty_Days |
| 46. | g | 26: [11, inf] | g trump president | Donald_Trump |
| 47. | japan | 26: [10, inf], 41: [12, 6.0] | japan korea south | Japan–South_Korea_relations |
| 48. | kashmir | 32: [13, inf] | kashmir india pakistan | 2014_India–Pakistan_floods |
| 49. | iranian | 33: [10, inf], 39: [10, 10.0] | iranian iran u.s. | Iran–United_States_relations |
| 50. | prince | 34: [11, inf] | prince saudi andrew | Prince_Andrew,_Duke_of_York |
| 51. | fires | 34: [23, inf] | fires amazon brazil | 2019_Amazon_rainforest_wildfires |
| 52. | amazon | 34: [14, inf] | amazon fires brazil | 2019_Amazon_rainforest_wildfires |
| 53. | residents | 36: [10, inf] | residents government island | Norfolk_Island |
| 54. | pope | 36: [10, inf] | pope francis church | Pope_Francis |
| 55. | francis | 36: [11, inf] | francis pope abuse | Catholic_Church_sexual_abuse_cases |
| 56. | australia | 37: [12, inf] | australia china australian | Chinese_Australians |
| 57. | netanyahu | 37: [13, inf], 47: [10, inf] | netanyahu israel prime | Benjamin_Netanyahu |
| 58. | israel | 37: [14, inf] | israel netanyahu minister | Sara_Netanyahu |
| 59. | gantz | 38: [10, inf] | gantz netanyahu benny | Benny_Gantz |
| 60. | trudeau | 38: [15, inf] | trudeau minister justin | Justin_Trudeau |
| 61. | peru | 40: [12, inf] | peru president congress | President_of_Peru |
| 62. | kurds | 41: [12, inf] | kurds syria turkey | Kurds_in_Syria |
| 63. | kurdish | 41: [11, inf] | kurdish syria turkey | Kurds_in_Syria |
| 64. | turkey | 41: [15, inf] | turkey erdogan president | Recep_Tayyip_Erdoğan |
| 65. | troops | 41: [10, inf] | troops u.s. trump | Foreign_policy_of_the_Donald_Trump_administration |
| 66. | syrian | 41: [13, inf] | syrian syria isis | Syrian_civil_war |
| 67. | militia | 41: [11, inf] | militia syria turkey | Turkish_involvement_in_the_Syrian_civil_war |
| 68. | turkish | 41: [10, inf] | turkish syria turkey | Syria–Turkey_relations |
| 69. | typhoon | 41: [16, inf] | typhoon japan storm | 2020_Pacific_typhoon_season |
| 70. | amid | 42: [11, inf] | amid president country | List_of_presidents_who_did_not_win_reelection |
| 71. | lawmakers | 42: [19, inf] | lawmakers brexit parliament | Brexit_withdrawal_agreement |
| 72. | al-baghdadi | 43: [10, inf] | al-baghdadi leader isis | Abu_Bakr_al-Baghdadi |
| 73. | mining | 45: [10, inf] | mining dam company | Vale_S.A. |
| 74. | macron | 49: [12, inf] | macron president france | Emmanuel_Macron |
| 75. | eruption | 50: [11, inf] | eruption zealand white | 2019_Whakaari_/_White_Island_eruption |
| 76. | white | 50: [10, inf] | white house iran | White_House_Down |
| 77. | nobel | 50: [10, inf] | nobel prize peace | Nobel_Peace_Prize |
| 78. | base | 50: [10, inf] | base afghan u.s. | War_in_Afghanistan_(2001–present) |
| 79. | christmas | 52: [18, inf] | christmas holiday first | Christmas_and_holiday_season |


### Top keywords 2019 - New York Times

- These tables only consider keywords in articles, which have been categorized as 'world news articles' by the   
respective newspaper
- **Column 1:** The position within the ranking
- **Column 2:** The name of the keyword
- **Column 3:** The name* of the resulting Wikipedia article computed from our simple keyword matching approach. Here the API query is always identical with the name of the keyword.
- **Column 4:** The computed query for our advanced keyword matching approach
- **Column 5:** The name* of the resulting Wikipedia article computed from our advanced keyword matching approach. Here we use column 4 as query for the API call.

(* use the link https://en.wikipedia.org/wiki/_PLACEHOLDER_ and replace the placeholder by the name)

| # | keyword | matching result (simple) | computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | president | President | president trump leader | Donald_Trump |
| 2. | trump | Trump | trump president u.s. | Donald_Trump |
| 3. | minister | Minister | minister prime brexit | Timeline_of_Brexit |
| 4. | government | Government | government minister president | Minister-president |
| 5. | china | China | china hong kong | Hong_Kong |
| 6. | country | Country | country president minister | Minister-president |
| 7. | prime | Prime_number | prime minister brexit | Theresa_May |
| 8. | u.s. | U.S._state | u.s. american trump | Donald_Trump_Jr. |
| 9. | police | Police | police hong kong | Hong_Kong_Police_Force |
| 10. | people | People | people killed least | List_of_people_killed_for_being_transgender |
| 11. | leader | Leadership | leader president trump | Donald_Trump |
| 12. | says | Says | says president trump | Donald_Trump |
| 13. | two | 2 | two people killed | List_of_people_killed_for_being_transgender |
| 14. | iran | Iran | iran u.s. trump | Iran–United_States_relations |
| 15. | hong | Hong | hong kong protesters | 2019–20_Hong_Kong_protests |
| 16. | kong | Kong | kong hong protesters | 2019–20_Hong_Kong_protests |
| 17. | american | American | american u.s. trump | Presidency_of_Donald_Trump |
| 18. | officials | Official | officials say u.s. | Utah_Data_Center |
| 19. | election | Election | election minister prime | List_of_prime_ministers_of_India |
| 20. | brexit | Brexit | brexit johnson prime | Boris_Johnson |
| 21. | say | Say | say officials police | SayHerName |
| 22. | could | English_modal_verbs | could trump president | Donald_Trump |
| 23. | protests | Protest | protests hong kong | 2019–20_Hong_Kong_protests |
| 24. | united | United | united states nations | Member_states_of_the_United_Nations |
| 25. | north | North | north korea trump | North_Korea–United_States_relations |
| 26. | killed | Killed_in_action | killed people least | List_of_people_killed_for_being_transgender |
| 27. | years | Years_&_Years | years two ago | Two_Years_Ago |
| 28. | party | Party | party election minister | List_of_chief_ministers_of_Uttar_Pradesh |
| 29. | would | Would? | would president trump | Donald_Trump |
| 30. | may | May | may brexit minister | Brexit |
| 31. | military | Military | military u.s. president | List_of_presidents_of_the_United_States_by_military_service |
| 32. | korea | Korea | korea north south | North_Korea–South_Korea_relations |
| 33. | state | State | state islamic isis | Islamic_State_of_Iraq_and_the_Levant |
| 34. | political | Politics | political minister president | Minister_President_of_Prussia |
| 35. | attack | Attack | attack police killed | 2016_shooting_of_Dallas_police_officers |
| 36. | first | First | first time president | President_of_East_Timor |
| 37. | britain | United_Kingdom | britain brexit minister | Brexit |
| 38. | protesters | Protest | protesters hong kong | 2019–20_Hong_Kong_protests |
| 39. | south | South | south korea north | North_Korea–South_Korea_relations |
| 40. | deal | Deal | deal brexit iran | Boris_Johnson |
| 41. | former | Former | former president minister | List_of_presidents_of_India |
| 42. | world | World | world leaders around | Reactions_to_the_assassination_of_John_F._Kennedy |
| 43. | british | British | british brexit minister | Brexit |
| 44. | russia | Russia | russia russian putin | Vladimir_Putin |
| 45. | parliament | Parliament | parliament brexit minister | Timeline_of_Brexit |
| 46. | states | State | states united trump | Donald_Trump |
| 47. | syria | Syria | syria isis u.s. | Islamic_State_of_Iraq_and_the_Levant |
| 48. | india | India | india modi pakistan | 2014_India–Pakistan_floods |
| 49. | many | Many | many say country | COVID-19_pandemic_by_country_and_territory |
| 50. | european | European | european union brexit | Impact_of_Brexit_on_the_European_Union |