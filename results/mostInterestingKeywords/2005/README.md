# Keywords with the highest 'interestingness' in 2005

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
| 1. | north | 1: [10, 5.0], 17: [15, 5.0], 27: [15, 15.0], 37: [49, inf] | north korea 's | North_Korea |
| 2. | including | 1: [10, inf], 38: [11, 5.5] | including 's world | The_World's_Billionaires |
| 3. | region | 1: [15, 7.5], 4: [12, 12.0], 22: [10, inf], 50: [15, inf] | region 's world | Region |
| 4. | families | 1: [11, inf] | families 's two | Two_Is_a_Family |
| 5. | family | 1: [15, inf], 36: [12, 6.0] | family 's police | United_States_Capitol_Police |
| 6. | photos | 1: [26, 13.0], 27: [11, 5.5], 44: [12, inf] | photos 's map | Google_Maps |
| 7. | abbas | 1: [28, 7.0], 13: [16, inf], 21: [19, inf] | abbas palestinian israel | Mahmoud_Abbas |
| 8. | fire | 1: [12, 6.0], 7: [12, inf], 10: [10, 5.0], 43: [11, 5.5] | fire gaza israeli | 2014_Gaza_War |
| 9. | tsunami | 1: [70, 8.75], 13: [10, inf] | tsunami 's aid | 2004_Indian_Ocean_earthquake_and_tsunami |
| 10. | south | 1: [24, inf] | south 's africa | South_Africa |
| 11. | two | 1: [16, inf] | two 's world | Two_Worlds_II |
| 12. | make | 1: [11, inf], 35: [16, 5.33] | make 's would | Would? |
| 13. | economy | 1: [10, inf] | economy 's china | Economy_of_China |
| 14. | sri | 1: [13, 6.5], 34: [10, 10.0], 46: [16, inf] | sri lanka 's | Sri_Lanka |
| 15. | aceh | 1: [13, inf], 28: [13, 6.5] | aceh indonesia tsunami | Aceh |
| 16. | around | 1: [10, 10.0], 16: [10, 5.0], 18: [10, inf], 26: [12, 6.0] | around 's world | Around_the_World_in_Eighty_Days |
| 17. | struggle | 1: [11, inf] | struggle 's political | Struggle_session |
| 18. | basque | 1: [12, inf], 5: [13, inf] | basque spain eta | ETA_(separatist_group) |
| 19. | spain | 1: [11, 11.0], 5: [11, inf], 10: [14, 7.0], 39: [11, 5.5], 44: [20, 20.0] | spain 's europe | Spain |
| 20. | province | 1: [10, inf], 26: [10, 10.0], 31: [18, 6.0], 33: [10, 5.0], 35: [20, inf] | province 's killed | Islamic_State_of_Iraq_and_the_Levant_–_Khorasan_Province |
| 21. | try | 1: [11, inf], 28: [10, 10.0] | try 's israel | Israel |
| 22. | bush | 1: [10, inf], 34: [11, 11.0] | bush 's president | George_H._W._Bush |
| 23. | official | 1: [12, inf], 30: [19, 6.33] | official 's police | Colt_Official_Police |
| 24. | million | 1: [16, inf], 11: [18, 6.0], 17: [18, 9.0], 37: [11, 5.5] | million 's world | Mega_Millions |
| 25. | state | 1: [10, inf], 30: [19, 6.33], 33: [20, 5.0], 35: [21, 5.25] | state 's government | State_governments_of_the_United_States |
| 26. | cuba | 1: [13, inf] | cuba 's guantánamo | Guantánamo_Bay |
| 27. | jewish | 1: [14, inf], 16: [12, 6.0], 26: [18, 6.0], 29: [10, 10.0], 31: [19, inf] | jewish gaza israeli | 2014_Gaza_War |
| 28. | french | 1: [11, inf], 7: [11, 5.5], 15: [12, 12.0], 24: [30, 5.0], 35: [11, 5.5], 38: [10, 10.0], 45: [48, 12.0] | french france 's | France |
| 29. | children | 1: [22, inf], 22: [17, 5.67], 30: [12, 6.0], 38: [14, 7.0] | children 's world | Children_of_the_World |
| 30. | report | 1: [10, 10.0], 9: [17, inf], 38: [21, 7.0] | report 's united | U.S._News_&_World_Report |
| 31. | relations | 1: [11, inf] | relations 's china | China–United_States_relations |
| 32. | solidarity | 1: [10, inf] | solidarity 's would | Solidarity |
| 33. | aids | 1: [10, inf], 18: [12, 6.0], 47: [12, inf] | aids 's africa | HIV/AIDS_in_Africa |
| 34. | arafat | 1: [18, inf], 8: [14, inf], 36: [19, inf] | arafat palestinian abbas | Mahmoud_Abbas |
| 35. | lost | 1: [11, inf] | lost 's people | The_Lost_People |
| 36. | mandela | 1: [13, inf] | mandela south africa | Zindzi_Mandela |
| 37. | prison | 2: [17, inf], 18: [10, 10.0] | prison years 's | Prison |
| 38. | flight | 2: [10, inf], 31: [10, inf] | flight 's world | TWA_Flight_800 |
| 39. | corruption | 2: [13, inf], 12: [11, inf], 36: [17, 17.0] | corruption 's president | President_of_the_United_States |
| 40. | members | 2: [13, inf], 45: [10, 5.0] | members 's government | Federal_government_of_the_United_States |
| 41. | talks | 2: [13, inf], 4: [17, 8.5], 19: [15, 5.0], 30: [33, 6.6], 37: [40, 5.0], 49: [25, 8.33] | talks 's nuclear | Six-party_talks |
| 42. | nazi | 2: [10, inf], 4: [12, inf] | nazi 's world | Nazi_Germany |
| 43. | visit | 2: [12, 6.0], 13: [17, inf], 35: [11, 5.5], 52: [10, 5.0] | visit 's china | Richard_Nixon's_1972_visit_to_China |
| 44. | cow | 2: [10, inf] | cow mad disease | Bovine_spongiform_encephalopathy |
| 45. | congressional | 2: [10, inf] | congressional 's president | President_pro_tempore_of_the_United_States_Senate |
| 46. | prince | 2: [10, inf], 14: [29, 14.5] | prince 's monaco | Albert_II,_Prince_of_Monaco |
| 47. | titan | 2: [15, inf] | titan 's moon | Titan_(moon) |
| 48. | zhao | 3: [18, 9.0], 35: [10, inf] | zhao chinese times | Zhao_Ziyang |
| 49. | funeral | 3: [11, inf], 14: [66, inf] | funeral 's pope | Funeral_of_Pope_John_Paul_II |
| 50. | car | 3: [11, inf], 17: [11, 5.5], 28: [16, 16.0] | car bomb 's | Car_bomb |
| 51. | abuse | 3: [13, 13.0], 16: [14, inf], 39: [11, 5.5] | abuse 's report | Abuse_Reporting_Format |
| 52. | autonomy | 4: [13, inf] | autonomy 's government | Autonomy |
| 53. | georgia | 4: [15, inf] | georgia 's europe | Georgia_(U.S._state) |
| 54. | pentagon | 4: [10, inf], 31: [13, inf] | pentagon iraq american | The_Pentagon |
| 55. | general | 4: [15, inf] | general 's united | United_States_Attorney_General |
| 56. | auschwitz | 4: [13, inf] | auschwitz camp death | Auschwitz_concentration_camp |
| 57. | davos | 4: [11, inf] | davos atomic world | DNA_digital_data_storage |
| 58. | church | 5: [14, inf], 45: [20, 6.67] | church pope 's | Pope_of_the_Coptic_Orthodox_Church_of_Alexandria |
| 59. | parliament | 5: [13, inf], 22: [12, 6.0] | parliament 's government | Government_of_the_United_Kingdom |
| 60. | ireland | 5: [15, inf] | ireland northern irish | Northern_Ireland |
| 61. | king | 5: [10, 5.0], 27: [14, inf], 31: [31, inf], 35: [12, 6.0] | king 's nepal | King_of_Nepal |
| 62. | emergency | 5: [10, 10.0], 45: [14, inf] | emergency 's state | State_of_emergency |
| 63. | greets | 6: [10, inf] | greets pope 's | Pope_Francis |
| 64. | togo | 6: [12, 12.0], 17: [16, inf] | togo 's gnassingbe | Faure_Gnassingbé |
| 65. | investigation | 6: [10, 5.0], 32: [10, inf] | investigation 's police | Police_Bureau_of_Investigation |
| 66. | suspects | 6: [11, 5.5], 28: [22, inf], 44: [10, 5.0] | suspects 's police | The_Usual_Suspects |
| 67. | sudan | 6: [11, 11.0], 31: [39, 19.5], 45: [11, inf] | sudan darfur 's | War_in_Darfur |
| 68. | kurds | 6: [11, inf] | kurds kurdish iraqi | Kurdish_population |
| 69. | darfur | 6: [13, 6.5], 45: [14, inf] | darfur sudan 's | War_in_Darfur |
| 70. | quebec | 6: [14, inf], 31: [11, inf] | quebec party canada | Quebec_Liberal_Party |
| 71. | wednesday | 6: [13, inf], 21: [15, 5.0] | wednesday 's president | President_of_the_United_States |
| 72. | rape | 6: [14, inf], 26: [13, 13.0] | rape 's court | Mahmudiyah_rape_and_killings |
| 73. | charles | 6: [11, inf], 14: [19, inf] | charles police 's | Charles_Ramsey |
| 74. | japan | 6: [10, 5.0], 31: [14, inf] | japan 's china | China–Japan_relations |
| 75. | saudi | 6: [12, 12.0], 9: [10, inf], 31: [23, inf] | saudi arabia 's | Saudi_Arabia |
| 76. | claim | 7: [10, inf], 45: [11, 5.5] | claim 's police | Police |
| 77. | policy | 7: [13, inf], 18: [10, 10.0] | policy 's government | Public_policy |
| 78. | administration | 7: [10, inf], 21: [16, 5.33], 23: [11, 5.5] | administration 's bush | Presidency_of_George_W._Bush |
| 79. | mosque | 7: [10, inf] | mosque 's attacks | Christchurch_mosque_shootings |
| 80. | monday | 7: [20, inf], 17: [11, inf], 23: [17, 5.67], 34: [19, 9.5], 36: [10, 5.0], 44: [13, 13.0], 46: [10, 5.0] | monday 's mr. | Plough_Monday |
| 81. | oil | 7: [16, 8.0], 19: [10, 5.0], 35: [18, inf], 40: [15, 15.0], 47: [20, 6.67] | oil 's iraq | Oil_reserves_in_Iraq |
| 82. | iran | 7: [11, 11.0], 19: [13, 6.5], 43: [15, inf] | iran nuclear 's | Nuclear_program_of_Iran |
| 83. | terrorist | 7: [11, inf], 27: [11, 5.5], 39: [17, 8.5] | terrorist 's attacks | September_11_attacks |
| 84. | hariri | 7: [16, inf], 22: [13, inf], 25: [13, inf], 35: [12, 12.0] | hariri 's lebanon | Rafic_Hariri |
| 85. | lebanon | 7: [30, inf], 9: [26, 5.2], 50: [11, inf] | lebanon 's syria | Mandate_for_Syria_and_the_Lebanon |
| 86. | hezbollah | 7: [12, inf], 10: [21, 10.5] | hezbollah lebanese lebanon | 2006_Lebanon_War |
| 87. | raids | 7: [10, inf] | raids police 's | Police_raid |
| 88. | canada | 8: [11, inf], 26: [15, inf], 31: [11, 11.0], 35: [11, 5.5], 43: [11, 5.5] | canada 's canadian | Canadians |
| 89. | gaymard | 8: [11, inf] | gaymard apartment finance | Hervé_Gaymard |
| 90. | apartment | 8: [12, inf] | apartment 's french | Penthouse_apartment |
| 91. | pledges | 8: [10, inf] | pledges 's aid | Aid |
| 92. | palestinians | 8: [18, 6.0], 11: [12, inf], 21: [18, 9.0] | palestinians israel palestinian | Israeli–Palestinian_conflict |
| 93. | barrier | 8: [10, inf] | barrier 's israel | Israeli_West_Bank_barrier |
| 94. | home | 8: [11, inf] | home 's britain | British_Home_Championship |
| 95. | document | 9: [12, inf] | document 's constitution | Constitution |
| 96. | syria | 9: [25, 6.25], 17: [16, inf], 21: [11, 5.5], 29: [10, inf], 49: [10, 5.0] | syria 's lebanon | Mandate_for_Syria_and_the_Lebanon |
| 97. | hussein | 9: [15, 7.5], 15: [14, inf], 19: [12, 6.0], 24: [13, 13.0], 42: [19, 9.5] | hussein 's iraq | Human_rights_in_Saddam_Hussein's_Iraq |
| 98. | hong | 9: [14, inf], 14: [10, inf], 22: [12, 12.0], 38: [17, inf], 45: [10, inf] | hong kong 's | Hong_Kong |
| 99. | kong | 9: [14, inf], 14: [10, inf], 22: [12, 12.0], 38: [17, inf], 45: [10, inf] | kong hong 's | Hong_Kong |
| 100. | abortion | 9: [10, inf] | abortion 's women | Abortion_in_India |
| 101. | journalist | 9: [13, 13.0], 22: [14, inf], 24: [12, 12.0], 31: [13, 6.5], 40: [10, 10.0] | journalist 's killed | List_of_journalists_killed_in_Europe |
| 102. | shooting | 10: [12, inf] | shooting police israeli | Stoneman_Douglas_High_School_shooting |
| 103. | system | 10: [11, inf], 19: [14, 7.0] | system 's government | List_of_countries_by_system_of_government |
| 104. | moldova | 10: [11, inf] | moldova russia communist | Party_of_Communists_of_the_Republic_of_Moldova |
| 105. | russian | 10: [12, inf], 46: [11, inf] | russian russia 's | Russia |
| 106. | dominican | 10: [10, inf] | dominican prison home | Dominican_Republic |
| 107. | sony | 10: [16, inf] | sony 's company | Sony |
| 108. | next | 10: [10, inf] | next 's party | PartyNextDoor |
| 109. | company | 10: [11, 5.5], 49: [10, inf] | company 's oil | Shell_Oil_Company |
| 110. | kosovo | 10: [10, inf] | kosovo 's united | United_Nations_Interim_Administration_Mission_in_Kosovo |
| 111. | mesa | 10: [10, inf] | mesa bolivia president | Carlos_Mesa |
| 112. | ira | 10: [11, inf], 14: [11, inf], 30: [11, inf] | ira irish ireland | Irish_Republican_Army |
| 113. | chechen | 10: [15, inf] | chechen russia russian | Chechen–Russian_conflict |
| 114. | airport | 11: [10, inf], 31: [14, 14.0], 36: [12, 12.0] | airport 's plane | Gordon_Ramsay_Plane_Food |
| 115. | korea | 11: [19, inf], 30: [35, 8.75], 37: [42, 10.5], 49: [15, 15.0] | korea north nuclear | North_Korea_and_weapons_of_mass_destruction |
| 116. | rice | 11: [15, inf], 16: [10, inf], 19: [10, 5.0], 24: [11, 11.0], 41: [20, inf], 45: [10, 5.0], 49: [21, 10.5] | rice state secretary | Condoleezza_Rice |
| 117. | canadian | 11: [10, 10.0], 37: [13, inf] | canadian canada 's | Canadians |
| 118. | budget | 12: [10, inf], 48: [12, 6.0] | budget 's sharon | Sharon_Pratt |
| 119. | pakistani | 12: [11, inf], 44: [16, inf] | pakistani pakistan 's | Pakistanis |
| 120. | khan | 12: [10, inf], 28: [11, 5.5] | khan london 's | Sadiq_Khan |
| 121. | week | 12: [16, inf] | week 's last | Last_Week_Tonight_with_John_Oliver |
| 122. | program | 12: [14, inf], 35: [11, inf], 41: [15, 5.0] | program 's nuclear | Nuclear_program_of_Iran |
| 123. | chechnya | 12: [11, 11.0], 50: [12, inf] | chechnya russia 's | Chechnya |
| 124. | commission | 12: [10, 5.0], 25: [12, inf] | commission 's government | City_commission_government |
| 125. | oil-for-food | 12: [10, inf], 36: [11, inf] | oil-for-food program united | Oil-for-Food_Programme |
| 126. | trade | 12: [10, inf], 23: [10, 5.0], 40: [14, inf] | trade 's china | China–United_States_trade_war |
| 127. | whether | 12: [10, inf], 25: [11, 11.0], 30: [17, 17.0] | whether 's government | Federal_government_of_the_United_States |
| 128. | rebels | 13: [10, inf], 15: [12, 6.0] | rebels 's government | List_of_Star_Wars_Rebels_characters |
| 129. | parties | 13: [10, inf], 38: [10, 10.0], 43: [19, 19.0] | parties 's government | Federal_government_of_the_United_States |
| 130. | known | 13: [11, inf], 45: [11, 5.5] | known 's years | There_are_known_knowns |
| 131. | death | 13: [45, 6.43], 16: [10, 10.0], 33: [19, 9.5], 40: [12, inf], 48: [10, 10.0] | death 's world | Death_to_the_World |
| 132. | festival | 13: [10, inf] | festival film 's | Film_festival |
| 133. | journalists | 13: [12, inf] | journalists 's government | List_of_journalists_killed_in_Europe |
| 134. | near | 13: [10, 5.0], 22: [18, inf], 35: [18, 18.0], 44: [20, 5.0] | near 's two | Near-Earth_object |
| 135. | described | 13: [10, inf] | described 's two | Two-hybrid_screening |
| 136. | nias | 13: [10, inf] | nias quake earthquake | Nias |
| 137. | signs | 13: [11, inf] | signs 's israel | Israel |
| 138. | great | 13: [10, inf] | great 's pope | Pope_Leo_I |
| 139. | vatican | 13: [17, 5.67], 30: [14, inf] | vatican pope 's | Pope_John_Paul_I_conspiracy_theories |
| 140. | resignation | 13: [12, inf], 23: [11, 5.5] | resignation 's president | Letter_of_resignation |
| 141. | mr. | 13: [10, 10.0], 15: [16, inf], 30: [34, 8.5] | mr. 's president | Mr._President_(title) |
| 142. | heart | 13: [10, inf] | heart 's pope | Sacred_Heart |
| 143. | rwanda | 13: [10, inf] | rwanda genocide rwandan | Rwandan_genocide |
| 144. | pray | 13: [10, inf] | pray 's pope | Rosary |
| 145. | krakow | 13: [22, inf] | krakow 's pope | Kraków_John_Paul_II_International_Airport |
| 146. | beyond | 13: [20, inf] | beyond 's pope | Pope |
| 147. | prayers | 13: [23, inf] | prayers 's pope | Prayer_to_Saint_Michael |
| 148. | tributes | 13: [20, inf] | tributes 's pope | Smoking_Popes_Tribute |
| 149. | awe | 13: [20, inf] | awe 's pope | Pope_Benedict_XVI |
| 150. | poland | 13: [11, inf], 30: [13, inf] | poland 's pope | Pope_John_Paul_II |
| 151. | cardinal | 13: [10, inf] | cardinal pope 's | Pope_Francis |
| 152. | kashmir | 14: [11, inf] | kashmir pakistan india | 2014_India–Pakistan_floods |
| 153. | bus | 14: [13, inf], 27: [21, inf], 49: [11, inf] | bus london police | List_of_bus_routes_in_London |
| 154. | divided | 14: [12, inf] | divided 's kashmir | List_of_districts_of_Jammu_and_Kashmir |
| 155. | legal | 14: [10, inf], 17: [10, 10.0], 35: [10, 5.0] | legal 's court | Court_dress |
| 156. | wedding | 14: [16, inf] | wedding charles 's | Wedding_of_Prince_Charles_and_Lady_Diana_Spencer |
| 157. | blair | 14: [11, inf], 22: [16, 16.0], 48: [11, 5.5] | blair 's prime | Tony_Blair |
| 158. | camilla | 14: [13, inf] | camilla charles wedding | Wedding_of_Prince_Charles_and_Camilla_Parker_Bowles |
| 159. | parker | 14: [11, inf] | parker charles camilla | Wedding_of_Prince_Charles_and_Camilla_Parker_Bowles |
| 160. | bowles | 14: [11, inf] | bowles charles camilla | Wedding_of_Prince_Charles_and_Camilla_Parker_Bowles |
| 161. | bolton | 15: [18, 6.0], 30: [10, inf] | bolton 's senate | John_Bolton |
| 162. | soldiers | 15: [10, 10.0], 38: [16, inf], 48: [13, 6.5] | soldiers military 's | Women_in_the_military |
| 163. | constitution | 15: [12, inf], 21: [21, 7.0], 27: [15, inf] | constitution 's iraq | Constitution_of_Iraq |
| 164. | rumsfeld | 15: [11, inf], 41: [11, 11.0] | rumsfeld defense secretary | Donald_Rumsfeld |
| 165. | `` | 15: [12, inf] | `` 's mr. | Toyota_MR2 |
| 166. | pledge | 15: [10, inf] | pledge 's world | The_Giving_Pledge |
| 167. | support | 16: [11, 5.5], 47: [10, inf], 51: [13, 13.0] | support 's government | Federal_government_of_the_United_States |
| 168. | congress | 16: [15, 7.5], 22: [17, inf], 25: [10, 10.0], 32: [15, 5.0] | congress 's president | List_of_presidents_of_the_Indian_National_Congress |
| 169. | gutierrez | 16: [13, inf] | gutierrez ecuador 's | Lucio_Gutiérrez |
| 170. | gen | 16: [12, inf] | gen 's annan | Kofi_Annan |
| 171. | federal | 16: [12, 12.0], 30: [11, inf] | federal 's mexico | Mexico_City |
| 172. | delay | 16: [24, inf], 19: [13, inf] | delay 's gaza | Gaza_Strip |
| 173. | film | 16: [12, inf] | film 's police | Police_Academy_(film) |
| 174. | might | 16: [13, inf], 30: [11, 11.0] | might 's government | They_Might_Be_Giants |
| 175. | roman | 16: [12, 6.0], 45: [10, inf] | roman pope 's | Pope |
| 176. | obrador | 16: [14, inf] | obrador mexico mayor | Andrés_Manuel_López_Obrador |
| 177. | presidential | 16: [10, inf], 34: [11, 5.5] | presidential 's election | United_States_presidential_election |
| 178. | benedict | 16: [32, inf] | benedict pope xvi | Resignation_of_Pope_Benedict_XVI |
| 179. | xvi | 16: [29, inf] | xvi pope benedict | Resignation_of_Pope_Benedict_XVI |
| 180. | wartime | 16: [12, inf] | wartime 's japan | Economic_history_of_Japan |
| 181. | social | 17: [17, inf] | social 's party | Social_Liberal_Party_(Brazil) |
| 182. | syrian | 17: [10, inf], 22: [20, inf], 41: [16, inf] | syrian lebanon 's | Syrian_occupation_of_Lebanon |
| 183. | tuesday | 17: [18, 18.0], 26: [28, 7.0], 31: [25, inf], 33: [17, 5.67] | tuesday 's mr. | Tuesday_Weld |
| 184. | wounded | 17: [12, inf], 35: [10, inf], 46: [11, 11.0] | wounded killed least | List_of_mass_shootings_in_the_United_States_in_2020 |
| 185. | driver | 17: [20, inf] | driver killed 's | Baby_Driver |
| 186. | croatia | 17: [10, inf] | croatia crimes union | 2013_enlargement_of_the_European_Union |
| 187. | anthem | 17: [10, inf] | anthem `` teachers | Kimigayo |
| 188. | member | 17: [10, 10.0], 35: [10, inf] | member 's union | Member_state_of_the_European_Union |
| 189. | gen. | 17: [14, inf] | gen. 's military | Military_coups_in_Pakistan |
| 190. | chisale | 17: [10, inf] | chisale lions mr. | EMPTY MATCHING |
| 191. | northern | 18: [16, 5.33], 33: [16, inf] | northern 's police | Police_Service_of_Northern_Ireland |
| 192. | kills | 18: [12, inf], 33: [16, 8.0] | kills bomb suicide | Suicide_attack |
| 193. | old | 18: [12, inf], 39: [10, 10.0] | old 's years | 38_Years_Old |
| 194. | child | 18: [11, inf] | child 's children | Child_labour |
| 195. | labor | 18: [17, inf] | labor 's party | Minnesota_Democratic–Farmer–Labor_Party |
| 196. | fatah | 18: [10, inf], 50: [18, inf] | fatah palestinian elections | Next_Palestinian_general_election |
| 197. | without | 19: [14, inf] | without 's government | Federal_government_of_the_United_States |
| 198. | trial | 19: [16, inf], 35: [10, 10.0], 38: [13, 13.0], 42: [26, 13.0] | trial 's court | Trial_court |
| 199. | union | 19: [16, 5.33], 35: [10, inf], 37: [24, inf], 46: [17, 17.0] | union european 's | European_Union |
| 200. | permanent | 19: [10, inf] | permanent 's united | Green_card |
| 201. | crimes | 19: [15, inf], 23: [11, 11.0] | crimes 's tribunal | International_Military_Tribunal_for_the_Far_East |
| 202. | run | 19: [10, inf], 30: [13, 6.5] | run 's president | President_of_the_United_States |
| 203. | council | 19: [22, 7.33], 36: [11, 5.5], 38: [20, inf] | council 's security | United_Nations_Security_Council |
| 204. | lower | 19: [10, 10.0], 51: [13, inf] | lower 's house | Lower_house |
| 205. | uzbek | 19: [10, inf], 46: [10, inf] | uzbek uzbekistan crackdown | Education_in_Uzbekistan |
| 206. | treaty | 19: [14, inf] | treaty 's nuclear | Treaty_on_the_Non-Proliferation_of_Nuclear_Weapons |
| 207. | raise | 20: [13, inf] | raise 's government | Federal_government_of_the_United_States |
| 208. | verdict | 20: [11, inf] | verdict 's mr. | After_the_Verdict |
| 209. | companies | 20: [10, inf], 22: [12, 6.0], 43: [15, inf] | companies 's oil | Seven_Sisters_(oil_companies) |
| 210. | truce | 20: [10, inf] | truce palestinian israel | Gaza_War_(2008–2009) |
| 211. | bring | 21: [10, inf] | bring 's party | Democratic_Party_(United_States) |
| 212. | shrine | 21: [21, 10.5], 39: [10, inf], 42: [12, inf] | shrine 's japan | Yasukuni_Shrine |
| 213. | sectarian | 21: [10, inf] | sectarian iraq 's | Iraqi_Civil_War_(2006–2008) |
| 214. | nearly | 21: [10, inf] | nearly 's government | Government_of_India |
| 215. | chirac | 21: [18, 9.0], 35: [10, inf] | chirac france french | Jacques_Chirac |
| 216. | site | 21: [15, inf] | site 's web | Website |
| 217. | short | 21: [10, inf] | short 's vote | Voting |
| 218. | i.r.a | 21: [11, inf], 30: [12, inf] | i.r.a irish ireland | Ireland |
| 219. | paramilitary | 21: [10, inf] | paramilitary 's colombia | Right-wing_paramilitarism_in_Colombia |
| 220. | right | 21: [10, inf] | right 's nuclear | Nuclear_program_of_Iran |
| 221. | fertility | 22: [10, inf] | fertility law pope | 2005_Italian_fertility_laws_referendum |
| 222. | newspaper | 22: [14, inf], 48: [10, 10.0] | newspaper 's world | List_of_newspapers_by_circulation |
| 223. | hamas | 22: [11, 5.5], 50: [10, inf] | hamas palestinian gaza | Hamas |
| 224. | bomber | 22: [10, 5.0], 24: [14, inf], 28: [23, inf], 49: [14, 7.0] | bomber suicide police | Female_suicide_bomber |
| 225. | food | 22: [12, inf], 38: [18, 6.0] | food 's aid | Aid |
| 226. | charter | 22: [10, inf] | charter 's constitution | Canadian_Charter_of_Rights_and_Freedoms |
| 227. | missile | 22: [11, inf] | missile israel 's | Arrow_(Israeli_missile) |
| 228. | zimbabwe | 22: [11, 5.5], 29: [16, inf], 35: [15, inf] | zimbabwe 's mugabe | Robert_Mugabe |
| 229. | missiles | 22: [12, inf] | missiles 's gaza | 2014_Gaza_War |
| 230. | video | 22: [10, inf] | video 's iraq | July_12,_2007,_Baghdad_airstrike |
| 231. | scud | 22: [12, inf] | scud syria missiles | Scud_missile |
| 232. | kassir | 22: [10, inf] | kassir lebanese syrian | Samir_Kassir |
| 233. | hindu | 23: [18, inf] | hindu india party | Hindu_Mahasabha |
| 234. | mortar | 23: [13, inf] | mortar israeli gaza | 2014_Gaza_War |
| 235. | senate | 23: [14, inf], 38: [10, 10.0] | senate bolton 's | John_Bolton |
| 236. | advani | 23: [10, inf] | advani hindu party | L._K._Advani |
| 237. | debt | 23: [10, inf] | debt world 's | History_of_the_United_States_public_debt |
| 238. | questioned | 24: [10, inf] | questioned bombings 's | Atomic_bombings_of_Hiroshima_and_Nagasaki |
| 239. | wine | 24: [10, inf] | wine france europe | French_wine |
| 240. | memo | 24: [15, inf] | memo 's iraq | Bush–Blair_2003_Iraq_memo |
| 241. | executive | 24: [11, inf] | executive 's hong | Chief_Executive_of_Hong_Kong |
| 242. | prosecutor | 24: [12, inf], 38: [12, 6.0] | prosecutor 's mr. | My_Lawyer,_Mr._Jo |
| 243. | strike | 25: [11, inf], 28: [11, 5.5], 47: [10, inf] | strike 's government | UK_miners'_strike_(1984–85) |
| 244. | bombs | 25: [12, inf], 27: [24, 8.0] | bombs police london | List_of_terrorist_incidents_in_London |
| 245. | fraud | 25: [14, inf] | fraud 's election | Republican_reactions_to_Donald_Trump's_claims_of_2020_election_fraud |
| 246. | wines | 25: [11, inf], 35: [12, inf] | wines africa 's | South_African_wine |
| 247. | arab | 25: [11, 11.0], 43: [10, 5.0], 50: [10, inf] | arab 's sunni | Arab_states–Israeli_alliance_against_Iran |
| 248. | muslim | 25: [10, inf], 34: [12, 6.0] | muslim 's police | National_Association_of_Muslim_Police |
| 249. | use | 25: [16, inf], 40: [10, 10.0] | use 's china | Land_use_in_China |
| 250. | six | 25: [11, inf] | six 's police | Six_Pack_(The_Police_box_set) |
| 251. | turkey | 25: [10, 10.0], 28: [14, inf], 35: [16, inf] | turkey 's european | Accession_of_Turkey_to_the_European_Union |
| 252. | crash | 25: [12, inf], 31: [17, inf], 36: [11, inf] | crash plane 's | Lynyrd_Skynyrd_plane_crash |
| 253. | plane | 25: [10, inf], 31: [16, inf], 33: [28, 14.0] | plane crash people | Germanwings_Flight_9525 |
| 254. | berlusconi | 25: [10, inf] | berlusconi 's italy | Silvio_Berlusconi |
| 255. | bosnian | 25: [11, inf] | bosnian serb crimes | Bosnian_War |
| 256. | supporters | 26: [10, 5.0], 45: [10, inf] | supporters 's president | Vice_President_of_the_United_States |
| 257. | fusion | 26: [10, inf] | fusion reactor france | Fusion_power |
| 258. | helicopter | 26: [17, inf] | helicopter crash 's | 2020_Calabasas_helicopter_crash |
| 259. | forgery | 26: [11, inf] | forgery mubarak nour | Ayman_Nour |
| 260. | nour | 26: [11, inf] | nour mubarak 's | Ayman_Nour |
| 261. | held | 26: [17, 5.67], 30: [14, inf], 43: [10, 10.0] | held 's world | Held |
| 262. | sovereignty | 26: [14, inf] | sovereignty 's government | Popular_sovereignty |
| 263. | gay | 26: [17, inf] | gay marriage bill | Same-sex_marriage |
| 264. | shiite | 26: [15, inf], 34: [16, 8.0], 43: [10, 5.0] | shiite 's iraq | Faisal_I_of_Iraq |
| 265. | reactor | 26: [10, inf], 37: [13, 13.0] | reactor nuclear north | List_of_nuclear_reactors |
| 266. | operations | 26: [12, inf] | operations military 's | Military_operation_plan |
| 267. | team | 26: [14, inf] | team 's united | United_States_women's_national_soccer_team |
| 268. | protesters | 26: [13, inf], 38: [12, inf] | protesters 's police | George_Floyd_protests |
| 269. | missing | 26: [12, inf] | missing 's people | Missing_People |
| 270. | sunni | 27: [21, inf], 50: [17, inf] | sunni iraq 's | Sons_of_Iraq |
| 271. | diplomat | 27: [22, inf] | diplomat 's iraq | Abduction_of_Russian_diplomats_in_Iraq |
| 272. | threat | 27: [10, inf], 42: [10, 5.0] | threat 's would | Minor_Threat |
| 273. | flu | 27: [11, 5.5], 38: [14, inf] | flu bird china | Avian_influenza |
| 274. | details | 27: [10, inf] | details 's would | The_Detail |
| 275. | republic | 27: [11, inf] | republic 's chechnya | Chechnya |
| 276. | show | 27: [11, 11.0], 51: [11, inf] | show 's would | Would_I_Lie_to_You?_(game_show) |
| 277. | warming | 27: [13, inf] | warming global 's | Climate_change |
| 278. | global | 27: [13, inf] | global 's world | Global_city |
| 279. | london | 27: [59, inf], 38: [19, 19.0] | london police 's | Metropolitan_Police |
| 280. | pinochet | 27: [10, inf], 32: [11, inf] | pinochet chile 's | Augusto_Pinochet |
| 281. | immunity | 27: [10, inf] | immunity pinochet court | Indictment_and_arrest_of_Augusto_Pinochet |
| 282. | subway | 27: [20, inf], 33: [11, 5.5] | subway police london | 1984_New_York_City_Subway_shooting |
| 283. | trains | 27: [13, inf] | trains london police | Metropolitan_Police |
| 284. | sunday | 28: [30, 6.0], 36: [23, 5.75], 45: [11, inf] | sunday 's president | President_of_the_United_States |
| 285. | armed | 28: [12, 12.0], 48: [10, inf] | armed 's palestinian | Palestinian_Security_Services |
| 286. | body | 28: [11, inf] | body 's police | Police_body_camera |
| 287. | number | 28: [13, inf] | number 's iraq | Multi-National_Force_–_Iraq |
| 288. | reserve | 28: [10, inf] | reserve iraq 's | Oil_reserves_in_Iraq |
| 289. | brought | 28: [10, inf] | brought 's president | President_of_the_United_States |
| 290. | silence | 28: [13, inf] | silence 's party | "S"_Is_for_Silence |
| 291. | leeds | 28: [17, inf] | leeds police london | Little_London,_Leeds |
| 292. | tanweer | 28: [10, inf] | tanweer bombers khan | Shehzad_Tanweer |
| 293. | panel | 29: [11, inf], 52: [12, 12.0] | panel 's annan | Kofi_Annan |
| 294. | already | 29: [14, inf], 31: [10, 5.0] | already 's government | Federal_government_of_the_United_States |
| 295. | sheik | 29: [11, inf] | sheik 's sharm | Sharm_El_Sheikh |
| 296. | committee | 29: [10, inf] | committee 's bolton | John_Bolton |
| 297. | korean | 30: [11, inf] | korean north korea | North_Korea–South_Korea_relations |
| 298. | raid | 30: [13, 13.0], 38: [11, inf], 48: [10, inf] | raid police 's | RAID_(French_police_unit) |
| 299. | ambassador | 30: [13, inf] | ambassador bolton 's | John_Bolton |
| 300. | mubarak | 30: [16, inf] | mubarak 's egypt | Hosni_Mubarak |
| 301. | belarus | 30: [13, inf] | belarus 's lukashenko | Alexander_Lukashenko |
| 302. | rome | 30: [12, inf] | rome 's pope | List_of_popes |
| 303. | sudanese | 31: [10, inf] | sudanese sudan darfur | Sudanese_nomadic_conflicts |
| 304. | arabia | 31: [13, inf] | arabia saudi 's | Saudi_Arabia |
| 305. | fahd | 31: [16, inf] | fahd king saudi | Fahd_of_Saudi_Arabia |
| 306. | italian | 31: [11, 5.5], 36: [10, inf] | italian italy 's | Demographics_of_Italy |
| 307. | brother | 31: [10, inf] | brother 's former | Big_Brother_(American_TV_series) |
| 308. | garang | 31: [21, inf] | garang sudan leader | John_Garang |
| 309. | passengers | 31: [10, inf] | passengers police 's | Passenger_57 |
| 310. | marines | 31: [19, inf], 40: [13, inf], 48: [17, inf] | marines iraq american | United_States_Marine_Corps |
| 311. | david | 31: [12, inf] | david 's british | David_Soul |
| 312. | arabs | 31: [16, inf] | arabs sunni 's | Arab_states–Israeli_alliance_against_Iran |
| 313. | jet | 31: [10, inf] | jet 's air | Jet_engine |
| 314. | vehicle | 31: [10, inf] | vehicle bomb 's | Car_bomb |
| 315. | health | 31: [15, 7.5], 43: [16, 8.0], 45: [10, inf] | health 's world | World_Health_Organization |
| 316. | crew | 31: [14, inf] | crew 's crash | Crash_Crew |
| 317. | submarine | 31: [12, inf] | submarine russian 's | List_of_Soviet_and_Russian_submarine_classes |
| 318. | river | 31: [11, inf] | river 's iraq | Iraq |
| 319. | information | 31: [14, inf] | information 's intelligence | Intelligence_assessment |
| 320. | niger | 31: [12, inf] | niger 's world | Niger |
| 321. | soldier | 31: [10, inf] | soldier israeli killed | Timeline_of_the_Israeli–Palestinian_conflict |
| 322. | u.n. | 32: [11, inf] | u.n. united nations | Headquarters_of_the_United_Nations |
| 323. | koizumi | 32: [13, 6.5], 42: [11, 11.0], 44: [10, inf] | koizumi 's japan | Junichiro_Koizumi |
| 324. | sikhs | 32: [10, inf] | sikhs sikh party | Sikhs |
| 325. | cleric | 32: [14, inf], 38: [11, 5.5] | cleric shiite 's | Shia_clergy |
| 326. | indulgences | 32: [14, inf] | indulgences pope young | Pope_Leo_X |
| 327. | militants | 32: [12, 6.0], 48: [11, inf] | militants palestinian gaza | Gaza–Israel_conflict |
| 328. | heathrow | 32: [10, inf] | heathrow british strike | British_Airways |
| 329. | athens | 33: [12, inf] | athens plane crash | List_of_accidents_and_incidents_involving_airliners_by_location |
| 330. | spanish | 33: [10, inf], 51: [11, inf] | spanish spain 's | Spain |
| 331. | sentences | 33: [11, inf] | sentences court years | Suspended_sentence |
| 332. | port | 33: [10, inf] | port 's world | World's_busiest_ports |
| 333. | synagogue | 33: [13, inf] | synagogue gaza israeli | Israeli_disengagement_from_Gaza |
| 334. | synagogues | 33: [10, inf] | synagogues gaza israeli | Israeli_disengagement_from_Gaza |
| 335. | resume | 34: [10, inf] | resume nuclear iran | Joint_Comprehensive_Plan_of_Action |
| 336. | france | 34: [10, inf] | france 's french | France |
| 337. | hunger | 34: [10, inf] | hunger 's world | Global_Hunger_Index |
| 338. | immigrants | 34: [11, inf], 45: [12, 6.0] | immigrants 's french | Immigration_to_France |
| 339. | knives | 35: [10, inf] | knives africa chisale | EMPTY MATCHING |
| 340. | senators | 35: [10, inf] | senators bolton 's | John_Bolton |
| 341. | public | 35: [18, inf] | public 's government | State_school |
| 342. | ethnic | 35: [11, inf] | ethnic 's government | List_of_ethnic_slurs_by_ethnicity |
| 343. | netanyahu | 35: [17, inf] | netanyahu sharon 's | Benjamin_Netanyahu |
| 344. | michael | 35: [14, inf] | michael 's africa | Out_of_Africa_(film) |
| 345. | stampede | 35: [16, inf] | stampede iraq baghdad | 2005_Al-Aaimmah_bridge_stampede |
| 346. | minibus | 35: [10, inf] | minibus police cliff | Get_Duked! |
| 347. | linked | 36: [15, inf] | linked 's police | United_States_Capitol_Police |
| 348. | indonesian | 36: [12, inf] | indonesian indonesia 's | Indonesia |
| 349. | outside | 36: [13, inf] | outside 's world | World_Outside |
| 350. | weapon | 36: [12, inf] | weapon nuclear `` | Nuclear_weapon |
| 351. | cyprus | 37: [17, inf] | cyprus turkey union | Turkish_invasion_of_Cyprus |
| 352. | britain | 37: [19, inf], 48: [16, 8.0] | britain 's british | Britishness |
| 353. | compromise | 37: [11, inf] | compromise 's mr. | Compromise_of_1790 |
| 354. | hopes | 37: [10, inf], 42: [10, 10.0] | hopes 's political | New_Hope_(Israel) |
| 355. | demand | 37: [11, inf] | demand 's nuclear | Nuclear_program_of_Iran |
| 356. | shiites | 37: [10, inf] | shiites iraq 's | Islamic_State_of_Iraq_and_the_Levant |
| 357. | camp | 38: [10, inf], 41: [11, inf] | camp 's refugee | Refugee_camp |
| 358. | massacre | 38: [10, inf] | massacre srebrenica bosnian | Srebrenica_massacre |
| 359. | british | 38: [32, 10.67], 40: [12, 6.0], 51: [15, inf] | british 's britain | Britishness |
| 360. | bombers | 38: [10, inf] | bombers london police | 7_July_2005_London_bombings |
| 361. | tensions | 38: [10, inf] | tensions 's china | 2020_China–India_skirmishes |
| 362. | khodorkovsky | 38: [17, inf] | khodorkovsky 's oil | Mikhail_Khodorkovsky |
| 363. | protest | 38: [10, inf], 51: [12, 6.0] | protest 's government | Protest |
| 364. | echeverría | 38: [10, inf] | echeverría mr. president | President_of_Mexico |
| 365. | charge | 38: [10, inf] | charge 's mr. | Mr._Mayor |
| 366. | ayatollah | 38: [12, inf] | ayatollah 's iran | Ayatollah |
| 367. | draft | 38: [13, inf], 43: [10, inf] | draft constitution 's | Constitution_of_the_United_States |
| 368. | governing | 38: [12, inf] | governing party 's | Ruling_party |
| 369. | visits | 39: [17, inf] | visits 's japan | Japan |
| 370. | justice | 39: [10, inf] | justice 's government | United_States_Department_of_Justice |
| 371. | hughes | 39: [11, inf] | hughes american 's | Glenn_Hughes_(American_singer) |
| 372. | laws | 39: [10, inf] | laws 's `` | Murphy's_law |
| 373. | algerians | 39: [11, inf] | algerians vote 's | Algerian_War |
| 374. | iranian | 39: [10, 10.0], 43: [14, inf] | iranian iran 's | Demographics_of_Iran |
| 375. | possible | 39: [10, inf] | possible 's government | Kim_Possible |
| 376. | ice | 39: [10, inf] | ice arctic gases | Climate_change_in_the_Arctic |
| 377. | venezuelan | 40: [10, inf] | venezuelan venezuela 's | Crisis_in_Venezuela_during_the_Bolivarian_Revolution |
| 378. | chancellor | 40: [18, 18.0], 47: [13, inf] | chancellor 's germany | Chancellor_of_Germany |
| 379. | nobel | 40: [13, inf] | nobel prize nuclear | 2017_Nobel_Peace_Prize |
| 380. | sanctions | 40: [13, inf] | sanctions 's united | United_States_sanctions |
| 381. | rescue | 41: [10, inf] | rescue 's train | Search_and_rescue |
| 382. | rescuers | 41: [11, inf] | rescuers survivors quake | 2008_Sichuan_earthquake |
| 383. | strain | 41: [10, inf] | strain 's flu | Hong_Kong_flu |
| 384. | virus | 41: [10, inf] | virus birds flu | Avian_influenza |
| 385. | poverty | 41: [12, inf] | poverty africa 's | Poverty_in_Africa |
| 386. | travel | 42: [10, inf] | travel 's palestinian | Palestinian_Authority_passport |
| 387. | coast | 42: [10, inf] | coast 's people | Indigenous_peoples_of_the_Pacific_Northwest_Coast |
| 388. | authority | 42: [10, inf] | authority palestinian 's | Palestinian_National_Authority |
| 389. | results | 42: [11, inf] | results 's election | Attempts_to_overturn_the_2020_United_States_presidential_election |
| 390. | criticism | 42: [10, inf] | criticism 's government | Criticism_of_the_Israeli_government |
| 391. | lawyer | 42: [10, inf] | lawyer 's hussein | Execution_of_Saddam_Hussein |
| 392. | work | 43: [12, inf] | work 's government | Copyright_status_of_works_by_the_federal_government_of_the_United_States |
| 393. | study | 43: [12, inf] | study 's world | Globalization_and_World_Cities_Research_Network |
| 394. | determine | 43: [13, inf] | determine 's world | Darts_world_rankings |
| 395. | leaders | 43: [13, inf] | leaders 's government | List_of_current_heads_of_state_and_government |
| 396. | center | 43: [10, inf] | center 's city | CityCenter |
| 397. | girl | 43: [16, inf] | girl 's -year-old | Destiny's_Child |
| 398. | spread | 44: [11, inf] | spread 's two | Spread_betting |
| 399. | rioting | 44: [14, inf] | rioting france violence | 2005_French_riots |
| 400. | clashes | 44: [10, inf] | clashes 's killed | 2020–21_Ayn_Issa_clashes |
| 401. | unrest | 44: [12, inf] | unrest 's police | Ferguson_unrest |
| 402. | spreads | 44: [13, inf] | spreads 's violence | Violence |
| 403. | suburbs | 44: [15, inf] | suburbs violence paris | Paris |
| 404. | summit | 44: [10, inf] | summit meeting 's | Summit_(meeting) |
| 405. | equatorial | 44: [10, inf] | equatorial guinea coup | 2004_Equatorial_Guinea_coup_d'état_attempt |
| 406. | guinea | 44: [10, inf] | guinea equatorial coup | 2004_Equatorial_Guinea_coup_d'état_attempt |
| 407. | catholic | 45: [15, inf] | catholic pope 's | List_of_popes |
| 408. | chile | 45: [14, inf] | chile pinochet 's | Augusto_Pinochet |
| 409. | curfews | 45: [11, inf] | curfews emergency violence | Violence_and_controversies_during_the_George_Floyd_protests |
| 410. | discrimination | 45: [10, inf] | discrimination french 's | Discrimination |
| 411. | mandate | 45: [12, inf] | mandate 's government | Mandate_for_Palestine |
| 412. | lawyers | 45: [13, inf] | lawyers 's court | Lawyer |
| 413. | jordan | 45: [16, inf] | jordan jordanian attack | Jordan |
| 414. | like | 45: [11, 11.0], 47: [13, inf] | like 's world | In_a_World_Like_This |
| 415. | amman | 45: [12, inf] | amman jordan attacks | 2005_Amman_bombings |
| 416. | priests | 45: [14, inf] | priests church pope | Catholic_Church_sexual_abuse_cases |
| 417. | sexual | 45: [12, inf] | sexual report church | Catholic_Church_sexual_abuse_cases |
| 418. | contract | 46: [10, inf] | contract annan iraq | Kofi_Annan |
| 419. | defeat | 47: [10, inf] | defeat 's party | Democratic_Party_(United_States) |
| 420. | water | 47: [18, inf] | water 's city | New_York_City_water_supply_system |
| 421. | spill | 47: [15, inf] | spill china water | Xingang_Port_oil_spill |
| 422. | alamieyeseigha | 48: [10, inf] | alamieyeseigha nigeria 's | Diepreye_Alamieyeseigha |
| 423. | see | 48: [10, inf] | see 's many | How_Many_Clouds_Can_You_See? |
| 424. | mall | 49: [12, inf] | mall shopping suicide | Westroads_Mall_shooting |
| 425. | lead | 49: [11, inf] | lead 's party | Republican_Party_(United_States) |
| 426. | planned | 50: [11, inf] | planned 's gaza | Israeli_disengagement_from_Gaza |
| 427. | tueni | 50: [10, inf] | tueni car syria | Gebran_Tueni |
| 428. | missionaries | 51: [12, inf] | missionaries north 's | Missionary |
| 429. | uzbekistan | 51: [11, inf] | uzbekistan uzbek crackdown | Education_in_Uzbekistan |
| 430. | karzai | 51: [11, inf] | karzai afghanistan afghan | Politics_of_Afghanistan |
| 431. | tax | 51: [12, inf] | tax 's charges | Poll_tax_(Great_Britain) |
| 432. | navy | 51: [13, inf] | navy 's u.s. | United_States_Navy |
| 433. | h.i.v | 51: [10, inf] | h.i.v 's children | V/H/S |
| 434. | libya | 51: [11, inf] | libya 's nuclear | Libya_and_weapons_of_mass_destruction |
| 435. | schwarzenegger | 52: [10, inf] | schwarzenegger 's stadium | Liebenauer_Stadium |
| 436. | ghana | 52: [12, inf] | ghana 's africans | Ghana |
| 437. | kidnapped | 52: [10, inf] | kidnapped 's baghdad | Foreign_hostages_in_Iraq |
| 438. | hwang | 52: [10, inf] | hwang stem cells | Hwang_Woo-suk |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | press | 1: [13, inf] | press review ... | Press_review |
| 2. | review | 1: [14, inf] | review press ... | Chicago_Review_Press |
| 3. | thailand | 4: [11, inf] | thailand g tsunami | 2004_Indian_Ocean_earthquake_and_tsunami |
| 4. | lebanon | 9: [10, inf] | lebanon syria press | Mandate_for_Syria_and_the_Lebanon |
| 5. | people | 14: [12, inf] | people 's say | What_Will_People_Say |
