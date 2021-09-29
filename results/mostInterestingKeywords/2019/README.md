# Keywords with the highest 'interestingness' in 2019

### Explanation:
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


## Results - New York Times:
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

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | venezuela | 4: [18, inf] | venezuela maduro 's | Nicolás_Maduro |
| 2. | christchurch | 11: [26, inf] | christchurch attack zealand | Christchurch_mosque_shootings |
| 3. | dame | 16: [29, inf] | dame fire cathedral | Notre-Dame_de_Paris_fire |
| 4. | fire | 16: [14, inf] | fire dame police | Notre-Dame_de_Paris_fire |
| 5. | mugabe | 36: [10, inf] | mugabe robert 's | Robert_Mugabe |
| 6. | kurds | 41: [11, inf] | kurds syria trump | Autonomous_Administration_of_North_and_East_Syria |
| 7. | turkish | 41: [15, inf] | turkish syria us | Turkish_involvement_in_the_Syrian_civil_war |
| 8. | white | 50: [16, inf] | white island volcano | 2019_Whakaari_/_White_Island_eruption |
| 9. | island | 50: [16, inf] | island white volcano | Whakaari_/_White_Island |
| 10. | volcano | 50: [14, inf] | volcano white island | 2019_Whakaari_/_White_Island_eruption |
