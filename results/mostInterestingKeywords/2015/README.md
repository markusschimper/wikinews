# Keywords with the highest 'interestingness' in 2015

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
| 1. | french | 2: [16, inf], 46: [10, 5.0] | french france paris | Paris |
| 2. | france | 2: [11, inf], 31: [13, 6.5] | france french paris | Paris |
| 3. | country | 2: [10, 5.0], 21: [13, 6.5], 31: [15, inf] | country president china | President_of_the_Republic_of_China |
| 4. | germany | 2: [11, inf], 19: [13, 6.5] | germany migrants german | Germany |
| 5. | paris | 2: [34, 17.0], 46: [30, inf] | paris attacks france | November_2015_Paris_attacks |
| 6. | political | 2: [13, inf] | political party president | Political_parties_in_the_United_States |
| 7. | sri | 2: [16, inf] | sri lanka president | President_of_Sri_Lanka |
| 8. | lanka | 2: [13, inf] | lanka sri president | President_of_Sri_Lanka |
| 9. | charlie | 2: [23, inf] | charlie hebdo newspaper | Charlie_Hebdo |
| 10. | hebdo | 2: [21, inf] | hebdo charlie newspaper | Charlie_Hebdo |
| 11. | satirical | 2: [13, inf] | satirical charlie hebdo | Charlie_Hebdo |
| 12. | qaeda | 2: [11, inf] | qaeda yemen killed | Al-Qaeda_in_the_Arabian_Peninsula |
| 13. | united | 2: [10, inf], 50: [14, 14.0] | united states nations | Member_states_of_the_United_Nations |
| 14. | states | 2: [10, inf], 5: [13, 6.5] | states united u.s. | U.S._state |
| 15. | talks | 2: [12, inf], 10: [13, 6.5] | talks iran nuclear | Iran_nuclear_deal_framework |
| 16. | nuclear | 2: [10, inf], 18: [10, 5.0], 26: [18, inf], 36: [13, 6.5] | nuclear iran deal | Iran_nuclear_deal_framework |
| 17. | pope | 3: [17, inf], 48: [13, inf] | pope francis church | Pope_Francis |
| 18. | speech | 3: [11, inf], 9: [10, 5.0], 39: [10, 5.0] | speech president minister | Blood_and_Iron_(speech) |
| 19. | groups | 3: [10, inf], 24: [12, 6.0] | groups rights government | Individual_and_group_rights |
| 20. | cover | 3: [11, inf] | cover charlie hebdo | Charlie_Hebdo |
| 21. | syria | 3: [11, inf] | syria state islamic | Islamic_State_of_Iraq_and_the_Levant |
| 22. | diplomatic | 4: [11, inf] | diplomatic obama syria | Foreign_policy_of_the_Barack_Obama_administration |
| 23. | agency | 5: [13, inf], 18: [10, 5.0], 49: [10, 5.0] | agency news state | Xinhua_News_Agency |
| 24. | jordan | 5: [13, inf] | jordan state pilot | Muath_al-Kasasbeh |
| 25. | afghanistan | 7: [10, inf], 40: [10, 5.0] | afghanistan taliban afghan | War_in_Afghanistan_(2001–present) |
| 26. | xi | 7: [10, inf], 39: [33, 5.5], 45: [11, 5.5] | xi jinping china | Xi_Jinping_Thought |
| 27. | air | 7: [12, 6.0], 29: [10, inf] | air pollution beijing | Pollution_in_China |
| 28. | battle | 8: [10, 5.0], 50: [11, inf] | battle state forces | Battle_of_Hastings |
| 29. | capital | 8: [10, inf], 25: [10, 10.0] | capital yemen government | Capital_of_Yemen |
| 30. | party | 9: [18, inf], 11: [10, 5.0], 25: [16, 8.0], 40: [17, 8.5] | party china communist | Chinese_Communist_Party |
| 31. | site | 10: [11, inf] | site attack killed | List_of_fatal_bear_attacks_in_North_America |
| 32. | flight | 10: [11, inf] | flight malaysia airlines | Malaysia_Airlines_Flight_370 |
| 33. | british | 11: [17, inf] | british international herald | Handley_Page_Dart_Herald |
| 34. | workers | 11: [10, inf] | workers aid china | Humanitarian_aid |
| 35. | chief | 12: [12, inf] | chief former official | Chief_Justice_of_India |
| 36. | bomb | 12: [11, 5.5], 32: [14, inf] | bomb kills attack | Centennial_Olympic_Park_bombing |
| 37. | yemen | 12: [10, inf], 23: [14, 14.0] | yemen houthi rebels | Houthi_movement |
| 38. | plane | 13: [13, 13.0], 45: [13, inf] | plane crash flight | US_Airways_Flight_1549 |
| 39. | knox | 13: [10, inf] | knox court amanda | Amanda_Knox |
| 40. | seeks | 13: [10, inf] | seeks china minister | The_Foreigner_(2017_film) |
| 41. | germanwings | 13: [19, inf] | germanwings crash pilot | Germanwings_Flight_9525 |
| 42. | buhari | 14: [10, inf] | buhari muhammadu president | Cabinet_of_President_Muhammadu_Buhari |
| 43. | activist | 14: [10, inf], 22: [10, 10.0] | activist rights police | List_of_assassinated_human_rights_activists |
| 44. | could | 16: [12, inf], 49: [10, inf] | could greece iran | Iran |
| 45. | european | 16: [14, inf], 51: [10, inf] | european union crisis | European_debt_crisis |
| 46. | pakistan | 17: [13, inf] | pakistan killed attack | 2001_Indian_Parliament_attack |
| 47. | plans | 17: [10, inf] | plans president minister | Union_Council_of_Ministers |
| 48. | pakistani | 17: [10, 5.0], 21: [10, inf] | pakistani pakistan officials | Pakistan |
| 49. | earthquake | 17: [11, inf], 38: [10, inf] | earthquake nepal relief | April_2015_Nepal_earthquake |
| 50. | nepal | 17: [11, inf] | nepal earthquake quake | April_2015_Nepal_earthquake |
| 51. | miliband | 18: [10, inf] | miliband leader party | Ed_Miliband |
| 52. | modi | 20: [10, inf] | modi minister prime | Narendra_Modi |
| 53. | axact | 21: [12, inf] | axact company fake | Axact |
| 54. | marriage | 21: [16, inf] | marriage same-sex gay | Same-sex_marriage_in_the_United_States |
| 55. | union | 22: [12, 6.0], 36: [14, inf] | union european minister | Council_of_the_European_Union |
| 56. | ivory | 22: [10, inf] | ivory trade illegal | Ivory_trade |
| 57. | major | 22: [10, inf] | major first china | Paramount_leader |
| 58. | ties | 23: [11, inf] | ties china president | President_of_the_Republic_of_China |
| 59. | yangtze | 23: [15, inf] | yangtze ship capsized | Sinking_of_Dongfang_zhi_Xing |
| 60. | disaster | 23: [11, inf] | disaster yangtze ship | Yangtze |
| 61. | ban | 23: [10, 5.0], 33: [11, inf] | ban u.n. iran | Ban_Ki-moon |
| 62. | forces | 23: [11, inf], 40: [10, 10.0] | forces military iraqi | Iraqi_Armed_Forces |
| 63. | iraq | 24: [10, inf] | iraq isis state | Islamic_State_of_Iraq_and_the_Levant |
| 64. | korean | 24: [13, inf] | korean south north | North_Korea–South_Korea_relations |
| 65. | weapons | 25: [10, inf] | weapons nuclear iran | Nuclear_program_of_Iran |
| 66. | yoga | 25: [10, inf] | yoga modi day | International_Day_of_Yoga |
| 67. | change | 25: [14, inf], 50: [15, 7.5] | change climate pope | Climate_change_denial |
| 68. | debt | 26: [10, inf] | debt greek greece | Greek_government-debt_crisis |
| 69. | karachi | 26: [10, inf] | karachi pakistan city | Karachi |
| 70. | referendum | 27: [15, inf] | referendum vote marriage | Thirty-fourth_Amendment_of_the_Constitution_of_Ireland |
| 71. | tsipras | 27: [11, inf] | tsipras alexis greece | Alexis_Tsipras |
| 72. | europe | 27: [12, inf] | europe migrants crisis | European_migrant_crisis |
| 73. | jihadist | 27: [10, inf] | jihadist killed attacks | Islamic_terrorism_in_Europe |
| 74. | year | 29: [11, inf], 42: [10, 10.0] | year last china | Chinese_New_Year |
| 75. | video | 29: [12, inf], 37: [11, inf] | video state isis | Islamic_State_of_Iraq_and_the_Levant |
| 76. | escape | 29: [11, inf] | escape chapo guzmán | Joaquín_"El_Chapo"_Guzmán |
| 77. | defense | 30: [10, 5.0], 51: [14, inf] | defense u.s. carter | Ash_Carter |
| 78. | kenya | 30: [12, inf] | kenya obama president | Barack_Obama_Sr. |
| 79. | inquiry | 31: [12, inf] | inquiry united investigation | Special_Counsel_investigation_(2017–2019) |
| 80. | taliban | 31: [20, 20.0], 40: [20, 20.0], 48: [10, inf] | taliban afghan afghanistan | War_in_Afghanistan_(2001–present) |
| 81. | mullah | 31: [11, inf] | mullah taliban leader | List_of_Taliban_leaders |
| 82. | hiroshima | 32: [10, inf] | hiroshima atomic bomb | Atomic_bombings_of_Hiroshima_and_Nagasaki |
| 83. | survivors | 32: [11, inf] | survivors people ship | The_captain_goes_down_with_the_ship |
| 84. | bombing | 32: [11, inf] | bombing president killed | Centennial_Olympic_Park_bombing |
| 85. | train | 34: [14, inf] | train attack troops | Shock_troops |
| 86. | austria | 35: [10, inf] | austria migrants truck | List_of_migrant_vehicle_incidents_in_Europe |
| 87. | queen | 37: [14, inf] | queen elizabeth international | Elizabeth_II |
| 88. | elizabeth | 37: [26, inf] | elizabeth queen international | Elizabeth_II |
| 89. | princess | 37: [10, inf] | princess elizabeth international | Princess_Elizabeth_of_Yugoslavia |
| 90. | top | 38: [11, inf] | top china officials | Scholar-official |
| 91. | kunduz | 40: [22, inf] | kunduz taliban afghan | War_in_Afghanistan_(2001–present) |
| 92. | worker | 40: [12, inf] | worker aid officials | Humanitarian_aid |
| 93. | many | 41: [18, inf], 44: [10, 10.0] | many china president | List_of_Chinese_leaders |
| 94. | turkey | 41: [10, inf], 48: [16, 5.33], 51: [13, 13.0] | turkey turkish syria | Syria–Turkey_relations |
| 95. | nobel | 41: [20, inf] | nobel prize peace | Nobel_Peace_Prize |
| 96. | east | 42: [10, inf] | east middle china | Middle_East |
| 97. | trudeau | 43: [13, inf] | trudeau justin canada | Justin_Trudeau |
| 98. | arabia | 44: [10, inf] | arabia saudi yemen | Saudi_Arabian-led_intervention_in_Yemen |
| 99. | child | 44: [15, inf] | child abuse children | Child_sexual_abuse |
| 100. | fire | 44: [10, inf] | fire police killed | List_of_law_enforcement_officers_killed_in_the_line_of_duty_in_the_United_States |
| 101. | house | 44: [10, inf] | house white obama | Presidency_of_Barack_Obama |
| 102. | taiwan | 45: [14, inf] | taiwan china president | President_of_the_Republic_of_China |
| 103. | detention | 46: [11, inf] | detention rights center | Youth_detention_center |
| 104. | mali | 47: [20, inf] | mali attack killed | Mali_War |
| 105. | britain | 48: [13, inf] | britain international herald | The_Herald_(Glasgow) |
| 106. | francis | 48: [12, inf] | francis pope church | Pope_Francis |
| 107. | german | 49: [10, inf] | german international herald | Michael_Diekmann |
| 108. | victory | 50: [11, inf] | victory party minister | List_of_prime_ministers_of_India |
| 109. | christmas | 52: [16, inf] | christmas international herald | Christmas |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | charlie | 2: [34, inf] | charlie hebdo attack | Charlie_Hebdo_shooting |
| 2. | hebdo | 2: [34, inf] | hebdo charlie attack | Charlie_Hebdo_shooting |
| 3. | paris | 2: [18, inf], 46: [44, inf] | paris attacks attack | November_2015_Paris_attacks |
| 4. | syriza | 5: [10, inf] | syriza greece greek | Syriza |
| 5. | plane | 13: [10, inf] | plane crash russian | Lokomotiv_Yaroslavl_plane_crash |
| 6. | germanwings | 13: [29, inf] | germanwings crash flight | Germanwings_Flight_9525 |
| 7. | flight | 13: [10, inf] | flight germanwings mh | Malaysia_Airlines_Flight_370_disappearance_theories |
| 8. | crash | 13: [22, inf] | crash plane germanwings | Germanwings_Flight_9525 |
| 9. | crisis | 17: [10, inf] | crisis refugee greek | Refugee_crisis |
| 10. | nepal | 17: [10, inf] | nepal earthquake quake | April_2015_Nepal_earthquake |
| 11. | charleston | 25: [19, inf] | charleston shooting church | Charleston_church_shooting |
| 12. | shooting | 25: [15, inf] | shooting charleston suspect | Charleston_church_shooting |
| 13. | tunisia | 26: [19, inf] | tunisia attack beach | 2015_Sousse_attacks |
| 14. | mh | 31: [11, inf] | mh debris crash | Malaysia_Airlines_Flight_370 |
| 15. | bangkok | 34: [10, inf] | bangkok bombing thai | 2015_Bangkok_bombing |
| 16. | bit | 37: [10, inf] | bit 's best | Bit_rate |
| 17. | sharm | 45: [10, inf] | sharm el-sheikh flights | Sharm_El_Sheikh |
| 18. | el-sheikh | 45: [10, inf] | el-sheikh sharm flights | Sharm_El_Sheikh |
| 19. | airstrikes | 47: [10, inf] | airstrikes syria isis | International_military_intervention_against_ISIL |
