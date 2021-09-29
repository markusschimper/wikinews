# Keywords with the highest 'interestingness' in 2006

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
| 1. | leader | 1: [38, inf], 48: [34, 5.67] | leader 's president | Party_leaders_of_the_United_States_Senate |
| 2. | two | 1: [37, inf] | two 's government | Two_Treatises_of_Government |
| 3. | tuesday | 1: [16, inf], 36: [20, 6.67] | tuesday 's mr. | Tuesday_Weld |
| 4. | country | 1: [22, inf] | country 's government | List_of_countries_by_government_budget |
| 5. | international | 1: [13, inf] | international 's iran | Iran_International |
| 6. | even | 1: [10, inf], 8: [10, 10.0], 52: [14, inf] | even 's iraq | Iraqi_Army |
| 7. | several | 1: [10, inf], 17: [14, 14.0] | several 's government | Federal_government_of_the_United_States |
| 8. | recent | 1: [12, inf] | recent 's mr. | Mr._Bean |
| 9. | since | 1: [13, inf] | since 's government | Federal_government_of_the_United_States |
| 10. | election | 1: [16, inf], 26: [32, 32.0] | election 's president | United_States_presidential_election |
| 11. | mr. | 1: [55, inf], 14: [88, 5.5], 42: [16, 16.0] | mr. 's president | Mr._President_(title) |
| 12. | iran | 1: [36, inf], 46: [24, 8.0] | iran nuclear 's | Nuclear_program_of_Iran |
| 13. | says | 1: [10, inf] | says 's government | Say's_law |
| 14. | nuclear | 1: [30, inf], 7: [33, 33.0], 34: [38, 6.33], 46: [21, 10.5] | nuclear iran 's | Nuclear_program_of_Iran |
| 15. | research | 1: [15, inf] | research nuclear iran | Nuclear_facilities_in_Iran |
| 16. | dispute | 1: [22, 11.0], 7: [10, 10.0], 24: [10, inf] | dispute 's russia | 2009_Russia–Ukraine_gas_dispute |
| 17. | southern | 1: [12, inf], 9: [10, 5.0], 18: [18, 9.0] | southern lebanon israel | Israeli_occupation_of_Southern_Lebanon |
| 18. | obituary | 1: [15, inf] | obituary dead writer | List_of_premature_obituaries |
| 19. | campaign | 1: [12, inf] | campaign 's government | Campaign_for_World_Government |
| 20. | briefs | 1: [12, inf] | briefs 's europe | Swim_briefs |
| 21. | sharon | 1: [62, inf], 12: [12, inf] | sharon 's prime | Ariel_Sharon |
| 22. | authorities | 1: [13, 13.0], 26: [17, inf] | authorities 's russian | Anti-gay_purges_in_Chechnya |
| 23. | border | 1: [20, 20.0], 5: [11, 5.5], 12: [17, inf], 15: [13, inf], 26: [13, 6.5], 35: [36, 18.0], 46: [16, 5.33], 52: [15, inf] | border israel israeli | Borders_of_Israel |
| 24. | chirac | 1: [16, inf], 7: [16, 8.0], 13: [30, 30.0], 43: [10, 10.0] | chirac france 's | Jacques_Chirac |
| 25. | iraq | 1: [50, inf] | iraq 's iraqi | Iraqi_Kurdistan |
| 26. | energy | 1: [14, inf], 4: [17, 8.5], 23: [10, inf], 47: [11, inf], 50: [11, 11.0], 52: [20, 6.67] | energy 's iran | Energy_in_Iran |
| 27. | lobbyist | 1: [12, inf] | lobbyist park united | David_Bernhardt |
| 28. | vote | 1: [12, 12.0], 26: [18, 6.0], 30: [12, inf], 43: [19, 6.33] | vote 's election | Electoral_fraud |
| 29. | would | 1: [24, inf] | would 's government | Federal_government_of_the_United_States |
| 30. | rink | 1: [12, inf] | rink roof collapse | Bad_Reichenhall_Ice_Rink_roof_collapse |
| 31. | dead | 1: [24, 24.0], 19: [15, 5.0], 29: [20, 6.67], 38: [10, 5.0], 40: [20, inf], 51: [12, 6.0] | dead 's people | Conversations_with_Dead_People |
| 32. | africa | 1: [18, inf], 31: [15, 7.5], 33: [17, 8.5] | africa world 's | South_Africa |
| 33. | three | 1: [21, inf] | three 's killed | 3_Days_to_Kill |
| 34. | wounded | 1: [14, 14.0], 15: [20, 6.67], 40: [13, inf] | wounded killed people | List_of_United_States_Congress_members_killed_or_wounded_in_office |
| 35. | attacks | 1: [24, inf], 3: [18, 6.0], 41: [13, 6.5] | attacks 's killed | List_of_fatal_cougar_attacks_in_North_America |
| 36. | suicide | 1: [19, inf], 10: [11, 5.5], 26: [34, inf] | suicide bomber killed | Suicide_attack |
| 37. | eastern | 1: [10, 10.0], 25: [11, 11.0], 31: [12, inf], 41: [13, inf], 47: [10, inf] | eastern 's officials | Eastern_Time_Zone |
| 38. | west | 1: [13, inf], 46: [15, 7.5] | west 's bank | West_Bank |
| 39. | briefing | 1: [24, inf] | briefing world 's | World_Briefing |
| 40. | asia | 1: [19, inf], 22: [21, inf], 45: [11, 11.0] | asia world briefing | BBC_World_News |
| 41. | afghanistan | 1: [16, 16.0], 5: [26, 8.67], 9: [19, inf], 20: [14, inf], 30: [12, 6.0], 36: [37, 5.29] | afghanistan afghan 's | Soviet–Afghan_War |
| 42. | bomber | 1: [14, inf], 3: [15, inf], 26: [10, inf] | bomber suicide killed | Female_suicide_bomber |
| 43. | south | 1: [19, inf] | south 's korea | South_Korea |
| 44. | afghan | 1: [15, 15.0], 5: [21, 21.0], 9: [17, 8.5], 15: [19, inf], 20: [11, inf], 31: [12, 6.0] | afghan afghanistan taliban | War_in_Afghanistan_(2001–present) |
| 45. | city | 1: [12, inf] | city 's mexico | Mexico_City |
| 46. | forces | 1: [12, inf], 5: [21, 5.25], 15: [18, 6.0] | forces 's security | Rhodesian_Security_Forces |
| 47. | month | 1: [13, inf], 14: [18, inf], 41: [13, 6.5] | month 's last | The_Last_Month_of_the_Year |
| 48. | `` | 1: [34, inf] | `` 's mr. | Toyota_MR2 |
| 49. | minister | 1: [30, inf] | minister prime 's | List_of_prime_ministers_of_the_United_Kingdom |
| 50. | ariel | 1: [15, inf] | ariel sharon 's | Ariel_Sharon |
| 51. | stroke | 1: [15, inf] | stroke sharon prime | Ariel_Sharon |
| 52. | israel | 1: [16, inf], 9: [26, 26.0], 26: [63, 5.73] | israel israeli lebanon | Israeli–Lebanese_conflict |
| 53. | interview | 1: [11, inf], 16: [11, inf], 20: [13, 6.5] | interview 's mr. | The_Interview |
| 54. | germany | 1: [11, inf], 19: [10, 10.0] | germany 's german | Germany |
| 55. | least | 1: [22, inf], 25: [12, 12.0] | least killed people | List_of_people_killed_for_being_transgender |
| 56. | monday | 1: [16, inf], 14: [13, 13.0], 36: [24, 6.0] | monday 's russian | Monday |
| 57. | reported | 1: [13, inf] | reported 's mr. | Toyota_MR2 |
| 58. | children | 1: [15, inf], 15: [13, inf], 43: [20, 10.0], 48: [15, 7.5] | children 's people | List_of_people_with_the_most_children |
| 59. | japan | 1: [14, 14.0], 6: [11, 5.5], 25: [32, 10.67], 33: [18, 9.0], 38: [22, 11.0], 46: [14, 7.0], 50: [15, inf] | japan 's korea | Koreans_in_Japan |
| 60. | kills | 1: [11, inf], 13: [21, 5.25], 23: [11, 11.0], 32: [25, 6.25] | kills killed suicide | Suicide_Squad:_Kill_the_Justice_League |
| 61. | central | 1: [11, inf], 27: [11, 5.5], 36: [12, 6.0] | central 's iraq | Central_Bank_of_Iraq |
| 62. | house | 1: [11, inf], 7: [16, 5.33], 16: [20, 6.67], 37: [12, inf] | house 's iraq | Iraq_War |
| 63. | attack | 1: [21, inf] | attack killed 's | List_of_fatal_cougar_attacks_in_North_America |
| 64. | sunni | 1: [15, inf], 15: [10, 5.0], 29: [18, 18.0] | sunni shiite iraqi | Shia–Sunni_relations |
| 65. | according | 1: [11, inf], 29: [22, 5.5], 49: [11, 11.0] | according 's russia | Russia |
| 66. | public | 1: [14, inf], 44: [12, 6.0], 46: [15, 7.5] | public 's government | State_school |
| 67. | company | 1: [10, inf], 28: [15, inf], 31: [11, 11.0], 34: [11, 11.0] | company 's russia | List_of_companies_of_Russia |
| 68. | leaders | 1: [22, inf], 3: [14, 7.0] | leaders 's government | List_of_current_heads_of_state_and_government |
| 69. | deal | 1: [16, inf], 17: [25, 25.0], 27: [15, 5.0] | deal 's government | New_Deal |
| 70. | army | 1: [12, inf], 22: [20, 5.0], 25: [18, inf], 31: [17, 5.67], 35: [23, 11.5] | army 's iraq | Iraqi_Army |
| 71. | decision | 1: [13, inf] | decision 's court | Dred_Scott_v._Sandford |
| 72. | including | 1: [12, inf], 34: [13, 13.0] | including 's people | Chinese_people |
| 73. | foreign | 1: [10, inf], 18: [23, 5.75] | foreign 's government | Foreign,_Commonwealth_and_Development_Office |
| 74. | arrest | 1: [13, inf], 51: [11, inf] | arrest 's police | Arrest |
| 75. | announced | 1: [10, inf], 21: [11, 5.5], 36: [15, 5.0] | announced 's russia | Russia |
| 76. | suspect | 1: [12, inf], 34: [26, 6.5] | suspect police 's | Prime_Suspect |
| 77. | say | 1: [11, inf] | say 's officials | Say_Say_Say |
| 78. | gen. | 1: [11, inf] | gen. iraq general | David_Petraeus |
| 79. | general | 1: [22, 22.0], 4: [11, inf], 6: [16, inf] | general 's united | United_States_Attorney_General |
| 80. | among | 1: [13, inf], 13: [10, 5.0], 31: [18, 9.0] | among 's iraq | Iraq |
| 81. | party | 1: [19, inf] | party 's prime | List_of_prime_ministers_of_India |
| 82. | korea | 1: [18, inf], 15: [14, 7.0], 19: [19, inf], 27: [35, 8.75], 46: [11, inf] | korea north south | North_Korea–South_Korea_relations |
| 83. | friday | 1: [19, inf], 24: [21, 5.25] | friday 's russian | Friday |
| 84. | week | 1: [10, inf], 16: [28, 5.6], 48: [18, 18.0] | week 's last | Last_Week_Tonight_with_John_Oliver |
| 85. | -- | 1: [23, inf], 36: [10, 5.0] | -- 's government | Federal_government_of_the_United_States |
| 86. | cases | 1: [12, inf], 4: [10, inf], 33: [17, inf] | cases 's flu | 2009_swine_flu_pandemic |
| 87. | others | 1: [10, inf] | others 's people | Hell_Is_Other_People |
| 88. | north | 1: [14, inf], 5: [14, 7.0], 41: [123, 5.59], 46: [20, 20.0] | north korea 's | North_Korea |
| 89. | insurgents | 1: [13, inf], 15: [10, inf], 20: [12, inf], 25: [24, 6.0] | insurgents killed iraqi | Iraqi_insurgency_(2011–2013) |
| 90. | wednesday | 1: [31, inf], 36: [27, 13.5], 38: [25, 8.33] | wednesday 's mr. | List_of_Mr._Robot_episodes |
| 91. | body | 1: [11, inf], 11: [16, inf], 23: [10, inf] | body 's world | Body_Worlds |
| 92. | found | 1: [15, 15.0], 5: [13, 6.5], 14: [20, 10.0], 22: [15, 7.5], 48: [30, inf] | found 's people | HTTP_404 |
| 93. | bird | 1: [22, inf], 5: [11, 5.5] | bird flu health | Avian_influenza |
| 94. | flu | 1: [22, inf], 5: [14, 7.0], 19: [12, inf] | flu bird health | Avian_influenza |
| 95. | turkey | 1: [14, inf], 19: [12, inf], 24: [12, 6.0], 45: [23, inf], 48: [33, 5.5] | turkey 's pope | Attempted_assassination_of_Pope_John_Paul_II |
| 96. | olmert | 1: [12, inf], 17: [18, inf], 25: [11, inf], 48: [11, inf] | olmert israel prime | Ehud_Olmert |
| 97. | israeli | 1: [12, inf], 41: [28, 14.0] | israeli israel lebanon | Israeli–Lebanese_conflict |
| 98. | gaza | 1: [15, 7.5], 31: [10, 5.0], 50: [19, inf] | gaza palestinian israeli | Gaza_War_(2008–2009) |
| 99. | thursday | 1: [15, inf], 16: [20, 20.0], 36: [18, 18.0], 50: [16, 8.0] | thursday 's mr. | Mr._Mayor |
| 100. | bush | 1: [13, inf], 38: [40, 10.0] | bush president 's | George_H._W._Bush |
| 101. | condition | 1: [10, inf] | condition 's sharon | Sharon_Osbourne |
| 102. | court | 1: [12, inf] | court 's mr. | Supreme_Court_of_the_United_States |
| 103. | visit | 1: [10, inf], 9: [26, 8.67], 11: [12, 12.0], 16: [28, 5.6], 36: [10, 10.0], 40: [15, 7.5] | visit 's president | Richard_Nixon's_1972_visit_to_China |
| 104. | koizumi | 1: [12, inf], 33: [15, inf] | koizumi japan 's | Junichiro_Koizumi |
| 105. | troops | 1: [14, inf], 5: [16, 16.0], 11: [16, 5.33], 16: [27, 5.4], 41: [19, 9.5] | troops iraq 's | Withdrawal_of_U.S._troops_from_Iraq_(2020–21) |
| 106. | spain | 1: [11, 11.0], 25: [10, 10.0], 27: [19, 9.5], 38: [12, inf], 44: [11, 11.0] | spain 's government | Government_of_Spain |
| 107. | pope | 2: [19, 9.5], 25: [20, inf], 27: [14, inf], 37: [50, 6.25], 48: [41, 5.86] | pope benedict 's | Pope_Benedict_XVI |
| 108. | prison | 2: [24, 6.0], 15: [12, inf], 28: [12, inf], 34: [15, 5.0] | prison years 's | Prison |
| 109. | muslim | 2: [15, 15.0], 5: [23, inf], 20: [11, 5.5], 48: [14, inf] | muslim 's world | Muslim_world |
| 110. | cheney | 2: [10, inf], 7: [12, inf], 18: [21, inf], 28: [14, inf] | cheney 's president | Dick_Cheney |
| 111. | involved | 2: [10, inf] | involved 's iraq | Multi-National_Force_–_Iraq |
| 112. | n't | 2: [10, 10.0], 12: [10, 5.0], 49: [22, inf] | n't 's iraq | Iraq |
| 113. | robertson | 2: [10, inf] | robertson sharon israel | Pat_Robertson |
| 114. | militants | 2: [10, 5.0], 22: [14, 14.0], 41: [18, inf], 44: [21, inf] | militants israeli gaza | 2012_Israeli_operation_in_the_Gaza_Strip |
| 115. | lawyer | 2: [12, inf], 50: [19, 9.5] | lawyer 's court | Lawyer |
| 116. | union | 2: [13, 6.5], 4: [16, 16.0], 9: [22, inf], 27: [21, 5.25] | union 's european | European_Union |
| 117. | uranium | 2: [11, 5.5], 7: [17, inf], 14: [14, 7.0], 23: [19, 19.0], 31: [16, inf] | uranium iran nuclear | Nuclear_program_of_Iran |
| 118. | hamas | 2: [17, 8.5], 4: [84, 5.25], 19: [12, 6.0], 23: [47, inf], 26: [35, 8.75], 35: [10, 5.0], 37: [28, 7.0], 50: [51, 8.5] | hamas palestinian israel | Hamas |
| 119. | stampede | 2: [13, inf] | stampede pilgrimage killed | 2015_Mina_stampede |
| 120. | call | 3: [10, 5.0], 28: [16, inf] | call 's iraq | Iraq |
| 121. | abbas | 3: [11, inf], 8: [11, 11.0], 16: [20, 6.67], 23: [33, 11.0], 48: [11, inf] | abbas palestinian hamas | Hamas |
| 122. | sheik | 3: [13, inf] | sheik hezbollah 's | Hassan_Nasrallah |
| 123. | fight | 3: [13, 6.5], 30: [19, 6.33], 35: [10, inf], 37: [18, 9.0], 47: [16, 8.0] | fight 's world | Fighting_the_World |
| 124. | bodies | 3: [11, 5.5], 5: [10, 10.0], 25: [20, 5.0], 36: [12, inf], 41: [12, inf] | bodies found baghdad | Baghdad |
| 125. | laden | 3: [14, inf], 16: [12, inf] | laden 's osama | Killing_of_Osama_bin_Laden |
| 126. | billion | 3: [16, inf], 20: [13, inf], 22: [12, inf] | billion 's russian | Billion |
| 127. | ivory | 3: [13, inf], 6: [10, inf] | ivory coast 's | Ivory_Coast |
| 128. | coast | 3: [13, inf], 22: [14, 14.0], 35: [19, inf] | coast 's ivory | Ivory_Coast |
| 129. | mass | 3: [11, inf], 31: [10, inf] | mass 's officials | Mass–energy_equivalence |
| 130. | nepal | 3: [11, inf], 14: [24, inf], 47: [14, 7.0] | nepal 's king | King_of_Nepal |
| 131. | wants | 4: [10, inf] | wants 's iraq | 2003_invasion_of_Iraq |
| 132. | accused | 4: [13, inf], 31: [22, 5.5], 42: [12, 12.0] | accused 's mr. | The_Accüsed |
| 133. | sudan | 4: [13, inf], 14: [12, 6.0], 23: [14, inf], 43: [20, 10.0], 46: [10, 10.0] | sudan darfur african | War_in_Darfur |
| 134. | georgia | 4: [42, 21.0], 39: [12, inf] | georgia russia russian | Georgia–Russia_relations |
| 135. | gas | 4: [49, 7.0], 13: [30, 15.0], 49: [10, inf], 52: [22, inf] | gas 's russia | 2009_Russia–Ukraine_gas_dispute |
| 136. | financial | 4: [12, inf], 25: [10, 10.0], 31: [11, inf] | financial 's government | Federal_government_of_the_United_States |
| 137. | hussein | 4: [20, inf], 7: [17, inf], 9: [13, inf], 11: [21, inf], 14: [23, inf], 25: [26, 26.0], 29: [16, inf], 44: [14, inf], 51: [11, inf], 52: [56, 5.09] | hussein iraq saddam | Saddam's_family |
| 138. | letter | 4: [15, inf], 19: [21, 21.0], 29: [15, inf] | letter 's president | A_Letter_to_the_President |
| 139. | region | 4: [17, 17.0], 43: [10, 10.0], 49: [11, inf], 52: [11, 11.0] | region 's russia | Ural_Mountains |
| 140. | novelist | 4: [10, inf] | novelist `` trial | Michael_Peterson_(criminal) |
| 141. | african | 4: [15, inf], 29: [14, inf], 33: [16, 5.33], 36: [39, 13.0], 38: [25, 6.25], 43: [16, 16.0] | african 's africa | Africa |
| 142. | fuel | 4: [13, 6.5], 15: [10, 10.0], 38: [14, inf] | fuel nuclear iran | Nuclear_program_of_Iran |
| 143. | secretary | 4: [15, inf], 13: [18, 9.0], 17: [40, 10.0], 21: [10, 5.0], 28: [16, 16.0], 35: [15, 5.0], 48: [10, 5.0] | secretary 's united | United_States_Secretary_of_State |
| 144. | encyclical | 4: [11, inf] | encyclical pope first | Encyclical |
| 145. | issues | 4: [10, inf] | issues 's government | Government_Issue |
| 146. | victory | 4: [25, 8.33], 14: [12, 12.0], 23: [11, inf] | victory 's president | President_of_the_United_States |
| 147. | groups | 4: [11, inf], 26: [32, 8.0] | groups 's government | Federal_government_of_the_United_States |
| 148. | sri | 4: [11, 5.5], 19: [14, inf], 30: [14, inf], 35: [20, inf], 42: [24, 6.0], 45: [30, 7.5], 52: [17, 8.5] | sri lanka rebels | Sri_Lankan_Civil_War |
| 149. | plan | 4: [11, inf], 25: [35, 5.83], 29: [15, 7.5], 33: [20, 6.67], 40: [24, 8.0] | plan 's iraq | 2003_invasion_of_Iraq |
| 150. | zimbabwe | 4: [13, inf], 22: [12, 12.0], 31: [22, inf] | zimbabwe 's government | Hyperinflation_in_Zimbabwe |
| 151. | bombing | 5: [13, inf], 8: [10, 10.0], 26: [11, 11.0], 43: [10, inf], 51: [10, 5.0] | bombing killed suicide | Suicide_attack |
| 152. | guilty | 5: [11, inf], 14: [11, inf], 31: [13, inf] | guilty court 's | Alford_plea |
| 153. | oil | 5: [11, inf], 28: [42, inf], 49: [16, 8.0], 52: [11, inf] | oil 's iraq | Oil_reserves_in_Iraq |
| 154. | danish | 5: [37, inf], 41: [10, inf] | danish cartoons muhammad | Jyllands-Posten_Muhammad_cartoons_controversy |
| 155. | muslims | 5: [13, inf], 7: [14, 14.0], 27: [20, inf], 48: [11, 11.0] | muslims 's muslim | Muslims |
| 156. | italy | 5: [15, 7.5], 25: [10, inf], 34: [25, inf] | italy 's berlusconi | Silvio_Berlusconi |
| 157. | priest | 5: [10, inf] | priest church vatican | Homosexual_clergy_in_the_Catholic_Church |
| 158. | response | 5: [10, inf], 16: [14, 7.0] | response 's iraq | Iraq_War |
| 159. | join | 5: [12, inf], 24: [13, inf] | join 's party | Democratic_Party_(United_States) |
| 160. | cartoons | 5: [30, inf], 22: [10, inf] | cartoons danish muhammad | Jyllands-Posten_Muhammad_cartoons_controversy |
| 161. | prophet | 5: [20, inf] | prophet cartoons muhammad | Jyllands-Posten_Muhammad_cartoons_controversy |
| 162. | ferry | 5: [20, inf] | ferry 's people | Harpers_Ferry,_West_Virginia |
| 163. | car | 5: [16, 8.0], 17: [10, 5.0], 33: [10, inf], 50: [10, inf] | car killed people | Who_Killed_the_Electric_Car? |
| 164. | atomic | 5: [13, 6.5], 47: [11, inf] | atomic iran nuclear | Nuclear_facilities_in_Iran |
| 165. | sees | 5: [11, inf] | sees 's iraq | Iraq_War |
| 166. | settlers | 5: [12, inf] | settlers israeli west | Israeli_settlement |
| 167. | egypt | 5: [18, inf], 15: [15, inf], 26: [15, 7.5] | egypt 's people | Egyptians |
| 168. | drawings | 5: [11, inf] | drawings cartoons european | Cartoon |
| 169. | nato | 5: [11, inf], 18: [15, inf], 23: [15, inf], 36: [16, 8.0], 43: [18, 9.0] | nato afghanistan taliban | Taliban_insurgency |
| 170. | red | 5: [10, inf] | red 's government | Red_box_(government) |
| 171. | holocaust | 6: [15, 5.0], 16: [13, inf] | holocaust iran germany | Holocaust_denial |
| 172. | cleric | 6: [16, inf], 24: [13, 6.5], 41: [14, 7.0] | cleric 's shiite | Shia_clergy |
| 173. | murder | 6: [11, inf], 41: [15, 5.0] | murder 's people | O._J._Simpson_murder_case |
| 174. | syria | 6: [11, inf], 20: [12, inf], 35: [29, 14.5], 37: [11, inf], 49: [16, 5.33] | syria 's iraq | Iraq–Syria_relations |
| 175. | seven | 6: [12, inf], 22: [13, 6.5] | seven killed 's | The_Red_Queen_Kills_Seven_Times |
| 176. | results | 6: [15, 7.5], 26: [15, inf], 37: [10, inf], 40: [13, 13.0] | results 's election | Attempts_to_overturn_the_2020_United_States_presidential_election |
| 177. | saddam | 7: [13, 13.0], 9: [11, 11.0], 11: [13, 6.5], 14: [12, inf], 25: [11, inf], 30: [11, 5.5], 52: [23, 5.75] | saddam hussein iraq | Saddam's_family |
| 178. | enrichment | 7: [16, inf] | enrichment iran uranium | Enriched_uranium |
| 179. | fraud | 7: [15, 5.0], 27: [14, inf] | fraud 's times | Fraud |
| 180. | declared | 7: [11, 5.5], 12: [11, inf], 27: [12, inf] | declared 's president | President_of_the_United_States |
| 181. | blair | 7: [23, inf], 17: [18, inf], 28: [11, inf], 36: [42, 10.5], 39: [18, 9.0], 49: [11, 11.0] | blair prime tony | Tony_Blair |
| 182. | months | 7: [19, 9.5], 43: [13, inf] | months 's iraq | Iraq |
| 183. | ban | 7: [11, inf], 14: [13, 6.5], 18: [19, 9.5], 20: [15, 15.0], 33: [12, inf], 43: [13, 6.5], 48: [14, inf] | ban 's government | List_of_books_banned_by_governments |
| 184. | ghraib | 7: [14, inf], 10: [13, inf] | ghraib abu iraq | Abu_Ghraib_torture_and_prisoner_abuse |
| 185. | rock | 7: [10, inf] | rock 's city | Rock_City |
| 186. | india | 7: [19, inf], 12: [12, 6.0], 28: [37, 37.0], 46: [14, 14.0] | india 's indian | Economy_of_India |
| 187. | camp | 7: [10, 5.0], 19: [14, 14.0], 31: [10, inf] | camp 's russian | Camp_David |
| 188. | refugees | 7: [10, inf], 30: [13, 13.0] | refugees asylum 's | Asylum_in_the_United_States |
| 189. | trapped | 8: [11, inf] | trapped people world | Stairwell:_Trapped_in_the_World_Trade_Center |
| 190. | miners | 8: [17, inf] | miners mining mexico | New_Mexico_Institute_of_Mining_and_Technology |
| 191. | rice | 8: [12, 6.0], 11: [17, 5.67], 13: [31, 7.75], 17: [45, inf], 42: [11, inf] | rice 's state | Condoleezza_Rice |
| 192. | rescue | 8: [11, inf] | rescue 's russia | Search_and_rescue |
| 193. | market | 8: [19, 6.33], 34: [13, inf] | market 's russia | Russia |
| 194. | collapse | 8: [10, 10.0], 23: [10, inf] | collapse 's iraq | Iraq_War |
| 195. | roof | 8: [19, inf] | roof snow moscow | Katowice_Trade_Hall_roof_collapse |
| 196. | mexico | 8: [14, 7.0], 21: [18, inf], 26: [15, 7.5], 31: [27, inf], 42: [11, inf], 47: [10, inf] | mexico 's election | Elections_in_Mexico |
| 197. | moscow | 8: [25, 12.5], 16: [10, 10.0], 21: [15, inf], 27: [16, inf], 48: [11, 11.0] | moscow russia russian | Moscow |
| 198. | emergency | 8: [13, inf] | emergency 's people | The_Emergency_(India) |
| 199. | snow | 8: [14, inf] | snow 's roof | Roof |
| 200. | shrine | 8: [13, inf], 29: [12, inf] | shrine 's shiite | 2006_al-Askari_mosque_bombing |
| 201. | fury | 8: [12, inf] | fury iraq 's | Hawker_Sea_Fury |
| 202. | coup | 8: [11, inf], 25: [10, inf], 38: [14, inf], 44: [10, inf] | coup 's government | List_of_coups_and_coup_attempts |
| 203. | milosevic | 8: [12, inf], 10: [10, 5.0], 11: [74, 7.4], 22: [16, inf] | milosevic 's slobodan | Slobodan_Milošević |
| 204. | saudi | 8: [11, inf], 16: [10, inf] | saudi people arabia | Demographics_of_Saudi_Arabia |
| 205. | weapons | 9: [10, inf] | weapons nuclear iran | Nuclear_program_of_Iran |
| 206. | pakistan | 9: [22, 11.0], 12: [12, 6.0], 22: [14, inf], 28: [19, 9.5], 38: [12, 6.0], 46: [30, 6.0], 52: [19, inf] | pakistan 's killed | Drone_strikes_in_Pakistan |
| 207. | control | 9: [13, 13.0], 18: [17, 5.67], 47: [12, inf] | control 's government | Divided_government_in_the_United_States |
| 208. | taliban | 9: [15, inf], 20: [15, inf], 47: [13, inf] | taliban afghanistan afghan | War_in_Afghanistan_(2001–present) |
| 209. | palestinians | 9: [14, 7.0], 12: [30, 15.0], 14: [12, 6.0], 33: [14, 14.0], 41: [22, 5.5], 47: [25, 12.5], 50: [22, inf] | palestinians israel palestinian | Israeli–Palestinian_conflict |
| 210. | taiwan | 9: [19, inf], 49: [16, inf], 52: [11, inf] | taiwan 's chen | Chen_Shui-bian |
| 211. | unification | 9: [16, inf] | unification russia taiwan | Chinese_unification |
| 212. | secret | 9: [10, inf], 14: [14, 7.0], 30: [10, inf] | secret 's program | United_States_Secret_Service |
| 213. | rules | 9: [10, inf], 12: [12, 12.0] | rules 's court | Merrick_Garland_Supreme_Court_nomination |
| 214. | force | 9: [11, inf], 16: [21, 7.0], 20: [25, 12.5], 25: [14, inf], 38: [32, 16.0], 46: [13, 6.5] | force 's united | United_States_Air_Force |
| 215. | chechnya | 9: [10, inf], 23: [10, inf], 27: [10, inf], 41: [12, 12.0] | chechnya russian russia | Chechnya |
| 216. | kadyrov | 9: [12, inf] | kadyrov russian russia | Ramzan_Kadyrov |
| 217. | mosque | 9: [15, inf], 14: [20, 5.0] | mosque 's baghdad | Abu_Hanifa_Mosque |
| 218. | britain | 9: [15, 5.0], 24: [15, 5.0], 26: [10, inf], 43: [14, inf] | britain 's british | Britishness |
| 219. | move | 9: [10, inf], 18: [15, 5.0] | move 's government | MOVE |
| 220. | jaafari | 9: [15, inf] | jaafari prime minister | Ibrahim_al-Jaafari |
| 221. | rift | 10: [10, inf] | rift 's turkey | League_of_Legends:_Wild_Rift |
| 222. | abu | 10: [13, inf], 23: [37, inf], 27: [26, inf] | abu 's iraq | Abu_Bakr_al-Baghdadi |
| 223. | pipeline | 10: [10, inf], 17: [31, 15.5], 19: [11, inf], 28: [11, inf], 31: [14, inf] | pipeline oil 's | Afghanistan_Oil_Pipeline |
| 224. | around | 10: [11, 5.5], 17: [15, 5.0], 28: [17, inf], 37: [10, 10.0], 48: [10, 5.0] | around 's world | Around_the_World_in_Eighty_Days |
| 225. | session | 10: [14, inf], 38: [10, inf] | session 's mr. | Mr._Mister |
| 226. | chile | 10: [11, inf], 20: [12, inf], 52: [10, 5.0] | chile pinochet 's | Augusto_Pinochet |
| 227. | formula | 10: [13, inf] | formula iraq 's | Abu_Ghraib |
| 228. | editor | 10: [10, inf], 26: [10, inf] | editor 's mr. | Mr._Mayor |
| 229. | increase | 11: [10, inf], 16: [11, 5.5] | increase 's government | Increase_Mather |
| 230. | judge | 11: [17, 8.5], 20: [20, 10.0], 37: [12, inf] | judge trial hussein | Trial_of_Saddam_Hussein |
| 231. | finally | 11: [10, 10.0], 26: [13, inf] | finally 's world | Finally_It's_Christmas |
| 232. | students | 11: [14, inf], 16: [10, 5.0], 19: [12, inf], 50: [12, 12.0] | students 's law | Parkinson's_law |
| 233. | reduce | 11: [11, inf] | reduce iraq 's | Iraq |
| 234. | open | 11: [17, inf] | open 's russia | Open_Russia |
| 235. | labor | 11: [15, inf], 17: [10, 5.0], 28: [11, inf], 39: [10, 10.0], 46: [18, inf] | labor 's law | United_States_labor_law |
| 236. | indonesia | 11: [22, inf], 47: [15, 15.0] | indonesia 's indonesian | Indonesia |
| 237. | mining | 11: [12, inf], 43: [14, inf] | mining company 's | List_of_mining_companies |
| 238. | papua | 11: [10, inf] | papua mining company | Mining_in_Papua_New_Guinea |
| 239. | time | 11: [15, 7.5], 23: [22, 11.0], 38: [24, 12.0], 47: [14, inf] | time 's first | First_Time |
| 240. | civilians | 11: [10, inf], 21: [24, 6.0], 45: [16, 5.33] | civilians killed military | Civilian_casualties_in_the_war_in_Afghanistan_(2001–present) |
| 241. | airport | 11: [15, inf], 20: [10, 10.0], 32: [12, 12.0], 44: [10, 5.0] | airport 's russia | Sheremetyevo_International_Airport |
| 242. | ice | 11: [12, inf], 32: [13, inf] | ice 's world | Ice_Hockey_World_Championships |
| 243. | water | 11: [10, inf], 34: [12, inf], 39: [19, 19.0], 46: [14, 14.0] | water 's people | Water_For_People |
| 244. | flights | 11: [14, inf], 17: [10, 10.0], 32: [10, inf] | flights 's plot | Bojinka_plot |
| 245. | belarus | 11: [18, inf], 50: [13, inf], 52: [15, inf] | belarus 's russia | Belarus–Russia_relations |
| 246. | appeared | 12: [10, inf] | appeared 's mr. | Toyota_MR2 |
| 247. | trafficking | 12: [10, inf] | trafficking cocaine 's | CIA_involvement_in_Contra_cocaine_trafficking |
| 248. | indian | 12: [13, inf], 15: [10, 5.0], 28: [16, 8.0] | indian india 's | Economy_of_India |
| 249. | bomb | 12: [19, 9.5], 20: [11, 11.0], 32: [31, 31.0], 38: [13, 6.5], 41: [26, 26.0], 47: [14, inf], 50: [10, 10.0] | bomb killed 's | Car_bomb |
| 250. | crossing | 12: [11, inf] | crossing border israel | Israel–Gaza_barrier |
| 251. | sonia | 12: [10, inf] | sonia gandhi parliament | Sonia_Gandhi |
| 252. | gandhi | 12: [14, inf] | gandhi indian sonia | Sonia_Gandhi |
| 253. | eta | 12: [12, inf] | eta basque group | ETA_(separatist_group) |
| 254. | cease-fire | 12: [10, inf], 17: [16, 8.0], 47: [13, 13.0] | cease-fire israel lebanon | Israeli–Lebanese_conflict |
| 255. | basque | 12: [21, inf] | basque cease-fire group | ETA_(separatist_group) |
| 256. | polish | 13: [12, inf] | polish poland europe | Poland |
| 257. | ukraine | 13: [14, 14.0], 25: [21, inf], 27: [25, 6.25], 34: [24, inf], 43: [14, inf] | ukraine russia 's | Ukrainians_in_Russia |
| 258. | coalition | 13: [18, 6.0], 21: [10, 10.0], 25: [20, inf], 37: [10, inf] | coalition 's government | Coalition_government |
| 259. | test | 13: [22, 7.33], 25: [11, 11.0], 40: [18, inf], 46: [19, 19.0] | test north korea | List_of_North_Korean_missile_tests |
| 260. | transit | 13: [11, inf] | transit gas russia | Russia–Ukraine_gas_disputes |
| 261. | immigration | 13: [14, inf] | immigration 's russia | Immigration_to_Russia |
| 262. | liberia | 13: [17, inf], 23: [14, inf] | liberia 's taylor | Charles_Taylor_(Liberian_politician) |
| 263. | sierra | 13: [21, 21.0], 24: [10, inf] | sierra taylor leone | Charles_Taylor_(Liberian_politician) |
| 264. | leone | 13: [21, 21.0], 24: [10, inf] | leone taylor sierra | Charles_Taylor_(Liberian_politician) |
| 265. | nation | 13: [10, inf], 34: [16, 5.33], 38: [21, 7.0] | nation 's president | President_of_the_Navajo_Nation |
| 266. | condoleezza | 13: [16, 16.0], 17: [11, inf] | condoleezza rice 's | Condoleezza_Rice |
| 267. | gunmen | 13: [14, inf], 50: [15, inf] | gunmen gaza killed | 2018–2019_Gaza_border_protests |
| 268. | gun | 13: [12, inf], 21: [10, inf] | gun 's palestinian | Carlo_(submachine_gun) |
| 269. | israelis | 13: [12, 6.0], 35: [12, inf] | israelis israel israeli | Israelis |
| 270. | eclipse | 13: [12, inf] | eclipse president world | President_of_the_United_States |
| 271. | prodi | 13: [10, inf], 15: [25, 8.33] | prodi berlusconi italy | Romano_Prodi |
| 272. | jacques | 13: [10, inf] | jacques chirac france | Jacques_Chirac |
| 273. | sanctions | 13: [12, inf], 15: [13, inf], 27: [10, inf], 46: [11, inf] | sanctions iran nuclear | Sanctions_against_Iran |
| 274. | captors | 13: [12, inf] | captors baghdad reporter | Foreign_hostages_in_Iraq |
| 275. | reporter | 13: [17, inf] | reporter 's court | Court_reporter |
| 276. | jill | 13: [13, inf] | jill carroll american | Jill_Carroll |
| 277. | carroll | 13: [15, inf] | carroll jill american | Jill_Carroll |
| 278. | kurdish | 13: [10, inf] | kurdish iraq 's | Iraqi–Kurdish_conflict |
| 279. | earthquake | 13: [18, inf], 22: [13, 6.5] | earthquake quake 's | 1994_Northridge_earthquake |
| 280. | raises | 13: [10, inf] | raises 's government | Federal_government_of_the_United_States |
| 281. | island | 13: [19, 19.0], 31: [18, inf] | island 's `` | Island |
| 282. | catalonia | 13: [10, inf], 25: [10, inf] | catalonia spain autonomy | Statute_of_Autonomy_of_Catalonia_of_2006 |
| 283. | shinawatra | 14: [10, inf] | shinawatra thaksin prime | Thaksin_Shinawatra |
| 284. | thailand | 14: [16, 16.0], 38: [12, inf] | thailand thaksin 's | Thaksin_Shinawatra |
| 285. | boycott | 14: [17, inf] | boycott 's government | Boycott |
| 286. | premier | 14: [17, 5.67], 48: [10, inf] | premier prime 's | Premier_of_the_People's_Republic_of_China |
| 287. | darfur | 14: [17, inf], 28: [12, inf], 32: [10, inf], 43: [13, 13.0] | darfur sudan force | War_in_Darfur |
| 288. | sell | 14: [10, inf], 19: [10, inf] | sell company 's | List_of_best-selling_singles |
| 289. | signed | 14: [11, inf] | signed 's russia | Call_signs_in_Russia |
| 290. | bill | 14: [12, inf], 19: [16, inf], 32: [20, inf] | bill 's would | Bill_&_Ted |
| 291. | largest | 14: [24, 24.0], 16: [10, 5.0], 22: [11, inf] | largest 's party | List_of_largest_political_parties |
| 292. | buying | 14: [15, inf] | buying china 's | Best_Buy |
| 293. | rule | 14: [10, inf], 41: [11, 5.5] | rule 's government | President's_rule |
| 294. | ties | 14: [12, inf], 25: [11, inf] | ties 's mr. | Toyota_MR2 |
| 295. | diplomatic | 14: [13, 13.0], 20: [11, 5.5], 49: [10, inf] | diplomatic 's iraq | Embassy_of_the_United_States,_Baghdad |
| 296. | abstinence | 14: [10, inf] | abstinence berlusconi aids | Pope_John_Paul_II |
| 297. | congress | 14: [15, inf] | congress 's iraq | Iraqi_National_Congress |
| 298. | newspapers | 14: [12, inf], 41: [16, inf], 48: [12, 6.0] | newspapers russian russia | List_of_newspapers_in_Russia |
| 299. | reforms | 14: [18, inf] | reforms 's people | Chinese_economic_reform |
| 300. | ivanov | 14: [10, inf] | ivanov russia 's | Sergei_Ivanov |
| 301. | putin | 14: [16, 8.0], 17: [19, inf], 19: [19, inf], 41: [17, 5.67], 52: [12, 6.0] | putin russia 's | Russia_under_Vladimir_Putin |
| 302. | officers | 14: [14, 7.0], 36: [12, inf] | officers police 's | Police_officer |
| 303. | ending | 14: [10, inf], 23: [10, inf] | ending 's people | I'm_Thinking_of_Ending_Things |
| 304. | deadline | 14: [15, inf], 34: [10, 5.0] | deadline iran 's | Tehran_(TV_series) |
| 305. | genocide | 14: [11, inf], 34: [12, inf], 41: [14, inf] | genocide 's hussein | Anfal_genocide |
| 306. | shot | 14: [14, inf], 19: [18, 9.0], 24: [14, 7.0] | shot 's killed | List_of_murdered_hip_hop_musicians |
| 307. | ireland | 14: [14, inf], 45: [12, inf] | ireland northern 's | Northern_Ireland |
| 308. | tax | 14: [12, inf] | tax 's government | List_of_countries_by_tax_rates |
| 309. | post-soviet | 14: [10, inf] | post-soviet russia russian | Post-Soviet_states |
| 310. | scholars | 14: [12, inf] | scholars 's photo | Google_Photos |
| 311. | suspected | 14: [10, inf] | suspected 's police | Prime_Suspect |
| 312. | toyota | 14: [10, inf] | toyota mike gascoyne | Mike_Gascoyne |
| 313. | democracy | 14: [12, inf], 38: [25, 12.5], 43: [13, 6.5] | democracy 's president | Democracy |
| 314. | tamil | 14: [11, inf], 26: [10, 5.0], 30: [10, inf], 45: [19, 9.5] | tamil sri lanka | Sri_Lankan_Tamils |
| 315. | pro-democracy | 14: [16, inf] | pro-democracy nepal king | Nepalese_democracy_movement |
| 316. | telescope | 14: [10, inf] | telescope really south | Hubble_Space_Telescope |
| 317. | really | 14: [10, inf] | really 's iraq | Islamic_State_of_Iraq_and_the_Levant |
| 318. | fujimori | 14: [10, inf], 20: [16, inf] | fujimori peru 's | Alberto_Fujimori |
| 319. | mafia | 15: [28, inf] | mafia arrest provenzano | Bernardo_Provenzano |
| 320. | boss | 15: [19, inf] | boss 's party | Political_boss |
| 321. | bernardo | 15: [16, inf] | bernardo mafia provenzano | Bernardo_Provenzano |
| 322. | provenzano | 15: [19, inf] | provenzano mafia arrest | Bernardo_Provenzano |
| 323. | runoff | 15: [12, inf] | runoff 's election | 2020–21_United_States_Senate_election_in_Georgia |
| 324. | bombings | 15: [20, 20.0], 43: [10, inf] | bombings killed attacks | 7_July_2005_London_bombings |
| 325. | qaeda | 15: [37, inf], 23: [16, inf], 32: [43, 5.38], 36: [11, 5.5], 44: [10, inf] | qaeda iraq 's | Saddam_Hussein_and_al-Qaeda_link_allegations |
| 326. | bosses | 15: [10, inf] | bosses boss party | Political_boss |
| 327. | tehran | 15: [10, inf] | tehran iran nuclear | Nuclear_facilities_in_Iran |
| 328. | kenyan | 15: [13, inf] | kenyan kiragu 's | Kithinji_Kiragu |
| 329. | plane | 15: [11, inf], 18: [10, inf], 32: [12, inf], 40: [15, 5.0] | plane crash russian | Lokomotiv_Yaroslavl_plane_crash |
| 330. | close | 15: [10, inf], 19: [10, inf], 48: [11, 11.0] | close 's people | Closer_to_the_People |
| 331. | question | 15: [11, inf], 49: [30, 30.0] | question 's iraq | Iraq_War |
| 332. | caused | 15: [11, 5.5], 27: [11, 5.5], 30: [10, inf] | caused 's russian | Russia |
| 333. | blast | 15: [15, 7.5], 26: [10, inf], 32: [12, 12.0] | blast killed least | List_of_explosions |
| 334. | karachi | 15: [15, inf] | karachi pakistan suicide | Consulate_General_of_the_United_States,_Karachi |
| 335. | rebels | 15: [28, 7.0], 31: [28, 9.33], 42: [16, 8.0], 45: [12, inf], 52: [13, 6.5] | rebels sri government | Sri_Lankan_Civil_War |
| 336. | attention | 15: [11, inf] | attention 's russia | Attention |
| 337. | rocket | 15: [15, 15.0], 22: [18, inf], 27: [15, inf], 41: [11, inf], 44: [19, inf] | rocket israel israeli | Palestinian_rocket_attacks_on_Israel |
| 338. | independence | 15: [11, inf], 28: [15, inf] | independence 's people | United_States_Declaration_of_Independence |
| 339. | recount | 15: [16, inf], 27: [22, inf], 31: [16, inf] | recount mexico election | 2006_Mexican_general_election |
| 340. | kyrgyzstan | 15: [12, inf], 28: [14, inf], 36: [26, inf] | kyrgyzstan united air | Kyrgyzstan |
| 341. | extended | 15: [10, inf] | extended russia government | Russian_Empire |
| 342. | extradition | 15: [10, inf] | extradition charges russia | Extradition_law_in_the_United_States |
| 343. | chad | 15: [25, 12.5], 46: [11, inf] | chad sudan rebels | Chadian_Civil_War_(2005–2010) |
| 344. | idriss | 15: [10, inf] | idriss chad rebels | Chadian_Civil_War_(2005–2010) |
| 345. | sicilian | 15: [12, inf] | sicilian mafia arrest | Sicilian_Mafia |
| 346. | sudanese | 15: [14, 7.0], 23: [14, inf], 35: [10, inf], 46: [10, inf] | sudanese darfur government | Sudan_Liberation_Movement/Army |
| 347. | baisalov | 15: [10, inf] | baisalov kyrgyzstan attack | Edil_Baisalov |
| 348. | bombs | 15: [10, 10.0], 17: [18, inf], 23: [12, 12.0], 31: [14, inf] | bombs iraq 's | 1998_bombing_of_Iraq |
| 349. | battles | 16: [15, inf] | battles 's gaza | Third_Battle_of_Gaza |
| 350. | researcher | 16: [13, inf], 34: [25, 12.5] | researcher times china | The_Epoch_Times |
| 351. | aid | 16: [20, 20.0], 19: [39, 5.57], 28: [14, inf], 43: [10, 10.0] | aid 's government | United_States_foreign_aid |
| 352. | tel | 16: [13, inf] | tel aviv palestinian | Tel_Aviv |
| 353. | aviv | 16: [13, inf] | aviv tel palestinian | Tel_Aviv |
| 354. | montenegro | 16: [10, inf], 25: [12, inf] | montenegro serbia nations | Serbia_and_Montenegro |
| 355. | irish | 16: [11, inf], 22: [22, inf] | irish ireland 's | Great_Famine_(Ireland) |
| 356. | schumacher | 16: [11, inf], 42: [13, inf] | schumacher race – | Michael_Schumacher |
| 357. | post | 16: [13, inf], 22: [10, 5.0], 25: [10, 5.0] | post 's minister | Minister_for_Posts_and_Telegraphs |
| 358. | major | 16: [16, inf] | major 's russia | Economy_of_Russia |
| 359. | plant | 16: [17, inf] | plant 's iran | Fordow_Fuel_Enrichment_Plant |
| 360. | hu | 16: [33, 16.5], 39: [12, inf] | hu china 's | Hu_Jintao |
| 361. | jintao | 16: [19, inf], 39: [10, inf] | jintao china hu | Hu_Jintao |
| 362. | tame | 16: [10, inf] | tame iraqi troops | Withdrawal_of_U.S._troops_from_Iraq_(2020–21) |
| 363. | block | 16: [14, inf] | block 's government | Maggie_De_Block |
| 364. | queen | 16: [26, inf] | queen 's elizabeth | Elizabeth_II |
| 365. | elizabeth | 16: [21, inf] | elizabeth queen th | Queen_Elizabeth |
| 366. | monarch | 16: [11, inf] | monarch queen th | Monarchy_of_the_United_Kingdom |
| 367. | karzai | 16: [10, inf] | karzai afghanistan president | Hamid_Karzai |
| 368. | nigeria | 16: [15, 7.5], 18: [12, inf], 24: [10, 10.0] | nigeria 's oil | Economy_of_Nigeria |
| 369. | workers | 16: [14, 14.0], 29: [11, 5.5], 32: [20, 10.0], 43: [10, inf] | workers 's government | Key_worker |
| 370. | th | 16: [19, inf] | th 's russian | Russia |
| 371. | using | 16: [10, inf] | using 's iraq | Authorization_for_Use_of_Military_Force_Against_Iraq_Resolution_of_2002 |
| 372. | debt | 16: [15, inf] | debt billion russian | National_debt_of_the_United_States |
| 373. | sinai | 17: [23, inf] | sinai resort two | Sinai_Peninsula |
| 374. | blasts | 17: [13, inf] | blasts india killed | Terrorism_in_India |
| 375. | vietnam | 17: [12, inf], 46: [17, inf] | vietnam 's president | President_of_Vietnam |
| 376. | greek | 17: [12, inf], 21: [13, inf] | greek visit police | Greece |
| 377. | video | 17: [14, inf], 27: [11, 11.0] | video 's iraq | July_12,_2007,_Baghdad_airstrike |
| 378. | malaria | 17: [18, inf], 30: [10, inf] | malaria world bank | World_Bank |
| 379. | health | 17: [12, inf], 40: [11, inf] | health 's flu | 2009_swine_flu_pandemic |
| 380. | orders | 17: [14, inf], 26: [13, 6.5] | orders court 's | Superior_orders |
| 381. | opposition | 17: [12, inf], 26: [20, inf], 29: [18, 9.0], 48: [18, 6.0], 52: [11, 11.0] | opposition 's party | Opposition_Party_(Southern_U.S.) |
| 382. | minister-designate | 17: [15, inf] | minister-designate prime government | Prime_minister-designate |
| 383. | built | 17: [11, inf] | built 's iraq | Iraq |
| 384. | rumsfeld | 17: [16, inf], 28: [13, inf], 48: [10, inf] | rumsfeld secretary defense | Donald_Rumsfeld |
| 385. | plug | 17: [12, inf] | plug jerusalem barrier | Separation_barrier |
| 386. | gaps | 17: [14, inf] | gaps 's jerusalem | Jerusalem |
| 387. | jerusalem | 17: [16, inf], 42: [12, inf] | jerusalem israel palestinian | United_States_recognition_of_Jerusalem_as_capital_of_Israel |
| 388. | barrier | 17: [20, inf] | barrier israel 's | Israeli_West_Bank_barrier |
| 389. | ehud | 17: [12, inf] | ehud olmert israel | Ehud_Olmert |
| 390. | lake | 17: [13, inf] | lake russia 's | Lake_Ladoga |
| 391. | poland | 17: [11, inf], 21: [20, inf] | poland 's europe | Poland_in_the_European_Union |
| 392. | struggle | 18: [10, inf], 38: [18, 9.0] | struggle 's people | Struggling_People's_Organization |
| 393. | mock | 18: [10, inf] | mock iraq 's | Mock_execution |
| 394. | policies | 18: [10, 5.0], 48: [14, inf] | policies 's russia | Visa_policy_of_Russia |
| 395. | citing | 18: [10, inf] | citing 's government | Federal_government_of_the_United_States |
| 396. | command | 18: [14, 7.0], 36: [12, inf] | command 's united | United_Nations_Command |
| 397. | bishop | 18: [16, 5.33], 48: [22, inf] | bishop china vatican | China–Holy_See_relations |
| 398. | bishops | 18: [12, inf] | bishops vatican church | Second_Vatican_Council |
| 399. | canadian | 18: [15, 5.0], 20: [13, inf], 38: [21, inf], 49: [15, 15.0] | canadian canada 's | Canada |
| 400. | resignation | 18: [11, inf], 26: [11, 11.0] | resignation 's mr. | Mr._Holland's_Opus |
| 401. | journalists | 18: [10, inf], 22: [10, inf], 34: [27, inf], 46: [12, inf] | journalists 's russia | List_of_journalists_killed_in_Russia |
| 402. | brazil | 18: [11, 5.5], 38: [13, inf] | brazil 's brazilian | Brazilian_Senate |
| 403. | armenian | 18: [11, inf], 30: [16, inf] | armenian genocide turkey | Armenian_Genocide_denial |
| 404. | young | 18: [18, 18.0], 29: [16, 16.0], 45: [10, 5.0], 50: [13, inf] | young 's people | Young_People_Fucking |
| 405. | tsunami | 18: [11, inf], 29: [15, inf], 52: [15, inf] | tsunami indonesia aceh | Aceh |
| 406. | roma | 18: [10, inf] | roma rights gypsies | Romani_people |
| 407. | dissidents | 18: [12, inf] | dissidents blair 's | Robert_Mugabe |
| 408. | girls | 19: [10, inf], 48: [14, inf] | girls china abuse | Sexual_abuse |
| 409. | peacekeepers | 19: [11, inf] | peacekeepers united nations | United_Nations_peacekeeping |
| 410. | battle | 19: [16, 5.33], 40: [10, inf] | battle 's killed | Killed_in_action |
| 411. | acquitted | 19: [11, inf] | acquitted 's africa | African_Americans |
| 412. | internet | 19: [16, 16.0], 47: [10, inf] | internet 's chinese | Internet_in_China |
| 413. | deployment | 19: [12, inf] | deployment people world | Rapid_deployment_force |
| 414. | king | 19: [10, inf], 47: [18, inf] | king 's nepal | King_of_Nepal |
| 415. | brigade | 19: [10, inf] | brigade iraq 's | Wolf_Brigade_(Iraq) |
| 416. | zuma | 19: [11, inf] | zuma south 's | Jacob_Zuma |
| 417. | guantánamo | 19: [13, inf], 24: [15, inf], 26: [10, inf] | guantánamo bay 's | Guantánamo_Bay |
| 418. | ready | 19: [12, inf] | ready 's iraq | Iraq_War |
| 419. | napolitano | 19: [10, inf] | napolitano president prodi | Romano_Prodi |
| 420. | exercise | 19: [10, inf] | exercise 's u.s. | U.S._state |
| 421. | trying | 19: [10, inf], 33: [10, 10.0] | trying 's iraq | Iraq_War |
| 422. | birds | 19: [10, inf] | birds flu bird | Avian_influenza |
| 423. | theft | 19: [10, inf] | theft 's russian | Horse_theft |
| 424. | baby | 19: [10, inf] | baby government 's | Baby_bonus |
| 425. | amin | 19: [10, inf] | amin trial 's | Idi_Amin |
| 426. | chávez | 19: [13, inf], 42: [15, inf] | chávez venezuela hugo | Hugo_Chávez |
| 427. | gasoline | 19: [10, inf] | gasoline pipeline people | Olympic_pipeline_explosion |
| 428. | suharto | 19: [10, inf] | suharto charges dropped | Suharto |
| 429. | charged | 19: [10, inf], 24: [15, 7.5], 29: [15, inf], 31: [17, 5.67], 34: [20, 6.67], 51: [23, 23.0] | charged 's police | Capitol_police |
| 430. | publicly | 20: [10, inf] | publicly 's mr. | Toyota_MR2 |
| 431. | resolution | 20: [12, 6.0], 28: [26, 6.5], 31: [23, 7.67], 41: [11, inf], 51: [13, 6.5] | resolution council 's | United_Nations_Security_Council_resolution |
| 432. | plants | 20: [14, inf] | plants nuclear power | Nuclear_power_plant |
| 433. | see | 20: [11, 5.5], 29: [10, inf] | see 's iraq | Iraq_War |
| 434. | assembly | 20: [10, inf], 23: [13, 6.5], 38: [20, 10.0] | assembly 's united | United_Nations_General_Assembly |
| 435. | term | 20: [24, 6.0], 31: [12, inf] | term 's president | List_of_presidents_of_the_United_States_by_time_in_office |
| 436. | protests | 20: [10, 5.0], 38: [16, 5.33], 43: [10, inf] | protests 's government | Protest |
| 437. | speech | 20: [12, inf], 22: [10, inf], 25: [11, 11.0], 48: [13, 13.0] | speech 's mr. | Tear_down_this_wall! |
| 438. | wanted | 20: [10, inf] | wanted 's iraq | Most-wanted_Iraqi_playing_cards |
| 439. | dutch | 20: [11, inf], 34: [11, 5.5], 47: [22, 5.5] | dutch 's government | Dutch_government-in-exile |
| 440. | short | 20: [11, inf] | short 's government | Federal_government_of_the_United_States |
| 441. | mubarak | 20: [10, 5.0], 26: [12, inf] | mubarak egypt egyptian | Egyptian_revolution_of_2011 |
| 442. | peruvian | 20: [10, inf] | peruvian peru fujimori | Alberto_Fujimori |
| 443. | seems | 20: [11, inf], 39: [12, 12.0], 48: [10, 5.0] | seems 's iraq | Iraq |
| 444. | reform | 20: [12, inf], 31: [10, inf], 38: [10, 5.0] | reform world 's | Reform_Party_of_the_United_States_of_America |
| 445. | supreme | 20: [12, inf] | supreme 's court | Supreme_Court_of_the_United_States |
| 446. | lebanon | 20: [10, inf], 28: [51, inf] | lebanon israel hezbollah | 2006_Lebanon_War |
| 447. | medical | 20: [11, 5.5], 22: [13, inf] | medical 's russia | List_of_medical_schools_in_Russia |
| 448. | told | 20: [10, 10.0], 23: [13, inf], 25: [15, 5.0], 31: [18, 6.0] | told 's iraq | 2003_invasion_of_Iraq |
| 449. | exchange | 20: [10, 5.0], 48: [10, inf] | exchange 's would | Intercontinental_Exchange |
| 450. | peru | 20: [22, inf] | peru 's fujimori | Alberto_Fujimori |
| 451. | presidential | 20: [16, 5.33], 23: [15, inf], 26: [16, 16.0], 31: [17, inf], 35: [12, 12.0], 50: [17, 5.67] | presidential 's election | United_States_presidential_election |
| 452. | orthodox | 20: [10, inf], 48: [10, 5.0] | orthodox pope 's | Pope_of_the_Coptic_Orthodox_Church_of_Alexandria |
| 453. | typhoon | 20: [14, inf], 48: [10, inf] | typhoon china people | Typhoon_Haiyan |
| 454. | santiago | 20: [12, inf] | santiago chile peru | Santiago |
| 455. | together | 21: [10, inf], 38: [12, inf] | together 's iraq | Iraq_War |
| 456. | governor | 21: [13, inf], 37: [20, 6.67] | governor 's killed | The_Governor_(The_Walking_Dead) |
| 457. | million | 21: [14, inf], 31: [21, 5.25], 38: [19, 9.5], 43: [33, inf], 48: [12, 12.0], 50: [13, 13.0] | million 's government | Federal_government_of_the_United_States |
| 458. | washington | 21: [11, 11.0], 30: [10, inf] | washington 's united | Washington |
| 459. | talks | 21: [26, inf], 44: [26, 13.0] | talks iran 's | Iran–United_States_relations |
| 460. | june | 21: [14, inf] | june russia 's | Russia |
| 461. | work | 21: [15, 7.5], 28: [11, inf], 38: [11, 5.5], 52: [10, inf] | work 's united | Copyright_status_of_works_by_the_federal_government_of_the_United_States |
| 462. | coming | 21: [10, inf] | coming 's government | Coming_out |
| 463. | aziz | 21: [11, inf] | aziz hamas 's | Abdel_Aziz_al-Rantisi |
| 464. | australian | 21: [17, inf], 48: [12, inf] | australian 's government | Australian_Government |
| 465. | timor | 21: [19, inf], 25: [13, inf] | timor east violence | Indonesian_occupation_of_East_Timor |
| 466. | drivers | 21: [12, inf] | drivers russian russia | Formula_One_drivers_from_Russia |
| 467. | john | 21: [13, 6.5], 25: [10, 10.0], 35: [23, 11.5], 49: [12, inf] | john 's iraq | Iraq_War |
| 468. | parade | 21: [10, inf] | parade party russian | Moscow_Victory_Parade_of_1945 |
| 469. | polar | 21: [12, inf] | polar bear hunting | Polar_bear |
| 470. | sainthood | 21: [11, inf] | sainthood poland pope | Pope_John_Paul_II |
| 471. | lebanese | 22: [14, 14.0], 28: [10, inf], 38: [10, 5.0] | lebanese lebanon hezbollah | 2006_Lebanon_War |
| 472. | crash | 22: [11, inf], 34: [10, inf], 38: [11, 11.0], 40: [12, 6.0] | crash plane people | 2006_New_York_City_plane_crash |
| 473. | accident | 22: [10, inf] | accident 's people | List_of_people_who_died_in_traffic_collisions |
| 474. | convoy | 22: [13, inf] | convoy suicide killed | List_of_major_terrorist_incidents |
| 475. | kabul | 22: [17, inf], 36: [11, inf] | kabul afghanistan afghan | Kabul |
| 476. | civilian | 22: [16, 8.0], 49: [10, inf] | civilian military 's | Civilian_control_of_the_military |
| 477. | long | 22: [11, 5.5], 41: [10, inf], 50: [12, 12.0] | long 's government | Copyright_status_of_works_by_the_federal_government_of_the_United_States |
| 478. | cbs | 22: [20, inf] | cbs news killed | CBS_News |
| 479. | note | 22: [18, inf] | note iraq 's | Iraq |
| 480. | risks | 22: [11, inf] | risks 's nuclear | Global_catastrophic_risk |
| 481. | fired | 22: [17, inf] | fired israel israeli | Israel |
| 482. | herald | 22: [26, inf] | herald international tribune | The_New_York_Times_International_Edition |
| 483. | kill | 22: [12, inf], 28: [11, 5.5] | kill israeli killed | Kill_off |
| 484. | rioting | 22: [14, inf] | rioting 's police | Police_riot |
| 485. | youths | 22: [28, inf] | youths paris police | List_of_incidents_of_civil_unrest_in_France |
| 486. | suburbs | 22: [16, inf] | suburbs paris youths | Banlieue |
| 487. | worst | 22: [14, inf] | worst 's government | The_Worst_Witch |
| 488. | unrest | 22: [15, inf] | unrest 's police | Ferguson_unrest |
| 489. | france | 22: [10, inf], 43: [11, 5.5] | france 's french | France |
| 490. | montfermeil | 22: [12, inf] | montfermeil youths violence | Les_Misérables_(2019_film) |
| 491. | clichy-sous-bois | 22: [10, inf] | clichy-sous-bois youths violence | 2005_French_riots |
| 492. | haditha | 22: [18, inf] | haditha iraqi iraq | Haditha_massacre |
| 493. | story | 22: [14, 14.0], 41: [13, inf] | story russia russian | Christmas_in_Russia |
| 494. | hospital | 22: [10, inf] | hospital 's officials | List_of_U.S._statewide_elected_officials |
| 495. | prepared | 22: [11, inf] | prepared 's russia | Peter_III_of_Russia |
| 496. | criticized | 22: [11, inf] | criticized 's iraq | 2003_invasion_of_Iraq |
| 497. | playing | 22: [10, inf] | playing 's military | Military |
| 498. | croquet | 22: [10, inf] | croquet playing prescott | John_Prescott |
| 499. | tribunal | 22: [12, inf], 28: [12, 6.0], 31: [10, inf] | tribunal crimes milosevic | Trial_of_Slobodan_Milošević |
| 500. | prescott | 22: [10, inf] | prescott prime minister | John_Prescott |
| 501. | running | 22: [10, inf] | running 's mr. | Running_with_Scissors_with_Mr._Interesting |
| 502. | finds | 22: [12, inf], 48: [10, 10.0] | finds 's report | U.S._News_&_World_Report |
| 503. | passengers | 22: [10, inf], 32: [10, 5.0] | passengers 's security | Airport_security |
| 504. | foul | 22: [10, inf] | foul milosevic death | Death_of_Slobodan_Milošević |
| 505. | play | 22: [10, inf] | play 's role | Role-playing |
| 506. | evidence | 22: [12, inf], 43: [11, 5.5] | evidence 's says | Evidence |
| 507. | prince | 22: [10, inf] | prince 's charles | Charles,_Prince_of_Wales |
| 508. | taking | 22: [14, inf] | taking 's iraq | Iraq |
| 509. | counterterrorism | 22: [10, inf] | counterterrorism british bush | George_W._Bush |
| 510. | sailor | 22: [10, inf] | sailor american killing | List_of_Sailor_Moon_characters |
| 511. | levels | 23: [13, inf] | levels iraq 's | Iraq |
| 512. | six | 23: [14, 7.0], 26: [13, inf] | six 's people | Six_degrees_of_separation |
| 513. | operation | 23: [13, 6.5], 32: [16, 5.33], 44: [11, inf] | operation 's israeli | Operation_Entebbe |
| 514. | suspects | 23: [15, 15.0], 45: [13, inf] | suspects police 's | Suspect |
| 515. | somaliland | 23: [10, inf] | somaliland somalia signs | British_Somaliland |
| 516. | referendum | 23: [15, inf] | referendum 's russia | Russian_interference_in_the_2016_Brexit_referendum |
| 517. | hold | 23: [13, inf] | hold 's world | World,_Hold_On_(Children_of_the_Sky) |
| 518. | review | 23: [10, 5.0], 25: [12, inf] | review 's russia | The_Russian_Review |
| 519. | plot | 23: [28, 9.33], 32: [37, inf] | plot suspects british | The_Usual_Suspects |
| 520. | date | 23: [16, inf] | date 's set | Dating |
| 521. | aides | 23: [12, inf], 36: [11, inf] | aides 's mr. | White_House_social_aide |
| 522. | high | 23: [11, inf] | high 's people | High_people's_court |
| 523. | unified | 23: [10, inf] | unified 's russia | Unified_S-band |
| 524. | warlords | 23: [10, inf] | warlords somalia mogadishu | United_Nations_Operation_in_Somalia_II |
| 525. | c.i.a | 23: [28, inf] | c.i.a european europe | Europe |
| 526. | later | 23: [14, inf] | later 's iraq | Iraq_War |
| 527. | sweden | 23: [10, inf], 31: [14, 7.0] | sweden 's european | 2019_European_Parliament_election_in_Sweden |
| 528. | jordan | 23: [13, 6.5], 38: [11, inf] | jordan people world | Demographics_of_Jordan |
| 529. | railway | 23: [12, inf] | railway state chinese | China_Railway |
| 530. | jews | 23: [10, inf] | jews jewish israel | Israeli_Jews |
| 531. | chance | 23: [11, inf] | chance 's iraq | Iraq |
| 532. | surveillance | 23: [17, inf] | surveillance 's police | Mass_surveillance |
| 533. | aircraft | 23: [13, inf] | aircraft russian 's | Russian_aircraft_carrier_Admiral_Kuznetsov |
| 534. | eichmann | 23: [12, inf] | eichmann c.i.a documents | Adolf_Eichmann |
| 535. | documents | 23: [11, inf] | documents russia russian | Russians |
| 536. | reach | 23: [12, 12.0], 38: [15, inf] | reach 's people | Reach_(S_Club_7_song) |
| 537. | annan | 23: [10, 5.0], 29: [14, inf], 35: [47, 7.83] | annan general kofi | Kojo_Annan |
| 538. | delegation | 23: [10, inf] | delegation 's government | Government_Delegation_for_Poland |
| 539. | migration | 23: [13, inf], 29: [15, inf] | migration russian russia | Russia |
| 540. | mayor | 23: [10, 5.0], 35: [11, inf] | mayor 's russia | Mayor |
| 541. | wife | 23: [10, inf] | wife 's mr. | The_Bishop's_Wife |
| 542. | get | 23: [13, 6.5], 25: [10, inf] | get 's iraq | Islamic_State_of_Iraq_and_the_Levant |
| 543. | beach | 23: [10, inf] | beach israel israeli | Israel |
| 544. | zarqawi | 23: [31, inf] | zarqawi 's iraq | Abu_Musab_al-Zarqawi |
| 545. | musab | 23: [35, inf] | musab abu al-zarqawi | Abu_Musab_al-Zarqawi |
| 546. | al-zarqawi | 23: [36, inf] | al-zarqawi abu musab | Abu_Musab_al-Zarqawi |
| 547. | airstrike | 23: [13, inf] | airstrike israel israeli | 2019_Israeli_airstrikes_in_Iraq |
| 548. | gorbachev | 23: [10, inf] | gorbachev 's russia | Mikhail_Gorbachev |
| 549. | truce | 23: [12, inf], 31: [13, 6.5], 51: [12, inf] | truce israel cease-fire | Ceasefire |
| 550. | wine | 23: [12, inf] | wine europe european | Wine |
| 551. | berlin | 23: [12, inf], 39: [11, 5.5] | berlin 's germany | Berlin |
| 552. | tajikistan | 24: [13, inf] | tajikistan russia 's | Russia–Tajikistan_relations |
| 553. | provide | 24: [13, inf] | provide 's iraq | Iraq |
| 554. | abuse | 24: [12, inf] | abuse military 's | Abuse |
| 555. | named | 24: [10, inf] | named 's world | The_World's_Billionaires |
| 556. | alert | 24: [11, inf] | alert 's lava | Mayon |
| 557. | kosovo | 24: [14, inf], 30: [12, inf], 43: [12, inf] | kosovo serbia 's | Kosovo–Serbia_relations |
| 558. | recall | 24: [10, inf] | recall 's president | Recall_election |
| 559. | legislature | 24: [10, inf] | legislature 's president | President_of_the_United_States |
| 560. | business | 24: [10, 5.0], 36: [12, 12.0], 49: [10, inf] | business 's russian | Russian_Business_Network |
| 561. | criminal | 24: [13, 13.0], 29: [13, inf], 42: [15, 7.5], 45: [10, inf] | criminal 's russia | Russian_criminal_tattoos |
| 562. | withdrawal | 24: [11, inf], 48: [11, 5.5] | withdrawal iraq 's | Withdrawal_of_U.S._troops_from_Iraq_(2020–21) |
| 563. | seizure | 24: [10, inf] | seizure 's israel | Israeli–Palestinian_conflict |
| 564. | chechen | 24: [12, inf], 28: [19, inf] | chechen russia russian | Chechen–Russian_conflict |
| 565. | missing | 24: [22, 11.0], 28: [10, inf], 36: [14, 14.0] | missing people two | Missing_People |
| 566. | wars | 25: [10, inf] | wars 's milosevic | Serbia_in_the_Yugoslav_Wars |
| 567. | penalty | 25: [11, inf] | penalty death hussein | Execution_of_Saddam_Hussein |
| 568. | congo | 25: [10, inf], 31: [12, 12.0], 34: [16, 5.33], 44: [19, 6.33] | congo election 's | Republic_of_the_Congo |
| 569. | socialist | 25: [12, inf] | socialist 's party | Socialist_Party_USA |
| 570. | disease | 25: [19, inf] | disease bird flu | Avian_influenza |
| 571. | presence | 25: [14, inf] | presence iraq 's | Iraq |
| 572. | korean | 25: [16, inf] | korean north korea | North_Korea–South_Korea_relations |
| 573. | sexual | 25: [11, inf], 42: [12, inf] | sexual charges 's | Daniel_Holtzclaw |
| 574. | tensions | 25: [10, inf], 31: [10, inf] | tensions 's russia | Russia |
| 575. | vatican | 25: [24, inf], 28: [13, inf], 46: [22, 22.0], 48: [18, inf] | vatican pope 's | Pope_John_Paul_I_conspiracy_theories |
| 576. | cardinal | 25: [20, inf], 48: [16, inf] | cardinal vatican pope | Pope_John_XXIII |
| 577. | age | 25: [10, inf] | age 's world | Age_of_Earth |
| 578. | course | 25: [11, inf], 49: [13, 13.0] | course 's iraq | Iran–Iraq_War |
| 579. | defectors | 25: [10, inf] | defectors north korean | North_Korean_defectors |
| 580. | hit | 26: [12, 6.0], 28: [13, inf] | hit 's iraq | Hit,_Iraq |
| 581. | diplomats | 26: [11, inf], 34: [10, 5.0] | diplomats iran 's | Iran_hostage_crisis |
| 582. | sentenced | 26: [20, 10.0], 34: [11, inf], 44: [10, 5.0] | sentenced years prison | List_of_longest_prison_sentences |
| 583. | give | 26: [13, inf], 49: [12, inf] | give 's government | Federal_government_of_the_United_States |
| 584. | sought | 26: [10, inf], 28: [10, 5.0] | sought 's government | Government_of_India |
| 585. | allow | 26: [13, inf] | allow 's would | Allow_natural_death |
| 586. | bear | 26: [12, inf] | bear 's polar | Polar_bear |
| 587. | gilad | 26: [13, inf] | gilad israeli palestinian | Gilad_Shalit_prisoner_exchange |
| 588. | shalit | 26: [17, inf] | shalit israeli palestinian | Gilad_Shalit |
| 589. | release | 26: [13, inf], 34: [20, 6.67] | release 's israeli | Israeli_new_shekel |
| 590. | income | 26: [16, inf] | income 's million | Income_tax_in_the_United_States |
| 591. | biggest | 26: [12, inf] | biggest 's million | List_of_biggest_box-office_bombs |
| 592. | changes | 26: [12, inf] | changes 's government | Federal_government_of_the_United_States |
| 593. | candidates | 26: [11, inf], 30: [14, inf] | candidates 's election | List_of_candidates_in_the_2004_United_States_presidential_election |
| 594. | kony | 26: [12, inf], 46: [16, inf] | kony rebel leader | Joseph_Kony |
| 595. | lower | 26: [13, inf] | lower 's house | Lower_house |
| 596. | used | 26: [12, inf], 29: [19, inf], 33: [10, inf] | used 's iraq | Authorization_for_Use_of_Military_Force_Against_Iraq_Resolution_of_2002 |
| 597. | ruling | 26: [12, inf] | ruling 's court | Supreme_Court_of_India |
| 598. | kiragu | 26: [12, inf] | kiragu cocaine case | EMPTY MATCHING |
| 599. | win | 26: [11, inf], 37: [16, inf], 42: [11, 5.5] | win 's party | WIN_Party |
| 600. | demand | 27: [10, inf], 38: [12, 6.0] | demand 's iran | Iran |
| 601. | senegal | 27: [10, inf] | senegal african spain | COVID-19_pandemic_in_Senegal |
| 602. | winner | 27: [12, inf] | winner 's election | List_of_United_States_presidential_elections_in_which_the_winner_lost_the_popular_vote |
| 603. | summit | 27: [14, inf] | summit russia 's | 2018_Russia–United_States_summit |
| 604. | calderón | 27: [19, inf] | calderón mexico felipe | Felipe_Calderón |
| 605. | hours | 27: [11, inf] | hours 's president | President_of_the_United_States |
| 606. | race | 27: [11, inf], 36: [14, 7.0], 42: [29, inf], 50: [10, 5.0] | race 's election | 2006_United_States_Senate_elections |
| 607. | andrés | 27: [10, inf] | andrés mexico lópez | Andrés_Manuel_López_Obrador |
| 608. | manuel | 27: [16, 5.33], 31: [12, inf] | manuel mexico obrador | Andrés_Manuel_López_Obrador |
| 609. | leftist | 27: [22, 11.0], 31: [18, inf] | leftist 's mexico | Mexico |
| 610. | broke | 27: [10, inf] | broke 's government | Divided_government_in_the_United_States |
| 611. | prosecution | 27: [10, inf] | prosecution 's trial | Witness_for_the_Prosecution_(1957_film) |
| 612. | shows | 27: [15, inf], 32: [12, inf] | shows 's russia | Russia |
| 613. | deadlock | 27: [12, inf] | deadlock ukraine 's | War_in_Donbass |
| 614. | tymoshenko | 27: [12, inf] | tymoshenko 's ukraine | Yulia_Tymoshenko |
| 615. | macedonia | 27: [12, inf] | macedonia government europe | North_Macedonia |
| 616. | numbers | 27: [12, inf], 29: [16, 8.0] | numbers iraq 's | Iraq |
| 617. | accept | 27: [13, inf], 29: [11, inf] | accept 's mr. | Mr._Mayor |
| 618. | questions | 27: [12, inf] | questions 's iraq | Iraq_War |
| 619. | tally | 27: [11, inf] | tally vote 's | Tally_(voting) |
| 620. | remained | 27: [14, inf], 31: [11, 5.5] | remained 's people | The_Remaining |
| 621. | french | 27: [12, inf] | french 's france | France |
| 622. | complaint | 27: [12, inf] | complaint 's trial | Complaint |
| 623. | dreyfus | 27: [12, inf] | dreyfus years army | Alfred_Dreyfus |
| 624. | museum | 27: [16, 8.0], 43: [10, inf] | museum government 's | Government_Museum,_Mathura |
| 625. | marred | 27: [10, inf] | marred election 's | Mar-a-Lago |
| 626. | guggenheim | 27: [14, inf] | guggenheim abu dhabi | Guggenheim_Abu_Dhabi |
| 627. | dhabi | 27: [20, inf] | dhabi abu guggenheim | Guggenheim_Abu_Dhabi |
| 628. | actions | 28: [10, inf] | actions 's russia | United_States_involvement_in_regime_change |
| 629. | oxfam | 28: [12, inf] | oxfam aid darfur | Oxfam |
| 630. | director | 28: [11, inf] | director 's russia | Russia |
| 631. | comments | 28: [11, inf] | comments 's iran | Iran–United_States_relations |
| 632. | shamil | 28: [11, inf] | shamil chechen 's | Shamil_Basayev |
| 633. | basayev | 28: [17, inf] | basayev chechen 's | Shamil_Basayev |
| 634. | hague | 28: [11, inf] | hague trial crimes | War_crime |
| 635. | follow | 28: [10, inf] | follow 's iraq | Iraq |
| 636. | pinochet | 28: [10, inf], 52: [12, 6.0] | pinochet chile augusto | Military_dictatorship_of_Chile_(1973–1990) |
| 637. | made | 28: [22, inf] | made 's iraq | Iraq_War |
| 638. | legal | 28: [12, inf], 48: [10, 5.0], 50: [10, 5.0] | legal 's rights | Natural_rights_and_legal_rights |
| 639. | landing | 28: [10, inf] | landing plane jet | Jay_Jay_the_Jet_Plane |
| 640. | aceh | 28: [14, inf] | aceh tsunami law | Aceh |
| 641. | videos | 28: [10, inf] | videos vote 's | Video_the_Vote |
| 642. | satellite | 28: [32, inf], 33: [12, 12.0] | satellite 's television | Satellite_television |
| 643. | space | 28: [12, inf], 44: [11, inf] | space satellite russia | Satellite |
| 644. | insat | 28: [12, inf] | insat satellite india | Indian_National_Satellite_System |
| 645. | failure | 28: [11, inf], 41: [13, inf] | failure 's mr. | Failure_to_Launch |
| 646. | raised | 28: [10, inf] | raised 's government | Federal_government_of_the_United_States |
| 647. | pen | 28: [12, inf] | pen france 's | Jean-Marie_Le_Pen |
| 648. | remarks | 28: [16, inf] | remarks 's iraq | 2003_invasion_of_Iraq |
| 649. | beirut | 28: [16, inf], 48: [28, 5.6] | beirut lebanon hezbollah | Hezbollah |
| 650. | hezbollah | 28: [48, inf] | hezbollah israel lebanon | 2006_Lebanon_War |
| 651. | asked | 28: [14, inf] | asked 's government | FAQ |
| 652. | tablets | 28: [20, inf] | tablets iran court | Persepolis_Administrative_Archives |
| 653. | mumbai | 28: [15, inf] | mumbai india pakistan | 2008_Mumbai_attacks |
| 654. | opens | 28: [13, inf] | opens world 's | Open_world |
| 655. | offered | 28: [14, inf] | offered 's iraq | 2003_invasion_of_Iraq |
| 656. | airstrikes | 28: [11, inf] | airstrikes israeli israel | 2019_Israeli_airstrikes_in_Iraq |
| 657. | arab | 29: [22, 11.0], 32: [15, 7.5], 38: [13, 6.5], 46: [13, inf] | arab 's sunni | Arab_states–Israeli_alliance_against_Iran |
| 658. | fighting | 29: [30, 10.0], 38: [10, inf], 41: [12, 12.0] | fighting israel 's | Israel_Adesanya |
| 659. | fierce | 29: [12, 6.0], 35: [10, inf] | fierce israel israeli | 1948_Arab–Israeli_War |
| 660. | small | 29: [15, inf], 41: [11, 5.5] | small 's police | Police |
| 661. | offers | 29: [12, inf], 34: [13, 6.5] | offers 's iraq | 2003_invasion_of_Iraq |
| 662. | poles | 29: [12, inf], 46: [10, inf] | poles poland labor | History_of_Jews_in_Poland |
| 663. | peacekeeping | 29: [11, inf], 34: [21, 7.0] | peacekeeping force united | United_Nations_peacekeeping |
| 664. | leave | 29: [10, inf], 36: [16, inf] | leave 's united | Maternity_leave_in_the_United_States |
| 665. | discuss | 29: [10, inf], 41: [10, inf] | discuss 's russia | Timeline_of_Russian_interference_in_the_2016_United_States_elections |
| 666. | service | 29: [17, 8.5], 49: [11, inf] | service 's russian | Federal_Security_Service |
| 667. | blind | 29: [10, inf] | blind iraq 's | 2003_invasion_of_Iraq |
| 668. | plastic | 29: [21, inf] | plastic bags 's | Plastic_bag |
| 669. | blogs | 29: [13, inf] | blogs government india | Blog |
| 670. | deaths | 29: [10, inf], 31: [11, inf] | deaths iraq military | Casualties_of_the_Iraq_War |
| 671. | hills | 29: [14, inf] | hills 's house | The_Haunting_of_Hill_House |
| 672. | gazeta | 29: [13, inf], 31: [20, inf] | gazeta russia russian | Novaya_Gazeta |
| 673. | russias | 29: [10, 10.0], 31: [31, inf], 34: [26, inf], 39: [10, inf] | russias russia russian | Russia |
| 674. | abkhazia | 29: [10, inf] | abkhazia russia russian | Abkhazia |
| 675. | article | 29: [12, inf] | article russia russian | Russia |
| 676. | ground | 29: [28, inf] | ground 's iraq | Iraqi_Army |
| 677. | bolton | 29: [12, inf], 49: [28, inf] | bolton united nations | John_Bolton |
| 678. | families | 29: [10, inf] | families people 's | The_People_of_Family |
| 679. | advocate | 29: [10, inf], 48: [10, inf] | advocate rights chinese | LGBT_rights_in_China |
| 680. | hirohito | 29: [10, inf] | hirohito shrine diaries | Hirohito |
| 681. | higher | 30: [10, inf] | higher 's russian | List_of_institutions_of_higher_education_in_Russia |
| 682. | experiencing | 30: [11, inf] | experiencing europe government | E-government_in_Europe |
| 683. | cash | 30: [12, inf] | cash million 's | Mega_Millions |
| 684. | traditional | 30: [13, inf] | traditional 's `` | Traditional_pop |
| 685. | lanka | 30: [11, inf], 35: [14, inf], 42: [15, 7.5], 45: [24, 8.0], 52: [14, 14.0] | lanka sri rebels | Sri_Lankan_Civil_War |
| 686. | verdict | 30: [10, inf] | verdict trial 's | Verdict |
| 687. | duty | 30: [10, inf] | duty `` officers | Duty_officer |
| 688. | firing | 30: [12, inf] | firing israel rockets | Palestinian_rocket_attacks_on_Israel |
| 689. | site | 30: [12, inf] | site 's web | Website |
| 690. | helicopter | 30: [10, inf] | helicopter military 's | Military_helicopter |
| 691. | zakayev | 30: [14, inf] | zakayev russia chechen | Akhmed_Zakayev |
| 692. | execution | 30: [17, inf], 52: [23, 11.5] | execution hussein saddam | Execution_of_Saddam_Hussein |
| 693. | appeal | 30: [16, inf], 36: [10, inf] | appeal 's russian | Pine_Tree_Flag |
| 694. | detained | 30: [14, inf], 39: [10, 10.0] | detained 's russian | Russian_interference_in_the_2016_United_States_elections |
| 695. | aleksandr | 30: [13, inf] | aleksandr 's russia | Aleksandr_Solzhenitsyn |
| 696. | headed | 30: [10, inf] | headed russian russia | Russia |
| 697. | monitors | 30: [12, inf], 35: [13, inf] | monitors sri government | List_of_government-owned_companies_of_Sri_Lanka |
| 698. | tigers | 30: [14, inf] | tigers sri tamil | Liberation_Tigers_of_Tamil_Eelam |
| 699. | g | 31: [10, inf] | g russia summit | List_of_G20_summits |
| 700. | irrigation | 31: [18, inf] | irrigation sri government | Ministry_of_Irrigation_and_Water_Resources_Management |
| 701. | canal | 31: [18, 18.0], 35: [10, inf], 43: [10, inf] | canal sri government | Sethusamudram_Shipping_Canal_Project |
| 702. | barrel | 31: [10, inf] | barrel oil russia | 2020_Russia–Saudi_Arabia_oil_price_war |
| 703. | obrador | 31: [14, inf], 37: [12, 6.0] | obrador mexico manuel | Andrés_Manuel_López_Obrador |
| 704. | raid | 31: [17, 8.5], 33: [22, 5.5], 38: [11, inf], 49: [10, inf] | raid police israeli | Yamam |
| 705. | calm | 31: [10, 5.0], 33: [10, inf] | calm 's palestinian | Israeli–Palestinian_conflict |
| 706. | clerics | 31: [10, inf], 39: [12, inf] | clerics iraq government | Muqtada_al-Sadr |
| 707. | artillery | 31: [11, inf] | artillery israel israeli | Israel |
| 708. | -year-old | 31: [14, inf] | -year-old 's mr. | Riemann_hypothesis |
| 709. | kommersant | 31: [11, inf] | kommersant russia russian | Kommersant |
| 710. | companies | 31: [16, 16.0], 46: [10, inf] | companies 's russian | List_of_companies_of_Russia |
| 711. | izvestia | 31: [11, inf] | izvestia russia russian | Izvestia |
| 712. | nezavisimaya | 31: [11, inf] | nezavisimaya russia russian | Nezavisimaya_Gazeta |
| 713. | claims | 31: [10, inf] | claims 's russia | Territorial_claims_in_the_Arctic |
| 714. | fidel | 31: [17, inf] | fidel castro cuba | Cuba_under_Fidel_Castro |
| 715. | castro | 31: [31, inf] | castro fidel cuba | Cuba_under_Fidel_Castro |
| 716. | cuba | 31: [17, inf] | cuba castro 's | Fidel_Castro |
| 717. | currency | 31: [12, inf] | currency zimbabwe 's | Zimbabwean_dollar |
| 718. | zimbabweans | 31: [10, inf] | zimbabweans zimbabwe currency | Zimbabwean_dollar |
| 719. | ''the | 31: [10, inf] | ''the 's government | Federal_government_of_the_United_States |
| 720. | inquiry | 31: [10, inf] | inquiry 's police | Undercover_Policing_Inquiry |
| 721. | aimed | 31: [15, inf] | aimed 's iran | Iran |
| 722. | center | 31: [12, inf] | center 's russia | Russia |
| 723. | ministry | 31: [13, inf] | ministry 's russia | Ministry_of_Defence_(Russia) |
| 724. | activists | 31: [12, inf] | activists russia 's | The_Other_Russia_(party) |
| 725. | criminals | 31: [10, inf] | criminals 's japan | Japanese_war_crimes |
| 726. | rape | 31: [11, inf] | rape 's soldiers | Mahmudiyah_rape_and_killings |
| 727. | crime | 31: [10, inf] | crime 's government | Federal_government_of_the_United_States |
| 728. | vacation | 31: [11, inf] | vacation russias russian | Russo-Ukrainian_War |
| 729. | areas | 31: [12, 6.0], 33: [10, 10.0], 49: [12, inf] | areas 's iraq | Iraq |
| 730. | reactor | 31: [12, inf], 47: [16, inf] | reactor nuclear iran | Nuclear_facilities_in_Iran |
| 731. | bridge | 31: [11, inf] | bridge iraq 's | 2003_invasion_of_Iraq |
| 732. | build | 31: [12, 6.0], 38: [18, inf] | build 's world | Build_the_Earth |
| 733. | marines | 31: [10, inf], 45: [16, 16.0], 51: [15, inf] | marines iraq military | 2003_invasion_of_Iraq |
| 734. | draft | 31: [10, inf], 43: [13, inf] | draft resolution council | United_Nations_Security_Council_resolution |
| 735. | tell | 32: [10, inf] | tell iraq 's | Tell_al-'Ubaid |
| 736. | away | 32: [16, 8.0], 43: [10, inf] | away 's iraq | Iraq_War |
| 737. | river | 32: [12, inf] | river 's china | List_of_rivers_of_China |
| 738. | proposed | 32: [12, inf] | proposed 's russian | Timeline_of_Russian_interference_in_the_2016_United_States_elections |
| 739. | dozen | 32: [12, inf], 38: [10, 5.0] | dozen 's people | Dozen |
| 740. | influence | 32: [10, inf] | influence 's iraq | Iraqi_insurgency_(2003–2011) |
| 741. | watch | 32: [11, inf] | watch rights 's | Human_Rights_Watch |
| 742. | dagestan | 32: [18, inf] | dagestan russia killed | List_of_journalists_killed_in_Russia |
| 743. | spying | 32: [12, inf] | spying government china | Chinese_intelligence_activity_abroad |
| 744. | executed | 32: [10, inf] | executed 's execution | List_of_offenders_executed_in_the_United_States_in_2020 |
| 745. | airports | 32: [12, inf] | airports security 's | Airport_security |
| 746. | liquid | 32: [26, inf] | liquid explosives security | Explosive |
| 747. | gang | 32: [17, inf] | gang police attacks | Glenanne_gang |
| 748. | asylum | 32: [18, 9.0], 35: [10, inf] | asylum 's russia | Edward_Snowden_asylum_in_Russia |
| 749. | airliners | 32: [16, inf] | airliners plot british | Timeline_of_airliner_bombing_attacks |
| 750. | liquids | 32: [10, inf] | liquids security carry-on | 2006_transatlantic_aircraft_plot_security_reaction |
| 751. | greenland | 32: [12, inf] | greenland ice study | Greenland_ice_sheet |
| 752. | melting | 32: [10, inf] | melting greenland ice | Greenland_ice_sheet |
| 753. | fragile | 33: [11, inf] | fragile 's government | List_of_countries_by_Fragile_States_Index |
| 754. | seemed | 33: [13, inf] | seemed 's mr. | Mr._Queen |
| 755. | streets | 33: [10, inf] | streets 's people | Street_people |
| 756. | speaker | 33: [12, inf] | speaker parliament party | Speaker_of_the_Parliament_of_Ghana |
| 757. | grouse | 33: [10, inf] | grouse -- britain | Red_grouse |
| 758. | data | 33: [10, inf] | data european 's | Data_Protection_Directive |
| 759. | memorial | 33: [10, inf] | memorial japan shrine | Yasukuni_Shrine |
| 760. | aristide | 33: [14, inf] | aristide haiti president | Jean-Bertrand_Aristide |
| 761. | charges | 33: [20, 5.0], 44: [23, 5.75], 48: [12, 6.0], 50: [14, inf] | charges 's mr. | Mr._Mayor |
| 762. | avoid | 33: [13, inf] | avoid 's iraq | 2003_invasion_of_Iraq |
| 763. | ramon | 33: [12, inf] | ramon sexual israel | Haim_Ramon |
| 764. | colombia | 33: [12, inf] | colombia 's world | Colombia |
| 765. | coca | 33: [12, inf] | coca colombia u.s. | Coca_production_in_Colombia |
| 766. | pilgrimage | 33: [12, inf] | pilgrimage pilgrims security | Pilgrim |
| 767. | challenges | 33: [10, inf] | challenges 's people | The_Challenge_(TV_series) |
| 768. | umarov | 33: [12, inf] | umarov leader mr. | Chechen–Russian_conflict |
| 769. | kurds | 34: [16, inf] | kurds hussein trial | Trial_of_Saddam_Hussein |
| 770. | finance | 34: [10, inf] | finance 's bank | AU_Small_Finance_Bank |
| 771. | film | 34: [14, inf] | film 's `` | Soul_(2020_film) |
| 772. | journalist | 34: [10, inf], 41: [14, 7.0], 43: [11, inf], 47: [10, 5.0] | journalist 's russian | List_of_journalists_killed_in_Russia |
| 773. | turns | 34: [10, inf] | turns 's police | Police |
| 774. | progress | 34: [10, inf], 45: [11, inf] | progress 's iraq | 2003_invasion_of_Iraq |
| 775. | phones | 34: [13, inf] | phones 's russia | Mobile_phone_industry_in_Russia |
| 776. | peninsula | 35: [16, inf] | peninsula sri baja | List_of_peninsulas |
| 777. | militia | 35: [20, inf] | militia hezbollah lebanon | Hezbollah |
| 778. | caracas | 35: [13, inf] | caracas venezuela 's | Caracas |
| 779. | peace | 35: [12, inf], 38: [45, 6.43], 46: [12, inf] | peace 's government | John_Hagelin |
| 780. | early | 35: [10, 10.0], 40: [10, inf] | early 's iraq | Iraq_War |
| 781. | embassy | 35: [11, inf] | embassy 's russian | List_of_diplomatic_missions_of_Russia |
| 782. | blockade | 35: [16, inf] | blockade lebanon israel | 2006_Lebanon_War |
| 783. | siniora | 35: [10, inf] | siniora hezbollah lebanon | Hezbollah |
| 784. | hurricane | 35: [24, inf] | hurricane john coast | 2020_Atlantic_hurricane_season |
| 785. | winds | 35: [10, inf] | winds typhoon hurricane | Tropical_cyclone_scales |
| 786. | baja | 35: [14, inf] | baja peninsula california | Baja_California_Peninsula |
| 787. | gunman | 36: [12, inf] | gunman shot killing | The_Killing_Jar_(film) |
| 788. | find | 36: [15, inf], 40: [14, 7.0] | find 's iraq | Iraq_War |
| 789. | ends | 36: [10, inf] | ends 's russia | Russia |
| 790. | conviction | 36: [10, inf] | conviction court times | Curtis_Flowers |
| 791. | nine | 36: [11, inf] | nine 's iraq | Iraq_War |
| 792. | survey | 36: [10, 10.0], 45: [10, inf] | survey 's percent | Demographics_of_Georgia_(U.S._state) |
| 793. | dialogue | 37: [11, inf] | dialogue iraq 's | Withdrawal_of_U.S._troops_from_Iraq_(2020–21) |
| 794. | demanding | 37: [10, inf] | demanding 's president | George_Washington |
| 795. | faith | 37: [10, inf] | faith 's iraq | Religion_in_Iraq |
| 796. | islam | 37: [17, inf] | islam 's pope | Pope_Benedict_XVI_and_Islam |
| 797. | life | 37: [17, inf] | life 's iraq | Iraq_War |
| 798. | rabbis | 37: [15, inf] | rabbis germany ordained | Women_rabbis_and_Torah_scholars |
| 799. | ordained | 37: [11, inf] | ordained rabbis germany | Women_rabbis_and_Torah_scholars |
| 800. | taxi | 37: [10, inf] | taxi killed south | A_Taxi_Driver |
| 801. | suggested | 38: [10, inf] | suggested 's iraq | 2003_invasion_of_Iraq |
| 802. | citizens | 38: [16, 16.0], 50: [11, inf] | citizens 's russia | Visa_requirements_for_Russian_citizens |
| 803. | clinton | 38: [10, inf], 48: [11, inf] | clinton iraq 's | Hillary_Clinton |
| 804. | geneva | 38: [12, inf] | geneva rights human | History_of_human_rights |
| 805. | truckers | 38: [14, inf] | truckers halliburton two | Halliburton |
| 806. | lives | 38: [10, inf] | lives 's iraq | Iraq_War |
| 807. | armed | 38: [12, inf] | armed 's government | United_States_Armed_Forces |
| 808. | extremists | 38: [24, inf] | extremists people 's | Extremism |
| 809. | freedom | 38: [20, inf] | freedom 's world | Freedom_in_the_World |
| 810. | 're | 38: [10, inf], 49: [26, inf] | 're iraq 's | Iraq_War |
| 811. | regime | 38: [12, inf] | regime people world | Ancien_Régime |
| 812. | must | 38: [29, inf], 49: [13, inf] | must 's russia | Russian_interference_in_the_2016_United_States_elections |
| 813. | working | 38: [15, inf] | working 's iraq | Iraq_War |
| 814. | good | 38: [10, inf] | good 's iraq | Iraq_War |
| 815. | presidency | 38: [12, inf] | presidency 's people | List_of_presidents_of_the_United_States |
| 816. | corruption | 38: [12, 6.0], 42: [12, inf] | corruption 's president | President_of_the_United_States |
| 817. | postwar | 38: [12, inf] | postwar japan 's | Post-occupation_Japan |
| 818. | ferenc | 38: [10, inf] | ferenc hungary gyurcsany | Ferenc_Gyurcsány |
| 819. | gyurcsany | 38: [17, inf] | gyurcsany hungary prime | Ferenc_Gyurcsány |
| 820. | aims | 38: [11, inf] | aims india china | 2020_China–India_skirmishes |
| 821. | hungary | 38: [17, inf] | hungary gyurcsany prime | Ferenc_Gyurcsány |
| 822. | generator | 39: [10, inf] | generator tibetan iraqi | Asia |
| 823. | stirs | 39: [10, inf] | stirs 's debate | Debate_on_traditional_and_simplified_Chinese_characters |
| 824. | lawmakers | 39: [11, inf] | lawmakers 's iraq | Iraq_and_weapons_of_mass_destruction |
| 825. | brazilian | 39: [10, 5.0], 52: [11, inf] | brazilian brazil pilots | Music_of_Brazil |
| 826. | smoke | 39: [10, inf] | smoke 's people | Pop_Smoke |
| 827. | archbishop | 39: [12, inf] | archbishop vatican pope | Pope_Francis |
| 828. | opera | 39: [29, inf] | opera german canceled | Soap_opera |
| 829. | canceled | 39: [14, inf] | canceled opera 's | Soap_opera |
| 830. | zambia | 39: [10, inf] | zambia 's mwanawasa | Levy_Mwanawasa |
| 831. | jospin | 39: [10, inf] | jospin socialist french | Lionel_Jospin |
| 832. | tourists | 39: [10, inf] | tourists 's chinese | AAAAA_Tourist_Attractions_of_China |
| 833. | links | 40: [10, inf] | links 's russia | Links_between_Trump_associates_and_Russian_officials |
| 834. | pilots | 40: [16, inf], 48: [10, inf] | pilots jet brazilian | Gol_Transportes_Aéreos_Flight_1907 |
| 835. | collision | 40: [15, inf] | collision brazilian pilots | Gol_Transportes_Aéreos_Flight_1907 |
| 836. | nicaragua | 40: [10, 10.0], 43: [10, inf] | nicaragua ortega election | Daniel_Ortega |
| 837. | turkish | 40: [17, inf] | turkish turkey 's | Turkish_lira |
| 838. | hijacker | 40: [10, inf] | hijacker turkish acted | Turkish_Airlines_Flight_1476 |
| 839. | residents | 40: [10, inf], 51: [11, 5.5] | residents 's party | Political_party_strength_in_U.S._states |
| 840. | rural | 40: [10, inf] | rural 's government | Ministry_of_Local_Government,_Rural_Development_and_Co-operatives |
| 841. | summary | 41: [14, inf], 48: [12, 6.0] | summary russian russia | Christmas_in_Russia |
| 842. | stories | 41: [18, inf], 48: [15, 5.0] | stories russian russia | Christmas_in_Russia |
| 843. | politkovskaya | 41: [22, 11.0], 43: [14, inf] | politkovskaya 's russian | Anna_Politkovskaya |
| 844. | newspaper | 41: [15, inf] | newspaper 's russia | List_of_newspapers_in_Russia |
| 845. | device | 41: [15, inf] | device north korea | COVID-19_pandemic_in_North_Korea |
| 846. | qatar | 41: [15, inf] | qatar palestinian government | Politics_of_Qatar |
| 847. | torture | 41: [16, inf], 47: [11, inf] | torture rights 's | Torture |
| 848. | strip | 41: [12, 6.0], 47: [10, inf] | strip gaza palestinian | Gaza_Strip |
| 849. | highest | 41: [11, inf] | highest 's court | Supreme_Court_of_the_United_States |
| 850. | slain | 41: [12, inf] | slain 's russia | Pale_Fire |
| 851. | kazakhstan | 41: [10, inf] | kazakhstan 's russia | Russians_in_Kazakhstan |
| 852. | venezuela | 42: [23, inf] | venezuela chávez 's | Hugo_Chávez |
| 853. | balad | 42: [12, inf] | balad iraqi american | Balad_Air_Base |
| 854. | seat | 42: [14, inf] | seat world people | SEAT |
| 855. | guatemala | 42: [11, inf] | guatemala venezuela seat | 2006_United_Nations_Security_Council_election |
| 856. | lead | 42: [13, inf] | lead 's president | President_of_the_United_States |
| 857. | boats | 42: [11, inf] | boats sri rebels | Sea_Tigers |
| 858. | tunnels | 42: [10, inf] | tunnels gaza israeli | Israel–Gaza_barrier |
| 859. | ability | 42: [10, inf] | ability 's iraq | 2003_invasion_of_Iraq |
| 860. | scandal | 42: [11, inf], 50: [10, inf] | scandal 's corruption | Rampart_scandal |
| 861. | gets | 43: [10, inf] | gets 's iraq | Islamic_State_of_Iraq_and_the_Levant |
| 862. | language | 43: [16, inf] | language 's russia | Languages_of_Russia |
| 863. | york | 43: [11, inf] | york times 's | The_New_York_Times |
| 864. | nationalist | 43: [10, 5.0], 49: [14, inf] | nationalist 's russia | Russian_nationalism |
| 865. | break | 43: [11, inf] | break 's iraq | Iran–Iraq_War |
| 866. | without | 43: [10, inf], 46: [10, inf], 48: [16, 8.0] | without 's government | Federal_government_of_the_United_States |
| 867. | toward | 43: [10, inf] | toward 's government | Government_shutdowns_in_the_United_States |
| 868. | cameras | 43: [18, inf] | cameras 's people | Camera |
| 869. | prize | 43: [10, 5.0], 49: [13, inf] | prize nobel peace | Nobel_Peace_Prize |
| 870. | warming | 44: [20, 20.0], 50: [10, inf] | warming global climate | Climate_change |
| 871. | climate | 44: [17, inf] | climate 's warming | Climate_change |
| 872. | carbon | 44: [11, inf] | carbon power britain | Carbon_capture_and_storage |
| 873. | chen | 44: [18, inf] | chen party taiwan | Taiwan_Statebuilding_Party |
| 874. | abalone | 44: [14, inf] | abalone africa women | History_of_Africa |
| 875. | meet | 45: [12, 6.0], 48: [10, inf] | meet 's iraq | 2003_invasion_of_Iraq |
| 876. | cyprus | 45: [14, inf] | cyprus turkey union | Turkish_invasion_of_Cyprus |
| 877. | christians | 45: [10, inf] | christians pope 's | Pope |
| 878. | heavy | 45: [10, inf] | heavy officials killed | Killer_Be_Killed |
| 879. | guard | 45: [10, inf] | guard 's iraq | Republican_Guard_(Iraq) |
| 880. | gay | 45: [12, inf] | gay 's marriage | Same-sex_marriage_in_the_United_States |
| 881. | rally | 45: [12, inf] | rally 's iraq | Protests_against_the_Iraq_War |
| 882. | polygamy | 46: [10, inf] | polygamy tajikistan women | Legality_of_polygamy |
| 883. | change | 46: [10, inf] | change 's government | Federal_government_of_the_United_States |
| 884. | gypsies | 46: [10, inf] | gypsies slovenia rights | Romani_people |
| 885. | slovenia | 46: [12, inf] | slovenia gypsies family | Romani_people |
| 886. | wartime | 46: [16, inf] | wartime 's crimes | Japanese_war_crimes |
| 887. | same-sex | 46: [12, inf] | same-sex 's legal | Same-sex_marriage_in_the_United_States |
| 888. | marriages | 46: [13, inf] | marriages same-sex south | Same-sex_marriage |
| 889. | marriage | 46: [17, inf] | marriage 's vatican | Marriage |
| 890. | royal | 46: [10, inf] | royal 's nepal | Nepalese_royal_massacre |
| 891. | bemba | 46: [10, inf] | bemba congo election | Jean-Pierre_Bemba |
| 892. | pierre | 47: [10, inf] | pierre iraq 's | Iran–Iraq_War |
| 893. | gemayel | 47: [12, inf] | gemayel iraq 's | Amine_Gemayel |
| 894. | restore | 47: [10, inf] | restore 's people | Rally_to_Restore_Sanity_and/or_Fear |
| 895. | abuses | 47: [10, inf] | abuses rights 's | Human_rights |
| 896. | rubber | 47: [10, inf] | rubber 's mr. | Rubber_band |
| 897. | radiation | 47: [11, inf] | radiation russian litvinenko | Poisoning_of_Alexander_Litvinenko |
| 898. | polonium | 47: [11, inf] | polonium russian litvinenko | Poisoning_of_Alexander_Litvinenko |
| 899. | homes | 48: [10, inf] | homes people 's | Old_people's_home |
| 900. | paid | 48: [10, inf] | paid 's government | Federal_government_of_the_United_States |
| 901. | ex-spy | 48: [12, inf] | ex-spy russian litvinenko | Poisoning_of_Alexander_Litvinenko |
| 902. | religious | 48: [14, inf] | religious 's iran | Religion_in_Iran |
| 903. | treat | 48: [14, inf] | treat aids clinton | Chelsea_Clinton |
| 904. | memo | 48: [15, inf] | memo iraq bush | Bush–Blair_2003_Iraq_memo |
| 905. | text | 48: [10, inf] | text 's council | Text_messaging |
| 906. | adviser | 48: [12, inf] | adviser 's security | National_Security_Advisor_(United_States) |
| 907. | supporters | 48: [13, inf] | supporters 's election | 2020–21_United_States_election_protests |
| 908. | child | 48: [10, inf] | child 's world | Child_World |
| 909. | smoking | 48: [12, inf] | smoking ban public | Smoking_ban |
| 910. | deportation | 49: [10, inf] | deportation russian 's | Deportation |
| 911. | hunger | 49: [10, inf] | hunger strike 's | Hunger_strike |
| 912. | cities | 49: [10, inf] | cities 's iraq | Iraq |
| 913. | hamilton | 49: [17, inf] | hamilton iraq 's | Iraq_Study_Group |
| 914. | baker | 49: [24, inf] | baker iraq 's | James_Baker |
| 915. | recommend | 49: [14, inf] | recommend iraq 's | 2003_invasion_of_Iraq |
| 916. | 've | 49: [15, inf] | 've iraq people | Iraqi_Turkmen |
| 917. | us | 49: [17, inf] | us iraq 's | 2003_invasion_of_Iraq |
| 918. | think | 49: [21, inf] | think 's iraq | Iraq_and_weapons_of_mass_destruction |
| 919. | 'll | 49: [11, inf] | 'll 's iraq | List_of_United_States_Military_installations_in_Iraq |
| 920. | mayoral | 49: [11, inf] | mayoral 's russia | Borja_Mayoral |
| 921. | urge | 49: [13, inf] | urge 's united | Urge_(film) |
| 922. | bourdais | 50: [10, inf] | bourdais race toro | Sébastien_Bourdais |
| 923. | deniers | 50: [12, inf] | deniers holocaust iran | Holocaust_denial |
| 924. | gathering | 50: [10, inf] | gathering 's russian | Intelligence_agencies_of_Russia |
| 925. | environmental | 50: [11, inf] | environmental russia 's | Environmental_issues_in_Russia |
| 926. | rap | 50: [12, inf] | rap cuban cuba | Afro-Cubans |
| 927. | serial | 51: [13, inf] | serial police pakistan | Javed_Iqbal_(serial_killer) |
| 928. | stephens | 51: [10, inf] | stephens arrested serial | Stephen_Port |
| 929. | setback | 51: [11, inf] | setback 's government | Setback_(land_use) |
| 930. | jail | 51: [10, inf] | jail 's mr. | Get_Out_of_Jail_Free_card |
| 931. | marine | 51: [11, inf] | marine iraq marines | United_States_Marine_Corps |
| 932. | sentence | 51: [17, inf] | sentence 's court | Suspended_sentence |
| 933. | transitional | 51: [11, inf] | transitional somalia government | Transitional_federal_government_of_Somalia |
| 934. | image | 52: [11, inf] | image 's party | Republican_Party_(United_States) |
| 935. | iranians | 52: [14, inf] | iranians iraq iran | Iran–Iraq_relations |
| 936. | station | 52: [12, inf] | station police 's | Police_station |
| 937. | area | 52: [10, inf] | area 's iraq | Iraq |
| 938. | strong | 52: [12, inf] | strong 's iraq | Iraq_War |
| 939. | gazprom | 52: [16, inf] | gazprom 's gas | Gazprom |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | 's | 1: [26, inf] | 's iraq world | Iraq |
| 2. | us | 1: [12, inf] | us iraq 's | 2003_invasion_of_Iraq |
| 3. | sharon | 1: [12, inf] | sharon 's surgery | Sharon_Osbourne |
| 4. | iran | 5: [10, 10.0], 15: [13, inf], 17: [10, 5.0] | iran nuclear 's | Nuclear_program_of_Iran |
| 5. | saddam | 52: [15, inf] | saddam trial judge | Trial_of_Saddam_Hussein |
