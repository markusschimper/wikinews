# Keywords with the highest 'interestingness' in 2008

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
| 1. | israel | 2: [15, 5.0], 14: [18, inf] | israel gaza israeli | Gaza–Israel_conflict |
| 2. | official | 2: [12, inf] | official u.s. president | List_of_presidents_of_the_United_States |
| 3. | suharto | 2: [11, inf] | suharto former president | Suharto |
| 4. | former | 2: [16, inf], 35: [12, 6.0] | former president minister | List_of_presidents_of_India |
| 5. | bush | 2: [25, 5.0], 7: [10, inf], 14: [15, 5.0], 20: [10, inf] | bush president iraq | George_W._Bush |
| 6. | pakistani | 3: [11, inf] | pakistani pakistan taliban | Tehrik-i-Taliban_Pakistan |
| 7. | shiite | 3: [10, inf] | shiite iraq iraqi | Sons_of_Iraq |
| 8. | israeli | 5: [11, inf] | israeli gaza israel | Gaza–Israel_conflict |
| 9. | rocket | 6: [12, inf] | rocket gaza israeli | Gaza_War_(2008–2009) |
| 10. | party | 6: [11, 11.0], 37: [11, inf], 43: [11, 11.0], 47: [18, 18.0] | party leader opposition | Leader_of_the_Opposition_(India) |
| 11. | bhutto | 6: [15, inf] | bhutto pakistan benazir | Nusrat_Bhutto |
| 12. | east | 7: [17, inf] | east middle timor | Middle_East |
| 13. | timor | 7: [14, inf] | timor east president | President_of_East_Timor |
| 14. | australia | 7: [12, inf] | australia australian pope | Lloyd_Pope |
| 15. | hezbollah | 7: [10, inf], 19: [11, inf] | hezbollah israel lebanon | 2006_Lebanon_War |
| 16. | fidel | 8: [12, inf] | fidel castro cuba | Cuba_under_Fidel_Castro |
| 17. | castro | 8: [19, inf] | castro cuba raúl | Raúl_Castro |
| 18. | serbia | 8: [10, inf] | serbia kosovo serbian | Kosovo–Serbia_relations |
| 19. | would | 8: [11, inf], 42: [27, 5.4] | would president u.s. | President_of_the_United_States |
| 20. | militants | 8: [11, inf] | militants pakistan pakistani | Pakistan |
| 21. | bureau | 9: [11, inf] | bureau baghdad iraq | Iraq_War |
| 22. | london | 9: [11, inf] | london britain north | London |
| 23. | ecuador | 10: [10, inf] | ecuador colombia american | 1906_Ecuador–Colombia_earthquake |
| 24. | soldiers | 11: [13, inf], 34: [10, 5.0] | soldiers u.s. killed | June_2006_abduction_of_United_States_soldiers_in_Iraq |
| 25. | story | 12: [11, inf] | story f – | The_Short_Stories_of_F._Scott_Fitzgerald |
| 26. | opposition | 14: [16, 5.33], 23: [10, 5.0], 33: [12, inf] | opposition zimbabwe president | President_of_Zimbabwe |
| 27. | bahrain | 14: [11, inf] | bahrain race tomorrow | 2008_Bahrain_Grand_Prix |
| 28. | gaza | 14: [10, inf], 23: [10, 10.0] | gaza israel israeli | Gaza–Israel_conflict |
| 29. | – | 17: [12, inf], 31: [10, 5.0] | – f race | F1_Race |
| 30. | children | 18: [13, inf] | children killed parents | Goebbels_children |
| 31. | hong | 18: [14, inf] | hong kong china | Hong_Kong |
| 32. | kong | 18: [14, inf] | kong hong china | Hong_Kong |
| 33. | myanmar | 19: [18, inf] | myanmar aid cyclone | Cyclone_Nargis |
| 34. | earthquake | 20: [30, inf] | earthquake china quake | 2008_Sichuan_earthquake |
| 35. | monaco | 21: [15, inf] | monaco race track | Race_track |
| 36. | top | 21: [10, inf], 24: [10, 10.0] | top official iraq | Iraq |
| 37. | embassy | 23: [10, inf] | embassy u.s. attack | Attack_on_the_United_States_embassy_in_Baghdad |
| 38. | arrested | 23: [10, inf] | arrested police attack | 2008_Mumbai_attacks |
| 39. | track | 23: [12, inf] | track – race | Race_track |
| 40. | beef | 24: [10, inf] | beef south korea | 2008_US_beef_protest_in_South_Korea |
| 41. | deal | 24: [10, inf] | deal u.s. iraq | Assassination_of_Qasem_Soleimani |
| 42. | mans | 24: [14, inf] | mans – race | 24_Hours_of_Le_Mans |
| 43. | lebanon | 25: [10, inf] | lebanon hezbollah israel | 2006_Lebanon_War |
| 44. | oil | 25: [13, inf], 44: [12, 6.0] | oil iraq deal | Iraq_War |
| 45. | ferry | 26: [10, inf] | ferry capsized philippine | MV_Princess_of_the_Stars |
| 46. | diplomatic | 29: [11, inf] | diplomatic u.s. president | President_of_the_United_States |
| 47. | paddock | 29: [12, inf] | paddock poker media | Stephen_Paddock |
| 48. | pope | 29: [12, inf] | pope benedict xvi | Pope_Benedict_XVI |
| 49. | karadzic | 30: [18, inf] | karadzic radovan arrest | Radovan_Karadžić |
| 50. | radovan | 30: [13, inf] | radovan karadzic crimes | Radovan_Karadžić |
| 51. | cambodia | 30: [10, inf] | cambodia thailand dispute | Cambodian–Thai_border_dispute |
| 52. | months | 31: [11, inf] | months two three | 3_Years,_5_Months_and_2_Days_in_the_Life_Of... |
| 53. | heikki | 31: [10, inf] | heikki kovalainen hamilton | Heikki_Kovalainen |
| 54. | solzhenitsyn | 32: [12, inf] | solzhenitsyn aleksandr russia | Aleksandr_Solzhenitsyn |
| 55. | kirkuk | 34: [18, inf] | kirkuk iraq city | Kirkuk |
| 56. | parliament | 35: [10, inf], 41: [13, inf], 47: [11, inf] | parliament president minister | Minister-president |
| 57. | say | 35: [10, 5.0], 42: [10, inf] | say officials u.s. | Threatening_government_officials_of_the_United_States |
| 58. | european | 36: [10, inf] | european union europe | European_Union |
| 59. | court | 37: [10, inf] | court ruling case | Lists_of_United_States_Supreme_Court_cases |
| 60. | troops | 37: [16, inf] | troops iraq iraqi | Iraq_War |
| 61. | leave | 37: [10, inf] | leave iraq u.s. | Iraq_War |
| 62. | sent | 37: [11, inf] | sent letter u.s. | Bixby_letter |
| 63. | engine | 38: [14, inf] | engine rules freeze | Honda_Indy_V8_engine |
| 64. | food | 38: [10, inf] | food china prices | Food_prices |
| 65. | women | 38: [10, inf] | women iraqi iraq | Women_in_Iraq |
| 66. | second | 41: [14, inf], 44: [11, inf] | second time – | Not_a_Second_Time |
| 67. | policy | 42: [10, inf] | policy u.s. president | Historical_rankings_of_presidents_of_the_United_States |
| 68. | plan | 42: [10, inf] | plan u.s. would | Operation_Northwoods |
| 69. | reform | 42: [10, inf] | reform rural president | Land_reform_in_the_Philippines |
| 70. | somalia | 44: [10, inf] | somalia government islamist | Somali_Civil_War_(2009–present) |
| 71. | missile | 45: [14, inf] | missile u.s. russia | Russia–United_States_relations |
| 72. | victory | 45: [11, inf] | victory president election | 2008_United_States_presidential_election |
| 73. | obama | 45: [10, inf] | obama barack president | Barack_Obama |
| 74. | mumbai | 48: [15, inf] | mumbai attacks india | 2008_Mumbai_attacks |
| 75. | meeting | 50: [12, inf] | meeting leaders president | Asia-Pacific_Economic_Cooperation |
| 76. | climate | 50: [10, inf] | climate treaty change | Climate_change |
| 77. | university | 51: [10, inf] | university baghdad bureau | Baghdad_Pact |
| 78. | family | 51: [10, inf] | family iraqi house | List_of_kings_of_Iraq |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | bush | 2: [10, inf] | bush george 's | George_H._W._Bush |
| 2. | basra | 13: [11, inf] | basra british battle | Battle_of_Basra_(2003) |
| 3. | quake | 20: [10, inf] | quake china shakes | 2008_Sichuan_earthquake |
| 4. | betancourt | 27: [13, inf] | betancourt ingrid hostage | Íngrid_Betancourt |
| 5. | radovan | 30: [13, inf] | radovan karadzic crimes | Trial_of_Radovan_Karadžić |
| 6. | karadzic | 30: [26, inf] | karadzic radovan crimes | Radovan_Karadžić |
| 7. | georgia | 32: [10, inf] | georgia russia russian | Georgia–Russia_relations |
| 8. | crash | 34: [10, inf] | crash plane madrid | Spanair_Flight_5022 |
| 9. | plane | 34: [11, inf] | plane crash madrid | Spanair_Flight_5022 |
| 10. | madrid | 34: [13, inf] | madrid crash plane | Spanair_Flight_5022 |
| 11. | congo | 44: [15, inf] | congo rebels 's | Simba_rebellion |
| 12. | reports | 45: [11, inf] | reports first world | First_World |
| 13. | mumbai | 48: [51, inf] | mumbai attacks terror | 2008_Mumbai_attacks |
| 14. | eyewitness | 52: [17, inf] | eyewitness burma account | Burmese_invasions_of_Assam |
