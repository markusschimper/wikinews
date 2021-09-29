# Keywords with the highest 'interestingness' in 2016

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
| 1. | states | 1: [17, inf] | states united u.s. | U.S._state |
| 2. | united | 1: [21, inf], 36: [20, 5.0] | united states nations | Member_states_of_the_United_Nations |
| 3. | political | 1: [10, inf], 17: [15, 5.0], 26: [15, 7.5] | political president government | President_(government_title) |
| 4. | would | 1: [11, inf], 4: [17, 17.0] | would president says | President_of_the_United_States |
| 5. | reports | 1: [10, inf] | reports news united | U.S._News_&_World_Report |
| 6. | death | 1: [10, inf], 26: [10, 10.0] | death police people | Saskatoon_freezing_deaths |
| 7. | korea | 1: [14, inf], 22: [16, 8.0] | korea north south | North_Korea–South_Korea_relations |
| 8. | attacks | 1: [11, inf], 51: [10, inf] | attacks brussels paris | 2016_Brussels_bombings |
| 9. | months | 1: [10, inf] | months government two | Month |
| 10. | u.s. | 1: [10, 5.0], 26: [10, inf] | u.s. american united | United_States |
| 11. | police | 1: [11, 11.0], 10: [13, inf], 29: [16, 5.33], 34: [19, 9.5], 40: [15, 5.0], 51: [15, 7.5] | police attack killed | 2016_shooting_of_Dallas_police_officers |
| 12. | iraq | 1: [10, inf], 8: [10, 5.0], 27: [14, inf], 42: [13, 13.0] | iraq isis syria | Islamic_State_of_Iraq_and_the_Levant |
| 13. | isis | 1: [11, inf], 26: [17, 17.0] | isis state islamic | Islamic_State_of_Iraq_and_the_Levant |
| 14. | roosevelt | 1: [10, inf], 15: [10, 10.0] | roosevelt international herald | Roosevelt_dictatorship |
| 15. | say | 1: [10, inf], 40: [18, 18.0] | say officials police | SayHerName |
| 16. | release | 2: [10, inf] | release iran u.s. | Iran–United_States_relations |
| 17. | taiwan | 2: [17, inf], 15: [15, inf] | taiwan china president | President_of_the_Republic_of_China |
| 18. | burkina | 2: [10, inf] | burkina faso ouagadougou | Ouagadougou |
| 19. | faso | 2: [10, inf] | faso burkina ouagadougou | Ouagadougou |
| 20. | week | 3: [12, 6.0], 29: [10, inf] | week last china | Last_Week_Tonight_with_John_Oliver |
| 21. | women | 4: [13, inf], 10: [12, 6.0] | women female year | List_of_female_spacefarers |
| 22. | center | 4: [10, inf] | center city detention | Baltimore_City_Detention_Center |
| 23. | seven | 5: [10, inf] | seven years officials | Seven_Years_in_Tibet_(1997_film) |
| 24. | israel | 6: [10, 10.0], 26: [15, 5.0], 35: [11, 11.0], 37: [14, inf] | israel israeli palestinian | Israeli–Palestinian_conflict |
| 25. | arab | 6: [12, inf] | arab emirates united | United_Arab_Emirates |
| 26. | nuclear | 6: [10, 10.0], 31: [10, inf] | nuclear north korea | North_Korea_and_weapons_of_mass_destruction |
| 27. | rights | 7: [11, 5.5], 10: [10, 5.0], 23: [11, 5.5], 31: [15, inf], 34: [10, inf] | rights human china | Human_rights_in_China |
| 28. | vote | 7: [10, inf], 15: [10, 5.0] | vote britain union | Brexit |
| 29. | turkey | 7: [16, inf], 28: [27, 13.5] | turkey erdogan president | Recep_Tayyip_Erdoğan |
| 30. | border | 7: [12, 6.0], 24: [13, inf] | border killed near | Deaths_along_the_Bangladesh–India_border |
| 31. | obama | 10: [14, inf], 12: [30, 5.0], 16: [21, 5.25], 35: [12, 6.0], 46: [17, 5.67] | obama president u.s. | Barack_Obama |
| 32. | syria | 11: [14, inf] | syria russia united | Russian_military_intervention_in_the_Syrian_Civil_War |
| 33. | panama | 14: [20, inf] | panama papers minister | Panama_Papers |
| 34. | papers | 14: [19, inf] | papers panama minister | Panama_Papers |
| 35. | law | 14: [13, inf] | law international china | Chinese_law |
| 36. | leaked | 14: [10, inf] | leaked papers panama | Panama_Papers |
| 37. | offshore | 14: [10, inf] | offshore panama papers | Panama_Papers |
| 38. | official | 14: [10, 10.0], 34: [10, inf] | official says china | SAIC-GM |
| 39. | city | 15: [10, inf], 24: [14, 7.0] | city aleppo china | Ancient_City_of_Aleppo |
| 40. | britain | 16: [12, inf] | britain european union | Brexit |
| 41. | fort | 18: [12, inf] | fort mcmurray alberta | Fort_McMurray |
| 42. | mcmurray | 18: [11, inf] | mcmurray fort alberta | Fort_McMurray |
| 43. | nigeria | 19: [13, inf] | nigeria boko haram | Boko_Haram |
| 44. | bbc | 19: [10, inf] | bbc inquiry savile | Jimmy_Savile_sexual_abuse_scandal |
| 45. | moves | 20: [10, inf] | moves u.s. president | Historical_rankings_of_presidents_of_the_United_States |
| 46. | made | 20: [10, inf], 40: [10, 5.0] | made president china | President_of_the_People's_Republic_of_China |
| 47. | plane | 20: [17, inf] | plane crash flight | US_Airways_Flight_1549 |
| 48. | egyptair | 20: [13, inf] | egyptair flight plane | EgyptAir_Flight_804 |
| 49. | flight | 20: [10, inf] | flight plane egyptair | EgyptAir_Flight_804 |
| 50. | vietnam | 20: [10, inf] | vietnam international herald | Hoàng_Thùy_Linh |
| 51. | hiroshima | 21: [25, inf] | hiroshima obama visit | Barack_Obama |
| 52. | beijing | 22: [13, inf], 45: [11, 5.5] | beijing china chinese | Beijing |
| 53. | tiger | 22: [12, inf] | tiger temple officials | Tiger_Temple |
| 54. | temple | 22: [10, inf] | temple tiger officials | Tiger_Temple |
| 55. | troops | 24: [12, inf] | troops international herald | Insurgency_in_the_Maghreb_(2002–present) |
| 56. | protest | 24: [11, inf] | protest government president | Protest |
| 57. | cox | 24: [11, inf] | cox mair killing | Murder_of_Jo_Cox |
| 58. | referendum | 25: [11, inf] | referendum britain vote | 2016_United_Kingdom_European_Union_membership_referendum |
| 59. | election | 26: [12, 12.0], 31: [14, 7.0], 48: [11, inf] | election party president | 2012_United_States_presidential_election |
| 60. | two | 26: [17, 17.0], 51: [10, inf] | two killed years | Kill_Bill:_Volume_2 |
| 61. | assault | 26: [10, inf] | assault attack police | Alleged_assault_of_Jussie_Smollett |
| 62. | groups | 26: [12, inf] | groups rights say | Men's_rights_movement |
| 63. | climate | 26: [10, inf] | climate change trump | Environmental_policy_of_the_Donald_Trump_administration |
| 64. | july | 26: [11, inf] | july international archives | Archive |
| 65. | battle | 26: [16, inf], 42: [10, 10.0] | battle killed mosul | Battle_of_Mosul_(2016–17) |
| 66. | civilians | 28: [10, inf] | civilians killed syrian | Casualties_of_the_Syrian_Civil_War |
| 67. | korean | 28: [15, inf] | korean south north | North_Korea–South_Korea_relations |
| 68. | nice | 28: [21, inf] | nice attack truck | 2016_Nice_truck_attack |
| 69. | truck | 28: [16, inf], 51: [10, inf] | truck attack nice | 2016_Nice_truck_attack |
| 70. | coup | 28: [21, inf] | coup turkey erdogan | 2016_Turkish_coup_d'état_attempt |
| 71. | group | 29: [10, 5.0], 31: [11, inf] | group killed militant | Al-Shabaab_(militant_group) |
| 72. | trump | 29: [12, inf], 45: [49, 12.25] | trump donald j. | Donald_Trump |
| 73. | pope | 30: [16, inf], 44: [14, inf] | pope francis church | Pope_Francis |
| 74. | francis | 30: [10, inf] | francis pope church | Pope_Francis |
| 75. | kong | 33: [11, inf] | kong hong china | Hong_Kong |
| 76. | haiti | 33: [11, inf] | haiti cholera hurricane | 2010s_Haiti_cholera_outbreak |
| 77. | cholera | 33: [11, inf] | cholera haiti united | 2010s_Haiti_cholera_outbreak |
| 78. | italy | 34: [11, inf] | italy italian renzi | Matteo_Renzi |
| 79. | debate | 35: [10, inf] | debate china lawmakers | 2036:_Nexus_Dawn |
| 80. | west | 35: [11, inf] | west bank palestinian | Palestinian_territories |
| 81. | september | 35: [12, inf] | september archives international | Archive |
| 82. | near | 36: [14, inf] | near killed attack | List_of_fatal_cougar_attacks_in_North_America |
| 83. | become | 36: [10, inf] | become president china | President_of_the_Republic_of_China |
| 84. | opposition | 37: [10, inf] | opposition leader president | Leader_of_the_Opposition_(India) |
| 85. | myanmar | 37: [10, inf] | myanmar aung san | Aung_San_Suu_Kyi |
| 86. | policy | 38: [11, inf] | policy foreign china | Foreign_policy_of_China |
| 87. | global | 38: [10, inf] | global foreign china | China_Global_Television_Network |
| 88. | shimon | 39: [10, inf] | shimon peres israel | Shimon_Peres |
| 89. | peres | 39: [14, inf] | peres shimon israel | Shimon_Peres |
| 90. | matthew | 40: [10, inf] | matthew hurricane haiti | Effects_of_Hurricane_Matthew_in_Haiti |
| 91. | storm | 40: [10, inf] | storm least hurricane | 2020_Atlantic_hurricane_season |
| 92. | taliban | 40: [10, inf] | taliban afghan afghanistan | War_in_Afghanistan_(2001–present) |
| 93. | religious | 40: [10, inf] | religious pope president | Pope_Francis |
| 94. | toward | 40: [10, inf] | toward china leader | China |
| 95. | king | 41: [11, inf] | king international herald | The_New_York_Times_International_Edition |
| 96. | aid | 42: [10, inf] | aid syria united | Syrian_civil_war |
| 97. | known | 44: [11, inf] | known group last | List_of_languages_by_time_of_extinction |
| 98. | j. | 45: [10, inf] | j. trump donald | Donald_Trump |
| 99. | free | 46: [10, inf] | free north minister | North_American_Free_Trade_Agreement |
| 100. | language | 47: [11, inf] | language say china | China_Can_Say_No |
| 101. | castro | 47: [11, inf] | castro cuba obama | Raúl_Castro |
| 102. | paris | 50: [10, inf] | paris attacks international | November_2015_Paris_attacks |
| 103. | berlin | 51: [26, inf] | berlin attack germany | 2016_Berlin_truck_attack |
| 104. | amri | 51: [10, inf] | amri berlin anis | 2016_Berlin_truck_attack |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | test | 1: [14, inf] | test north korea | List_of_North_Korean_missile_tests |
| 2. | north | 1: [16, inf] | north korea nuclear | North_Korea_and_weapons_of_mass_destruction |
| 3. | korea | 1: [14, inf] | korea north nuclear | North_Korea_and_weapons_of_mass_destruction |
| 4. | nuclear | 1: [14, inf] | nuclear north korea | North_Korea_and_weapons_of_mass_destruction |
| 5. | chapo | 1: [11, inf] | chapo 's mexico | Joaquín_"El_Chapo"_Guzmán |
| 6. | easter | 12: [11, inf] | easter rising irish | Easter_Rising |
| 7. | egyptair | 20: [15, inf] | egyptair flight ms | EgyptAir_Flight_804 |
| 8. | ms | 20: [13, inf] | ms egyptair flight | EgyptAir_Flight_648 |
| 9. | truck | 28: [11, inf] | truck nice attack | 2016_Nice_truck_attack |
| 10. | nice | 28: [27, inf] | nice attack truck | 2016_Nice_truck_attack |
| 11. | turkey | 28: [20, inf] | turkey 's coup | 2016_Turkish_coup_d'état_attempt |
| 12. | munich | 29: [13, inf] | munich 's attack | Munich_massacre |
| 13. | italy | 34: [12, inf] | italy 's earthquake | List_of_earthquakes_in_Italy |
| 14. | earthquake | 34: [14, inf] | earthquake italy zealand | August_2016_Central_Italy_earthquake |
| 15. | hurricane | 40: [10, inf] | hurricane matthew haiti | Hurricane_Matthew |
| 16. | matthew | 40: [11, inf] | matthew hurricane haiti | Effects_of_Hurricane_Matthew_in_Haiti |
| 17. | trump | 45: [13, inf] | trump 's donald | Donald_Trump |
| 18. | castro | 47: [22, inf] | castro fidel 's | Fidel_Castro |
| 19. | fidel | 47: [15, inf] | fidel castro 's | Fidel_Castro |
| 20. | chapecoense | 48: [11, inf] | chapecoense plane crash | LaMia_Flight_2933 |
| 21. | plane | 48: [14, inf] | plane crash mh | Aviation_accidents_and_incidents |
| 22. | berlin | 51: [23, inf] | berlin attack suspect | 2016_Berlin_truck_attack |
