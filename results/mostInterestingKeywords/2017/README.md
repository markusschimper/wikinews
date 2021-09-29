# Keywords with the highest 'interestingness' in 2017

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
| 1. | trump | 1: [17, inf], 44: [36, inf] | trump president u.s. | Donald_Trump |
| 2. | mr. | 1: [11, inf], 26: [16, inf] | mr. trump president | Donald_Trump |
| 3. | would | 1: [11, inf], 13: [11, 11.0], 48: [17, 8.5] | would trump president | Donald_Trump |
| 4. | police | 1: [10, inf] | police attack officers | 2016_shooting_of_Dallas_police_officers |
| 5. | video | 1: [11, inf], 31: [12, 6.0] | video shows china | Vídeo_Show |
| 6. | minister | 1: [10, 10.0], 10: [15, inf], 16: [12, 12.0] | minister prime may | Prime_minister |
| 7. | official | 1: [10, inf] | official u.s. trump | List_of_Republicans_who_opposed_the_Donald_Trump_2020_presidential_campaign |
| 8. | year | 1: [15, 5.0], 11: [17, inf] | year last trump | Donald_Trump_(Last_Week_Tonight) |
| 9. | trial | 1: [10, inf] | trial president park | Impeachment_of_Park_Geun-hye |
| 10. | government | 1: [15, inf], 19: [12, 6.0] | government president says | Government_of_Russia |
| 11. | taiwan | 2: [10, inf] | taiwan china president | President_of_the_Republic_of_China |
| 12. | court | 3: [20, 10.0], 13: [16, 8.0], 23: [10, inf], 25: [14, 14.0] | court supreme president | Supreme_Court_of_the_United_States |
| 13. | camp | 3: [11, inf] | camp refugee people | Refugee_camp |
| 14. | order | 4: [10, inf] | order trump president | Donald_Trump |
| 15. | house | 5: [10, inf], 20: [13, 6.5] | house white trump | White_House_COVID-19_outbreak |
| 16. | iran | 5: [19, 6.33], 18: [14, inf], 37: [12, 6.0], 45: [11, 5.5] | iran trump president | Donald_Trump |
| 17. | near | 5: [11, inf], 16: [10, inf] | near attack police | Murder_of_Lee_Rigby |
| 18. | russia | 7: [20, inf], 30: [17, 5.67] | russia president trump | Donald_Trump |
| 19. | nato | 7: [11, 5.5], 21: [11, inf] | nato trump allies | Major_non-NATO_ally |
| 20. | vice | 7: [14, inf] | vice president pence | Mike_Pence |
| 21. | called | 10: [10, inf], 29: [10, 5.0] | called president trump | Donald_Trump |
| 22. | prime | 10: [13, inf] | prime minister may | Prime_minister |
| 23. | talks | 13: [10, inf] | talks north korea | North_Korea–South_Korea_relations |
| 24. | four | 14: [10, inf] | four attack killed | American_fatalities_and_injuries_of_the_2012_Benghazi_attack |
| 25. | syria | 14: [44, inf], 25: [15, 5.0], 35: [11, 11.0] | syria syrian u.s. | Syria_(region) |
| 26. | chemical | 14: [26, inf] | chemical syria attack | Ghouta_chemical_attack |
| 27. | missile | 14: [14, inf], 35: [19, 6.33], 48: [10, 10.0] | missile north korea | List_of_North_Korean_missile_tests |
| 28. | bomb | 15: [11, 11.0], 35: [18, inf] | bomb attack north | Suicide_attack |
| 29. | election | 16: [21, 10.5], 23: [25, 5.0], 31: [10, inf], 35: [11, 5.5], 37: [10, 5.0], 41: [11, 5.5] | election president party | 1828_United_States_presidential_election |
| 30. | political | 16: [11, inf] | political president minister | Minister_President_of_Prussia |
| 31. | macron | 16: [12, inf], 28: [10, 5.0] | macron france emmanuel | Emmanuel_Macron |
| 32. | land | 16: [10, inf] | land canada many | Canadian_Army |
| 33. | base | 16: [10, inf] | base military afghan | Afghan_Armed_Forces |
| 34. | system | 17: [11, inf] | system korea south | Education_in_South_Korea |
| 35. | campaign | 18: [12, 6.0], 37: [10, inf], 44: [10, 10.0] | campaign president trump | Donald_Trump |
| 36. | moon | 19: [17, inf] | moon korea south | Moon_Jae-in |
| 37. | jae-in | 19: [14, inf] | jae-in korea south | Moon_Jae-in |
| 38. | says | 20: [20, inf] | says president trump | Donald_Trump |
| 39. | saudi | 20: [14, inf], 44: [10, 5.0] | saudi arabia prince | Crown_Prince_of_Saudi_Arabia |
| 40. | manchester | 21: [38, inf] | manchester attack bomber | Manchester_Arena_bombing |
| 41. | concert | 21: [13, inf] | concert manchester bombing | Manchester_Arena_bombing |
| 42. | bombing | 21: [18, inf] | bombing attack killed | Centennial_Olympic_Park_bombing |
| 43. | bomber | 21: [14, inf] | bomber suicide manchester | Manchester_Arena_bombing |
| 44. | allies | 21: [11, inf], 23: [11, inf] | allies trump president | Donald_Trump |
| 45. | trade | 22: [10, inf] | trade trump china | China–United_States_trade_war |
| 46. | kabul | 22: [14, inf] | kabul afghan attack | Kabul |
| 47. | qatar | 23: [15, inf] | qatar gulf arab | Gulf_Cooperation_Council |
| 48. | warmbier | 24: [11, inf] | warmbier north korea | Otto_Warmbier |
| 49. | fire | 24: [10, inf] | fire london grenfell | Grenfell_Tower_fire |
| 50. | tower | 24: [10, inf] | tower london fire | Grenfell_Tower_fire |
| 51. | spyware | 25: [10, inf] | spyware government mexican | Pegasus_(spyware) |
| 52. | south | 25: [13, inf] | south korea north | North_Korea–South_Korea_relations |
| 53. | day | 26: [11, inf] | day president trump | Donald_Trump |
| 54. | hong | 26: [15, inf] | hong kong china | Hong_Kong |
| 55. | kong | 26: [15, inf] | kong hong china | Hong_Kong |
| 56. | cardinal | 26: [11, inf] | cardinal pell pope | George_Pell |
| 57. | hospital | 27: [11, inf] | hospital oxygen attack | Oxygen_therapy |
| 58. | world | 27: [15, 7.5], 38: [13, inf] | world trump president | Donald_Trump |
| 59. | woman | 29: [10, inf] | woman police american | Joan_As_Police_Woman |
| 60. | sharif | 30: [14, inf] | sharif pakistan nawaz | Maryam_Nawaz |
| 61. | pakistan | 30: [12, inf] | pakistan sharif minister | Nawaz_Sharif |
| 62. | foreign | 31: [10, inf], 49: [12, inf] | foreign trump minister | Foreign_policy_of_the_Donald_Trump_administration |
| 63. | guam | 32: [14, inf] | guam north korea | Andersen_Air_Force_Base |
| 64. | spain | 33: [12, inf] | spain catalonia independence | Catalan_declaration_of_independence |
| 65. | investigators | 33: [10, inf] | investigators say u.n. | Special_Counsel_investigation_(2017–2019) |
| 66. | people | 33: [13, inf], 51: [20, 10.0] | people killed least | List_of_people_killed_for_being_transgender |
| 67. | singapore | 34: [12, inf] | singapore navy mccain | USS_John_S._McCain_(DDG-56) |
| 68. | diana | 35: [13, inf] | diana death princess | Death_of_Diana,_Princess_of_Wales |
| 69. | hydrogen | 35: [10, inf] | hydrogen bomb north | Thermonuclear_weapon |
| 70. | next | 36: [13, inf], 50: [10, 5.0] | next president trump | Donald_Trump |
| 71. | hurricane | 36: [20, inf] | hurricane storm caribbean | Hurricane_Eta |
| 72. | irma | 36: [11, inf] | irma hurricane caribbean | Hurricane_Irma |
| 73. | national | 37: [11, inf], 40: [11, inf] | national party president | List_of_presidents_of_the_Bharatiya_Janata_Party |
| 74. | quake | 38: [14, inf] | quake mexico earthquake | 2017_Puebla_earthquake |
| 75. | deal | 40: [10, inf], 48: [10, 5.0] | deal trump iran | United_States_withdrawal_from_the_Joint_Comprehensive_Plan_of_Action |
| 76. | journalist | 40: [11, inf] | journalist wall killing | Murder_of_Kim_Wall |
| 77. | state | 42: [12, inf] | state islamic isis | Islamic_State_of_Iraq_and_the_Levant |
| 78. | isis | 42: [16, inf] | isis state islamic | Islamic_State_of_Iraq_and_the_Levant |
| 79. | mattis | 43: [10, inf] | mattis defense secretary | Jim_Mattis |
| 80. | decision | 49: [16, inf] | decision court president | Supreme_Court_of_the_United_States |
| 81. | african | 50: [10, inf] | african migrants south | Migrants'_African_routes |
| 82. | christmas | 51: [11, inf] | christmas queen day | Royal_Christmas_Message |
| 83. | fujimori | 52: [10, inf] | fujimori peru president | Alberto_Fujimori |
| 84. | star | 52: [10, inf] | star party mr. | Jeffree_Star |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | terror | 33: [11, inf] | terror attack attacks | 2008_Mumbai_attacks |
| 2. | irma | 36: [27, inf] | irma hurricane caribbean | Hurricane_Irma |
| 3. | maria | 38: [12, inf] | maria hurricane puerto | Hurricane_Maria |
| 4. | zimbabwe | 46: [14, inf] | zimbabwe mugabe 's | Robert_Mugabe |
