# Keywords with the highest 'interestingness' in 2001

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
| 1. | argentine | 2: [10, inf], 44: [10, 5.0], 51: [13, inf] | argentine argentina 's | Argentina |
| 2. | european | 2: [12, inf], 33: [13, 13.0], 35: [13, inf] | european 's union | European_Union |
| 3. | navy | 2: [10, 10.0], 14: [12, inf] | navy plane 's | Doomsday_plane |
| 4. | oil | 2: [14, inf], 4: [18, 9.0], 7: [13, 13.0], 22: [11, inf], 33: [12, inf] | oil 's iraq | Oil_reserves_in_Iraq |
| 5. | bosnian | 2: [20, inf], 27: [14, 14.0] | bosnian serb crimes | Bosnian_War |
| 6. | serb | 2: [19, inf], 31: [12, 6.0] | serb bosnian crimes | Bosnian_War |
| 7. | schroder | 2: [10, 5.0], 21: [10, inf] | schroder germany chancellor | Gerhard_Schröder |
| 8. | mad | 2: [14, inf] | mad cow disease | Bovine_spongiform_encephalopathy |
| 9. | cow | 2: [14, inf], 12: [10, 10.0] | cow mad disease | Bovine_spongiform_encephalopathy |
| 10. | disease | 2: [14, 14.0], 6: [10, 5.0], 34: [10, inf] | disease foot-and-mouth 's | Foot-and-mouth_disease |
| 11. | depleted | 2: [10, inf] | depleted uranium nato | Depleted_uranium |
| 12. | kosovo | 2: [11, inf], 5: [30, 15.0], 23: [12, 6.0], 46: [13, inf] | kosovo nato 's | Kosovo_War |
| 13. | civilians | 2: [11, inf] | civilians 's photo | Civilian_casualties_in_the_war_in_Afghanistan_(2001–present) |
| 14. | turkey | 2: [15, inf], 17: [15, 5.0], 23: [22, 7.33] | turkey 's world | Turkey |
| 15. | lockerbie | 2: [20, inf], 5: [23, inf] | lockerbie trial bombing | Pan_Am_Flight_103 |
| 16. | prosecutor | 2: [10, inf] | prosecutor tribunal 's | International_Criminal_Tribunal_for_Rwanda |
| 17. | plavsic | 2: [12, inf] | plavsic serb bosnian | Biljana_Plavšić |
| 18. | pilot | 2: [10, inf], 14: [12, inf], 17: [17, 5.67] | pilot chinese plane | Hainan_Island_incident |
| 19. | quebec | 2: [10, inf], 16: [10, 5.0] | quebec trade americas | Free_Trade_Area_of_the_Americas |
| 20. | bouchard | 2: [10, inf] | bouchard quebec premier | Lucien_Bouchard |
| 21. | britain | 3: [11, inf], 8: [22, 7.33] | britain 's british | Britishness |
| 22. | airport | 3: [11, inf] | airport 's afghanistan | Kandahar_International_Airport |
| 23. | congo | 3: [30, inf] | congo kabila 's | Laurent-Désiré_Kabila |
| 24. | laurent | 3: [15, inf] | laurent kabila congo | Laurent-Désiré_Kabila |
| 25. | kabila | 3: [34, inf] | kabila congo 's | Joseph_Kabila |
| 26. | shanghai | 3: [10, inf], 42: [25, inf] | shanghai bush china | Jiang_Mianheng |
| 27. | church | 4: [11, inf], 8: [12, inf] | church pope 's | Pope_of_the_Coptic_Orthodox_Church_of_Alexandria |
| 28. | colombia | 4: [16, inf] | colombia 's colombian | Colombians |
| 29. | despite | 4: [11, inf], 23: [13, 6.5], 42: [10, 5.0] | despite 's us | United_States |
| 30. | tanker | 4: [10, inf] | tanker oil galapagos | Galápagos_Islands |
| 31. | galapagos | 4: [10, inf] | galapagos oil tanker | Galápagos_Islands |
| 32. | india | 4: [31, 10.33], 14: [10, inf], 19: [17, 17.0], 23: [10, 5.0] | india 's pakistan | India–Pakistan_relations |
| 33. | blair | 4: [16, 16.0], 8: [18, inf], 14: [14, 14.0], 23: [16, 8.0], 40: [43, 43.0], 51: [11, 11.0] | blair 's prime | Premiership_of_Tony_Blair |
| 34. | media-most | 4: [10, inf] | media-most gusinsky 's | Vladimir_Gusinsky |
| 35. | wahid | 4: [10, inf], 22: [26, inf] | wahid indonesia 's | Abdurrahman_Wahid |
| 36. | politics | 5: [12, 6.0], 30: [10, 5.0], 41: [17, inf] | politics 's party | Political_parties_in_the_United_States |
| 37. | dead | 5: [22, 7.33], 13: [10, inf], 21: [15, 7.5] | dead 's people | Conversations_with_Dead_People |
| 38. | pinochet | 5: [11, inf] | pinochet chile augusto | Lucía_Pinochet |
| 39. | ordered | 5: [14, inf] | ordered 's american | Ordered_field |
| 40. | house | 5: [15, inf], 8: [10, inf] | house 's bush | George_W._Bush |
| 41. | found | 5: [10, inf], 14: [12, 6.0], 27: [12, inf] | found 's world | HTTP_404 |
| 42. | way | 5: [10, 5.0], 14: [10, 5.0], 38: [15, inf], 50: [14, 7.0] | way 's says | Hey,_That's_No_Way_to_Say_Goodbye |
| 43. | mexico | 5: [23, 7.67], 28: [16, 5.33], 31: [13, inf], 43: [11, 5.5] | mexico 's fox | Vicente_Fox |
| 44. | interview | 5: [10, inf], 32: [16, 5.33] | interview 's says | The_Interview |
| 45. | appears | 5: [10, 5.0], 40: [10, inf] | appears 's bush | George_H._W._Bush |
| 46. | decision | 5: [13, 6.5], 38: [11, inf] | decision 's bush | Bush_v._Gore |
| 47. | libyans | 5: [13, inf] | libyans trial lockerbie | Pan_Am_Flight_103 |
| 48. | bombing | 5: [29, inf], 8: [10, inf], 21: [17, 5.67], 30: [12, 12.0], 32: [11, 5.5] | bombing taliban american | Taliban_insurgency |
| 49. | finds | 5: [10, inf], 31: [16, 16.0], 48: [10, 10.0] | finds 's world | Findability |
| 50. | verdict | 5: [30, inf] | verdict trial guilty | Not_proven |
| 51. | guilty | 5: [18, inf] | guilty trial 's | Impeachment_of_Bill_Clinton |
| 52. | goes | 5: [11, inf] | goes 's world | The_Go-Go's |
| 53. | pan | 5: [15, inf] | pan bombing lockerbie | Pan_Am_Flight_103 |
| 54. | plant | 5: [10, inf] | plant 's nuclear | Chernobyl_Nuclear_Power_Plant |
| 55. | legislature | 5: [10, inf] | legislature 's president | President_of_the_United_States |
| 56. | growth | 5: [10, inf] | growth 's economic | Economic_growth |
| 57. | libyan | 5: [16, inf] | libyan lockerbie bombing | Pan_Am_Flight_103 |
| 58. | albanians | 5: [10, inf], 26: [10, 10.0] | albanians macedonia kosovo | Kosovo_Albanians |
| 59. | libya | 5: [18, inf] | libya bombing sanctions | Pan_Am_Flight_103 |
| 60. | democratic | 6: [10, inf], 17: [18, 6.0], 37: [11, inf] | democratic 's party | Democratic_Party_(United_States) |
| 61. | canada | 6: [13, inf], 20: [10, inf] | canada 's world | Canada_in_World_War_II |
| 62. | borders | 6: [12, inf] | borders 's says | Canada–United_States_border |
| 63. | aristide | 6: [11, inf] | aristide haiti opposition | Jean-Bertrand_Aristide |
| 64. | victory | 6: [17, inf], 31: [13, inf] | victory 's party | Victory_Party |
| 65. | unity | 6: [10, inf] | unity 's sharon | 2003_Israeli_legislative_election |
| 66. | coalition | 6: [10, inf], 17: [13, inf] | coalition 's government | Coalition_government |
| 67. | form | 6: [10, inf] | form 's government | List_of_forms_of_government |
| 68. | arsenal | 6: [10, inf] | arsenal 's nuclear | Nuclear_weapons_of_the_United_States |
| 69. | milosevic | 6: [12, inf], 13: [16, inf], 26: [45, 11.25], 31: [12, 12.0], 34: [13, inf] | milosevic tribunal crimes | Trial_of_Slobodan_Milošević |
| 70. | gaza | 7: [10, 5.0], 18: [11, inf], 47: [14, 7.0], 49: [18, 18.0] | gaza israeli palestinian | Gaza_War_(2008–2009) |
| 71. | ukraine | 7: [18, inf], 41: [20, 5.0], 43: [14, 14.0] | ukraine 's kuchma | Leonid_Kuchma |
| 72. | week | 7: [10, 10.0], 18: [10, inf] | week 's last | Last_Week_Tonight_with_John_Oliver |
| 73. | food | 7: [12, inf], 40: [20, 5.0] | food 's taliban | Taliban |
| 74. | torture | 7: [10, inf], 36: [10, inf] | torture 's rights | Torture |
| 75. | general | 7: [12, inf], 17: [11, inf], 44: [10, 5.0] | general 's united | United_States_Attorney_General |
| 76. | human | 7: [10, 5.0], 16: [13, inf], 52: [17, 8.5] | human rights 's | Human_rights |
| 77. | bus | 7: [19, inf] | bus palestinian israeli | Israeli–Palestinian_conflict |
| 78. | zone | 7: [10, inf], 9: [10, 10.0], 11: [14, 7.0] | zone 's kosovo | Kosovo–Serbia_relations |
| 79. | iraqi | 7: [12, inf], 27: [11, inf] | iraqi iraq hussein | Saddam_Hussein |
| 80. | korea | 8: [17, inf], 13: [26, 13.0], 18: [15, inf], 23: [24, inf] | korea north south | North_Korea–South_Korea_relations |
| 81. | keep | 8: [11, inf] | keep 's taliban | Taliban |
| 82. | refugees | 8: [11, 11.0], 17: [18, inf] | refugees 's taliban | Taliban |
| 83. | aid | 8: [16, 5.33], 17: [12, inf], 22: [13, 13.0] | aid 's afghanistan | Phantom_aid_in_Afghanistan |
| 84. | saddam | 8: [10, inf] | saddam iraq hussein | Saddam's_family |
| 85. | hussein | 8: [12, inf], 51: [11, 5.5] | hussein iraq saddam | Saddam's_family |
| 86. | basque | 8: [13, inf], 19: [12, inf], 44: [14, inf] | basque group eta | ETA_(separatist_group) |
| 87. | pope | 8: [10, inf], 18: [16, inf], 25: [11, inf], 38: [15, 7.5], 43: [12, 6.0] | pope paul john | Pope_John_Paul_II |
| 88. | defenses | 8: [13, inf] | defenses missile bush | Missile_defense |
| 89. | arrest | 8: [14, inf], 30: [11, inf] | arrest 's police | Arrest |
| 90. | coca | 8: [10, inf], 11: [12, inf] | coca colombia 's | Coca_production_in_Colombia |
| 91. | orthodox | 8: [11, inf] | orthodox church pope | Pope_of_the_Coptic_Orthodox_Church_of_Alexandria |
| 92. | report | 9: [13, inf], 20: [18, 9.0], 27: [10, 5.0], 36: [14, 14.0] | report 's says | U.S._News_&_World_Report |
| 93. | money | 9: [18, 9.0], 19: [10, 5.0], 39: [14, inf], 45: [16, 5.33] | money 's united | United_States_dollar |
| 94. | citibank | 9: [12, inf] | citibank bank money | Citibank_India |
| 95. | bodies | 9: [11, inf], 31: [10, inf] | bodies 's taliban | Taliban |
| 96. | buffer | 9: [10, inf] | buffer zone kosovo | Insurgency_in_the_Preševo_Valley |
| 97. | department | 9: [10, inf] | department state 's | United_States_Department_of_State |
| 98. | mexican | 9: [11, inf], 14: [12, inf], 31: [14, inf], 36: [15, 15.0] | mexican mexico fox | Mexico |
| 99. | east | 9: [13, inf], 18: [12, inf], 31: [12, 12.0] | east middle 's | Middle_East |
| 100. | private | 10: [10, inf] | private 's government | Government |
| 101. | court | 10: [16, 16.0], 14: [19, inf], 39: [15, 15.0], 44: [17, 8.5], 46: [15, 7.5] | court 's world | International_Court_of_Justice |
| 102. | election | 10: [13, inf], 18: [14, 7.0], 34: [10, 5.0], 44: [10, inf] | election 's party | 2024_United_States_presidential_election |
| 103. | drugs | 10: [14, inf], 13: [26, inf], 16: [11, inf] | drugs aids africa | HIV/AIDS_denialism |
| 104. | trial | 10: [12, 6.0], 14: [26, inf], 20: [18, 6.0], 25: [12, 6.0] | trial 's former | O._J._Simpson_murder_case |
| 105. | companies | 10: [15, 7.5], 13: [10, inf] | companies 's drugs | Pharmaceutical_industry |
| 106. | hungary | 10: [12, inf] | hungary 's european | 2019_European_Parliament_election_in_Hungary |
| 107. | faces | 10: [11, inf], 50: [14, 7.0] | faces 's government | Government_shutdowns_in_the_United_States |
| 108. | school | 10: [14, 7.0], 23: [12, inf], 36: [16, inf], 51: [15, inf] | school 's children | Professional_Children's_School |
| 109. | ruling | 10: [11, inf], 31: [14, 7.0] | ruling 's taliban | Islamic_Emirate_of_Afghanistan |
| 110. | force | 10: [12, 12.0], 25: [14, 7.0], 36: [10, inf] | force 's military | United_States_Armed_Forces |
| 111. | payments | 10: [12, inf] | payments 's united | Global_Payments |
| 112. | macedonia | 10: [12, inf], 23: [12, inf] | macedonia albanian rebels | 2001_insurgency_in_Macedonia |
| 113. | macedonian | 10: [11, inf], 12: [23, 11.5] | macedonian albanian macedonia | Macedonian_front |
| 114. | free | 11: [14, inf], 31: [10, 5.0] | free 's trade | Free_trade |
| 115. | along | 11: [10, 5.0], 52: [11, inf] | along 's border | Migrant_deaths_along_the_Mexico–United_States_border |
| 116. | health | 11: [12, 6.0], 13: [18, inf], 35: [16, 16.0] | health 's world | World_Health_Organization |
| 117. | sales | 11: [16, inf] | sales 's arms | List_of_US_arms_sales_to_Taiwan |
| 118. | iran | 11: [21, 5.25], 18: [10, inf], 23: [11, 5.5] | iran 's afghanistan | Afghanistan–Iran_relations |
| 119. | blockade | 11: [14, inf] | blockade palestinian israeli | Israeli–Palestinian_conflict |
| 120. | kuwait | 11: [12, inf] | kuwait 's iraq | Invasion_of_Kuwait |
| 121. | paris | 11: [11, inf] | paris french 's | Paris |
| 122. | return | 11: [10, inf], 14: [23, inf], 47: [14, 7.0] | return 's photo | Google_Photos |
| 123. | bristol-myers | 11: [12, inf] | bristol-myers africa price | Emcure_Pharmaceuticals |
| 124. | criticism | 11: [11, inf] | criticism 's bush | Public_image_of_George_W._Bush |
| 125. | tunnel | 11: [13, inf], 43: [35, inf], 52: [13, inf] | tunnel france channel | Channel_Tunnel |
| 126. | immigrants | 11: [13, inf], 26: [12, 6.0], 36: [12, inf] | immigrants 's illegal | Illegal_immigration_to_the_United_States |
| 127. | saudi | 11: [14, inf], 22: [12, inf] | saudi arabia 's | Saudi_Arabia |
| 128. | intelligence | 12: [10, inf], 15: [12, 6.0] | intelligence 's us | United_States_Intelligence_Community |
| 129. | issues | 12: [13, 6.5], 28: [10, inf] | issues 's bush | Prescott_Bush |
| 130. | diplomats | 12: [15, inf] | diplomats 's american | Foreign_Service_Officer |
| 131. | leaders | 12: [16, inf] | leaders 's taliban | List_of_Taliban_leaders |
| 132. | ireland | 12: [12, 12.0], 15: [12, inf], 23: [21, 10.5], 31: [10, inf] | ireland northern 's | Northern_Ireland |
| 133. | scholar | 12: [12, inf], 30: [15, 15.0] | scholar chinese china | China |
| 134. | pigs | 12: [12, inf] | pigs disease bay | Pig |
| 135. | castro | 12: [10, inf] | castro 's pres | Fidel_Castro |
| 136. | kurdish | 12: [10, inf] | kurdish britain turkey | Kurds_in_Turkey |
| 137. | effort | 13: [13, 6.5], 31: [11, inf] | effort 's photo | Google_Photos |
| 138. | brazil | 13: [14, 14.0], 18: [14, 7.0], 41: [12, 6.0], 51: [20, inf] | brazil 's world | Brazil_v_Germany_(2014_FIFA_World_Cup) |
| 139. | prices | 13: [20, inf] | prices aids 's | HIV/AIDS |
| 140. | iraq | 13: [20, 20.0], 18: [10, 5.0], 20: [12, inf], 27: [10, 5.0], 35: [11, inf], 47: [11, 5.5] | iraq iraqi 's | Iraqis |
| 141. | toward | 13: [12, inf], 36: [10, 5.0], 45: [12, 12.0] | toward 's bush | George_H._W._Bush |
| 142. | council | 13: [11, inf] | council security 's | United_Nations_Security_Council |
| 143. | belgrade | 13: [12, inf] | belgrade milosevic tribunal | Slobodan_Milošević |
| 144. | chinese | 14: [106, 7.57], 26: [11, inf], 30: [48, 12.0] | chinese china 's | China |
| 145. | spy | 14: [59, 6.56], 26: [10, inf] | spy china chinese | China |
| 146. | surveillance | 14: [10, inf] | surveillance plane china | Surveillance_aircraft |
| 147. | fighter | 14: [29, inf] | fighter plane chinese | Mitsubishi_A6M_Zero |
| 148. | landing | 14: [18, inf] | landing plane china | Hainan_Island_incident |
| 149. | hainan | 14: [21, inf] | hainan plane china | Hainan_Island_incident |
| 150. | crew | 14: [79, inf] | crew china plane | Hainan_Island_incident |
| 151. | aircraft | 14: [18, inf] | aircraft american 's | All_American_(aircraft) |
| 152. | april | 14: [40, inf] | april 's china | China |
| 153. | sunday | 14: [17, inf] | sunday 's bush | Alaskan_Bush_People |
| 154. | collision | 14: [46, inf], 43: [11, 5.5] | collision china chinese | 1990_Guangzhou_Baiyun_airport_collisions |
| 155. | incident | 14: [18, inf] | incident 's china | Hainan_Island_incident |
| 156. | crimes | 14: [21, 5.25], 16: [14, inf], 22: [12, 6.0], 46: [15, 15.0] | crimes tribunal milosevic | Trial_of_Slobodan_Milošević |
| 157. | yugoslavia | 14: [17, 8.5], 23: [10, inf] | yugoslavia milosevic 's | Slobodan_Milošević |
| 158. | colin | 14: [18, 6.0], 26: [15, 5.0], 30: [25, 6.25], 42: [15, 7.5], 46: [10, inf] | colin powell 's | Colin_Powell |
| 159. | powell | 14: [30, 6.0], 26: [31, 5.17], 30: [51, 5.67], 35: [11, inf], 42: [29, 14.5], 46: [21, inf] | powell 's colin | Colin_Powell |
| 160. | delay | 14: [11, inf] | delay 's government | Tom_DeLay |
| 161. | long | 14: [10, inf], 24: [10, 10.0] | long 's says | Say's_law |
| 162. | regret | 14: [10, inf] | regret 's chinese | Chinese_Exclusion_Act |
| 163. | jiang | 14: [11, inf], 32: [27, inf], 42: [11, inf] | jiang china 's | Jiang_Zemin |
| 164. | apology | 14: [19, inf] | apology china chinese | Band_in_China |
| 165. | aides | 14: [13, 13.0], 41: [10, inf] | aides bush 's | George_H._W._Bush |
| 166. | letter | 14: [12, inf] | letter 's bush | Mahmoud_Ahmadinejad's_letter_to_George_W._Bush |
| 167. | network | 14: [12, inf], 25: [10, inf], 38: [18, inf] | network 's laden | Bin_Laden_family |
| 168. | ntv | 14: [16, inf] | ntv 's gazprom | Gazprom-Media |
| 169. | gazprom | 14: [13, inf] | gazprom 's ntv | Gazprom-Media |
| 170. | bhutto | 14: [10, inf] | bhutto pakistan court | Zulfikar_Ali_Bhutto |
| 171. | remains | 15: [10, inf] | remains 's say | The_Remains_of_the_Day |
| 172. | heroes | 15: [14, inf] | heroes 's welcome | Heroes_Welcome_UK |
| 173. | use | 15: [10, inf], 38: [19, 6.33], 44: [13, 13.0] | use 's military | Authorization_for_Use_of_Military_Force_of_2001 |
| 174. | home | 15: [20, 10.0], 21: [11, inf] | home 's photo | Photo_Booth |
| 175. | water | 15: [14, inf], 18: [13, inf] | water 's says | Flint_water_crisis |
| 176. | gusinsky | 16: [19, inf] | gusinsky 's vladimir | Vladimir_Gusinsky |
| 177. | known | 16: [10, inf], 46: [10, 10.0] | known 's say | There_are_known_knowns |
| 178. | calling | 16: [14, inf] | calling 's china | China |
| 179. | withdraw | 16: [10, inf], 35: [10, 10.0] | withdraw 's bush | George_H._W._Bush |
| 180. | lebanon | 16: [14, inf] | lebanon israeli israel | Israeli–Lebanese_conflict |
| 181. | arab | 16: [15, inf], 47: [21, 5.25] | arab 's israeli | Arab–Israeli_conflict |
| 182. | sharon | 16: [15, inf], 25: [13, 6.5] | sharon israeli israel | Ariel_Sharon |
| 183. | japan | 16: [23, 5.75], 37: [30, 7.5], 43: [11, 11.0], 51: [13, inf] | japan 's japanese | Japan |
| 184. | helms | 16: [10, inf] | helms mexico 's | Jesse_Helms |
| 185. | mr. | 16: [23, 7.67], 18: [23, 11.5], 24: [12, inf], 27: [17, inf], 30: [14, 14.0], 46: [14, 7.0] | mr. 's president | Mr._President_(title) |
| 186. | americas | 16: [15, 15.0], 31: [14, inf], 39: [11, inf], 45: [12, 6.0] | americas world briefing | 1211_Avenue_of_the_Americas |
| 187. | industry | 16: [10, inf] | industry 's government | State_ownership |
| 188. | aids | 16: [11, inf], 25: [16, 8.0] | aids africa 's | HIV/AIDS_in_Africa |
| 189. | beirut | 16: [10, inf] | beirut 's chtaura | Chtaura |
| 190. | protest | 17: [10, inf], 40: [10, inf] | protest 's world | Protest |
| 191. | chechnya | 17: [12, inf] | chechnya russian 's | Chechnya |
| 192. | koizumi | 17: [20, 10.0], 30: [15, inf] | koizumi 's japan | Junichiro_Koizumi |
| 193. | communist | 17: [10, inf], 48: [10, 10.0] | communist 's party | Chinese_Communist_Party |
| 194. | agency | 17: [10, inf] | agency 's says | National_Security_Agency |
| 195. | show | 17: [11, inf], 49: [10, 5.0], 51: [13, 6.5] | show 's government | That_'70s_Show |
| 196. | campaign | 17: [11, inf] | campaign 's afghanistan | Afghanistan_Campaign_Medal |
| 197. | cabinet | 17: [10, inf], 22: [11, 11.0], 36: [11, 5.5] | cabinet 's government | Cabinet_(government) |
| 198. | labor | 17: [10, 5.0], 19: [11, inf], 49: [12, inf] | labor 's party | Minnesota_Democratic–Farmer–Labor_Party |
| 199. | missile | 18: [54, 13.5], 46: [13, inf], 50: [25, 8.33] | missile bush 's | 1993_cruise_missile_strikes_on_Iraq |
| 200. | system | 18: [31, inf], 22: [12, 6.0] | system 's missile | S-500_missile_system |
| 201. | indonesia | 18: [14, 7.0], 22: [23, inf], 30: [33, 8.25] | indonesia 's wahid | Abdurrahman_Wahid |
| 202. | change | 18: [14, 7.0], 20: [11, inf] | change 's photo | Google_Photos |
| 203. | speech | 18: [16, inf], 40: [10, inf] | speech 's bush | Mission_Accomplished_speech |
| 204. | treaty | 18: [21, 10.5], 27: [15, 5.0], 36: [18, inf], 50: [30, 15.0] | treaty bush missile | Anti-Ballistic_Missile_Treaty |
| 205. | zambia | 18: [13, inf], 52: [11, inf] | zambia 's party | List_of_political_parties_in_Zambia |
| 206. | chiluba | 18: [11, inf] | chiluba zambia 's | Frederick_Chiluba |
| 207. | citizens | 18: [16, inf] | citizens 's china | Visa_requirements_for_Chinese_citizens |
| 208. | korean | 18: [12, inf], 33: [43, 6.14], 41: [14, inf] | korean north korea | North_Korea–South_Korea_relations |
| 209. | gloria | 18: [10, inf] | gloria philippines arroyo | Gloria_Macapagal_Arroyo |
| 210. | macapagal | 18: [10, inf] | macapagal philippines arroyo | Jose_Miguel_Arroyo |
| 211. | arroyo | 18: [11, inf] | arroyo philippines gloria | Gloria_Macapagal_Arroyo |
| 212. | days | 18: [12, 6.0], 26: [10, 5.0], 35: [10, 5.0], 38: [10, inf] | days 's taliban | Taliban |
| 213. | liberia | 18: [10, inf] | liberia 's united | Liberia–United_States_relations |
| 214. | bishops | 18: [10, inf] | bishops pope catholic | Bishops_in_the_Catholic_Church |
| 215. | commission | 18: [14, inf], 32: [14, inf], 50: [10, 5.0] | commission 's rights | National_Human_Rights_Commission_of_India |
| 216. | berlusconi | 19: [24, 12.0], 22: [10, inf], 39: [13, 13.0] | berlusconi italy 's | Silvio_Berlusconi |
| 217. | dues | 19: [12, inf] | dues us united | United_States_dollar |
| 218. | loss | 19: [10, inf] | loss 's american | Hearing_loss |
| 219. | history | 19: [11, inf] | history 's photo | Google_Photos |
| 220. | shipman | 19: [12, inf] | shipman harold doctor | Harold_Shipman |
| 221. | german | 19: [10, 5.0], 34: [14, 7.0], 36: [12, inf], 39: [15, inf] | german germany 's | Germany |
| 222. | women | 20: [13, 13.0], 22: [10, 5.0], 24: [13, inf], 30: [15, 7.5], 33: [10, 10.0] | women 's taliban | Taliban_treatment_of_women |
| 223. | slaughter | 20: [10, inf] | slaughter disease 's | Animal_slaughter |
| 224. | chickens | 20: [13, inf] | chickens hong kong | Hong_Kong_Soya_Sauce_Chicken_Rice_and_Noodle |
| 225. | flu | 20: [11, inf] | flu hong kong | Hong_Kong_flu |
| 226. | suicide | 20: [10, inf], 32: [14, inf], 37: [13, 6.5], 39: [10, 5.0] | suicide palestinian israeli | Use_of_child_suicide_bombers_by_Palestinian_militant_groups |
| 227. | sudan | 21: [10, inf] | sudan 's government | South_Sudan |
| 228. | rajoub | 21: [11, inf] | rajoub palestinian 's | Jibril_Rajoub |
| 229. | cable | 21: [14, inf] | cable american german | Cable_television |
| 230. | pakistan | 21: [14, inf], 25: [10, 5.0], 33: [10, 10.0], 37: [11, 5.5] | pakistan 's taliban | Tehrik-i-Taliban_Pakistan |
| 231. | chad | 22: [12, inf] | chad candidates africa | 2021_Chadian_presidential_election |
| 232. | wants | 22: [16, inf] | wants 's bush | Cori_Bush |
| 233. | union | 22: [10, inf] | union european 's | European_Union |
| 234. | arafat | 22: [17, inf], 26: [11, 5.5], 34: [14, 14.0], 48: [15, 15.0] | arafat palestinian israeli | Yasser_Arafat |
| 235. | special | 22: [10, inf], 42: [25, 12.5] | special taliban 's | Taliban |
| 236. | indonesian | 22: [10, inf] | indonesian indonesia wahid | Indonesian_Democratic_Party_of_Struggle |
| 237. | abdurrahman | 22: [13, inf] | abdurrahman wahid indonesia | Abdurrahman_Wahid |
| 238. | vote | 22: [21, 7.0], 28: [13, inf], 44: [11, 11.0] | vote 's party | Party-line_vote |
| 239. | republic | 22: [14, inf] | republic 's world | South_Korea |
| 240. | jakarta | 22: [10, inf] | jakarta 's indonesia | Jakarta |
| 241. | company | 22: [10, inf] | company 's oil | Shell_Oil_Company |
| 242. | elf | 22: [10, inf], 25: [11, inf] | elf former dumas | Elf_Aquitaine |
| 243. | nepal | 22: [12, inf], 45: [11, inf], 48: [10, 5.0] | nepal 's world | Nepal |
| 244. | zimbabwe | 22: [10, 5.0], 32: [16, inf], 36: [10, inf] | zimbabwe 's government | Hyperinflation_in_Zimbabwe |
| 245. | rumsfeld | 23: [21, inf], 40: [18, 9.0] | rumsfeld defense taliban | Donald_Rumsfeld |
| 246. | donald | 23: [11, inf], 40: [13, 6.5] | donald rumsfeld defense | Donald_Rumsfeld |
| 247. | khatami | 23: [10, inf], 32: [10, 5.0] | khatami iran 's | Mohammad_Khatami |
| 248. | tiananmen | 23: [10, inf] | tiananmen gong falun | Tiananmen_Square_self-immolation_incident |
| 249. | massacre | 23: [15, inf] | massacre 's nepal | Nepalese_royal_massacre |
| 250. | favor | 23: [10, inf] | favor 's powell | Colin_Powell |
| 251. | catholic | 23: [10, inf], 25: [11, inf] | catholic 's church | Catholic_Church |
| 252. | potato | 23: [10, inf] | potato irish famines | Great_Famine_(Ireland) |
| 253. | warming | 24: [15, inf] | warming bush global | Global_warming_controversy |
| 254. | northern | 25: [10, inf], 36: [10, 5.0] | northern taliban alliance | Northern_Alliance |
| 255. | koreans | 26: [10, inf] | koreans north korea | North_Korea–South_Korea_relations |
| 256. | transfer | 26: [12, inf] | transfer milosevic government | Slobodan_Milošević |
| 257. | kofi | 26: [10, inf] | kofi annan united | Kofi_Annan |
| 258. | annan | 26: [12, inf], 41: [19, inf], 50: [19, 19.0] | annan united kofi | Kofi_Annan |
| 259. | already | 26: [13, inf] | already 's government | Federal_government_of_the_United_States |
| 260. | seven | 26: [12, inf], 50: [16, 5.33] | seven 's israeli | Israel–United_States_relations |
| 261. | making | 26: [11, 11.0], 44: [11, inf] | making 's photo | Donald_Trump_photo_op_at_St._John's_Church |
| 262. | reported | 27: [10, inf] | reported 's world | U.S._News_&_World_Report |
| 263. | fuat | 27: [12, inf] | fuat turkey muslim | Mehmet_Fuat_Köprülü |
| 264. | followers | 27: [10, inf] | followers 's gong | Falun_Gong |
| 265. | germany | 27: [12, inf], 29: [12, inf] | germany 's german | Germany |
| 266. | test | 27: [11, inf] | test 's treaty | Comprehensive_Nuclear-Test-Ban_Treaty |
| 267. | sri | 28: [11, inf] | sri lanka rebels | Sri_Lankan_Civil_War |
| 268. | strategy | 28: [10, inf], 41: [12, 6.0], 51: [12, inf] | strategy 's bush | Bush_Doctrine |
| 269. | agreement | 29: [11, 5.5], 34: [12, inf] | agreement 's us | Comprehensive_and_Progressive_Agreement_for_Trans-Pacific_Partnership |
| 270. | salmon | 29: [10, inf] | salmon invercreran fish | EMPTY MATCHING |
| 271. | blood | 29: [16, inf] | blood 's aids | HIV/AIDS |
| 272. | protesters | 29: [14, inf] | protesters 's police | George_Floyd_protests |
| 273. | industrialized | 29: [11, inf] | industrialized leaders nations | Newly_industrialized_country |
| 274. | monitors | 29: [19, inf] | monitors rights human | Human_rights |
| 275. | eight | 29: [11, inf] | eight 's israel | Israel |
| 276. | whether | 30: [11, inf] | whether 's bush | George_W._Bush |
| 277. | shrine | 30: [17, inf], 33: [13, 6.5] | shrine 's japan | Yasukuni_Shrine |
| 278. | past | 30: [14, inf] | past 's photo | Google_Photos |
| 279. | devi | 30: [11, inf] | devi india 's | Shakuntala_Devi |
| 280. | racism | 31: [12, inf], 35: [11, inf] | racism conference israel | World_Conference_against_Racism_2001 |
| 281. | trucks | 31: [13, inf] | trucks tunnel 's | Eisenhower_Tunnel |
| 282. | boys | 31: [10, inf] | boys two israeli | Our_Boys_(miniseries) |
| 283. | block | 31: [11, inf], 41: [10, 5.0] | block 's bush | Bush–Breyman_Block |
| 284. | ministry | 31: [10, inf] | ministry 's foreign | Ministry_of_Foreign_Affairs_of_the_People's_Republic_of_China |
| 285. | investigation | 31: [10, inf], 40: [10, 10.0] | investigation 's american | Special_Counsel_investigation_(2017–2019) |
| 286. | farrakhan | 31: [10, inf] | farrakhan britain ban | R_(on_the_application_of_Farrakhan)_v_Secretary_of_State_for_the_Home_Department |
| 287. | bosnia | 31: [10, inf] | bosnia bosnian crimes | Bosnian_War |
| 288. | golf | 32: [10, inf] | golf 's journal | Men's_major_golf_championships |
| 289. | break | 32: [10, 5.0], 46: [10, inf] | break 's bush | Barbara_Bush_(born_1981) |
| 290. | zemin | 32: [18, inf] | zemin china 's | Jiang_Zemin |
| 291. | bomber | 32: [11, inf] | bomber palestinian suicide | Use_of_child_suicide_bombers_by_Palestinian_militant_groups |
| 292. | vatican | 32: [10, inf] | vatican 's pope | Pope_John_Paul_I_conspiracy_theories |
| 293. | armed | 33: [14, inf] | armed 's forces | United_States_Armed_Forces |
| 294. | signed | 33: [11, inf] | signed 's peace | Peace_symbols |
| 295. | th | 33: [11, inf] | th 's us | Thnks_fr_th_Mmrs |
| 296. | nato | 33: [28, inf], 49: [10, inf] | nato 's macedonia | North_Macedonia–NATO_relations |
| 297. | coins | 33: [10, inf] | coins euro european | Euro_coins |
| 298. | rice | 33: [12, inf] | rice bush 's | Condoleezza_Rice |
| 299. | epidemic | 34: [14, inf] | epidemic aids 's | Epidemiology_of_HIV/AIDS |
| 300. | neighboring | 35: [11, inf] | neighboring 's says | Says |
| 301. | myanmar | 35: [16, inf] | myanmar 's world | Myanmar |
| 302. | town | 35: [28, 28.0], 37: [12, inf] | town 's israeli | List_of_cities_in_Israel |
| 303. | beit | 35: [24, inf] | beit israeli palestinian | 2006_Israeli_operation_in_Beit_Hanoun |
| 304. | jala | 35: [26, inf] | jala israeli palestinian | Beit_Jala |
| 305. | stop | 35: [10, inf] | stop 's says | My_Brain_Says_Stop,_But_My_Heart_Says_Go! |
| 306. | gilo | 35: [15, inf] | gilo israeli palestinian | Gilo |
| 307. | euro | 35: [12, inf], 52: [14, 7.0] | euro european currency | Euro |
| 308. | islamic | 36: [10, 5.0], 38: [26, inf] | islamic 's taliban | Islamic_Emirate_of_Afghanistan |
| 309. | african | 36: [11, inf] | african africa south | South_Africa |
| 310. | grant | 36: [10, inf] | grant 's bush | U.S._Presidential_IQ_hoax |
| 311. | `` | 37: [13, 13.0], 46: [13, inf] | `` 's today | Today_(American_TV_program) |
| 312. | around | 37: [12, inf], 46: [24, 12.0] | around 's world | Around_the_World_in_a_Day |
| 313. | timor | 37: [15, inf] | timor east world | East_Timor |
| 314. | center | 37: [15, 7.5], 50: [10, inf] | center 's world | World_Trade_Center_(1973–2001) |
| 315. | pakistani | 38: [12, inf] | pakistani taliban pakistan | Tehrik-i-Taliban_Pakistan |
| 316. | afghans | 38: [11, 11.0], 46: [10, inf], 51: [25, 6.25] | afghans taliban afghanistan | War_in_Afghanistan_(2001–present) |
| 317. | top | 38: [13, inf] | top 's laden | Killing_of_Osama_bin_Laden |
| 318. | action | 38: [13, inf], 48: [11, 5.5] | action 's bush | Presidency_of_George_W._Bush |
| 319. | militant | 38: [11, inf], 49: [12, inf] | militant 's pakistan | Pakistan_and_state-sponsored_terrorism |
| 320. | cease-fire | 38: [19, inf] | cease-fire palestinian israel | Israeli–Palestinian_conflict |
| 321. | targets | 38: [17, inf], 44: [10, 5.0] | targets taliban 's | Taliban |
| 322. | changes | 38: [11, inf] | changes 's american | United_States_involvement_in_regime_change |
| 323. | clerics | 38: [17, inf] | clerics taliban laden | Taliban |
| 324. | demands | 38: [11, inf] | demands 's says | Say's_law |
| 325. | congress | 38: [12, 6.0], 51: [10, inf] | congress 's bush | Presidency_of_George_H._W._Bush |
| 326. | information | 39: [12, inf] | information 's says | Say's_law |
| 327. | american-led | 39: [10, inf], 41: [15, 7.5] | american-led afghanistan 's | War_in_Afghanistan_(2001–present) |
| 328. | havel | 39: [10, inf] | havel czech vaclav | Václav_Havel_Airport_Prague |
| 329. | persuade | 39: [10, inf] | persuade 's taliban | Tehrik-i-Taliban_Pakistan |
| 330. | hijackers | 39: [13, inf] | hijackers laden attacks | Responsibility_for_the_September_11_attacks |
| 331. | quetta | 39: [16, inf] | quetta pakistan taliban | Quetta_Shura |
| 332. | king | 39: [12, inf] | king 's bush | Kate_Bush |
| 333. | milan— | 39: [10, inf] | milan— 's fashion | Fashion_in_Milan |
| 334. | discuss | 40: [11, inf] | discuss 's bush | George_H._W._Bush |
| 335. | nuclear | 40: [26, inf], 44: [33, 16.5], 49: [20, 10.0] | nuclear 's bush | India–United_States_Civil_Nuclear_Agreement |
| 336. | short | 40: [13, inf] | short 's us | Short_Empire |
| 337. | september | 40: [14, inf] | september 's attacks | September_11_attacks |
| 338. | asia/pacific | 40: [24, inf] | asia/pacific world briefing | Trans-Pacific_Partnership |
| 339. | abortion | 40: [10, inf] | abortion 's ireland | Abortion_in_the_Republic_of_Ireland |
| 340. | involved | 40: [11, inf] | involved 's military | Military |
| 341. | crash | 40: [10, inf] | crash 's tunnel | Eisenhower_Tunnel |
| 342. | separatist | 41: [11, inf] | separatist 's basque | Basque_nationalism |
| 343. | georgia | 41: [11, 5.5], 44: [10, inf] | georgia world abkhazia | List_of_cities_and_towns_in_Georgia_(country) |
| 344. | bombers | 41: [10, inf] | bombers says 's | Tupolev_Tu-160 |
| 345. | broadcast | 41: [10, inf] | broadcast 's laden | Bin_Laden_family |
| 346. | night | 41: [10, inf] | night 's taliban | Taliban |
| 347. | us-led | 41: [10, inf] | us-led 's says | Saudi_Arabian-led_intervention_in_Yemen |
| 348. | chirac | 41: [10, inf], 46: [10, 5.0] | chirac pres jacques | Jacques_Chirac |
| 349. | sites | 41: [10, inf] | sites 's taliban | Tehrik-i-Taliban_Pakistan |
| 350. | airstrikes | 41: [41, inf] | airstrikes taliban 's | Kunduz_hospital_airstrike |
| 351. | boat | 41: [10, inf], 52: [15, inf] | boat 's south | E-boat |
| 352. | jazeera | 41: [10, inf] | jazeera laden 's | Videos_and_audio_recordings_of_Osama_bin_Laden |
| 353. | prepare | 41: [10, inf] | prepare 's says | Si_vis_pacem,_para_bellum |
| 354. | service | 41: [13, 6.5], 44: [13, inf] | service 's bush | George_W._Bush_military_service_controversy |
| 355. | honey | 41: [11, inf] | honey 's laden | Caucasian_honey_bee |
| 356. | challenged | 41: [10, inf] | challenged 's afghanistan | United_States_invasion_of_Afghanistan |
| 357. | prayer | 41: [14, inf] | prayer 's thousands | Prayer |
| 358. | mosques | 41: [12, inf] | mosques 's afghanistan | List_of_mosques_in_Afghanistan |
| 359. | mosque | 41: [12, inf] | mosque 's islam | Holiest_sites_in_Islam |
| 360. | nobel | 41: [18, inf], 50: [16, inf] | nobel prize 's | Nobel_Prize_in_Literature |
| 361. | prize | 41: [13, inf], 50: [12, inf] | prize nobel 's | Nobel_Prize |
| 362. | moderate | 42: [11, inf] | moderate 's taliban | Taliban |
| 363. | dr. | 42: [10, inf] | dr. world 's | Dr._Mario_World |
| 364. | marcos | 42: [10, inf] | marcos philippines 's | History_of_the_Philippines_(1965–1986) |
| 365. | zeevi | 42: [12, inf] | zeevi palestinian israeli | Timeline_of_the_Israeli–Palestinian_conflict |
| 366. | raid | 42: [18, 9.0], 48: [16, inf] | raid 's israeli | 1968_Israeli_raid_on_Lebanon |
| 367. | sinn | 43: [10, inf] | sinn fein ireland | Sinn_Féin |
| 368. | fein | 43: [10, inf] | fein sinn ireland | Sinn_Féin |
| 369. | dismantling | 43: [11, inf] | dismantling plane immigrants | Digital_native |
| 370. | alps | 43: [11, inf] | alps tunnel killed | Alps |
| 371. | gotthard | 43: [11, inf] | gotthard tunnel swiss | Gotthard_Tunnel |
| 372. | haq | 43: [19, inf] | haq taliban afghanistan | Taliban |
| 373. | b- | 44: [12, inf] | b- taliban afghanistan | Islamic_Emirate_of_Afghanistan |
| 374. | wheat | 44: [10, inf] | wheat afghanistan aid | Economy_of_Afghanistan |
| 375. | bases | 45: [14, inf] | bases military 's | List_of_United_States_military_bases |
| 376. | strike | 45: [12, inf] | strike 's taliban | Taliban |
| 377. | tajikistan | 45: [16, inf] | tajikistan taliban uzbekistan | Islamic_Movement_of_Uzbekistan |
| 378. | leadership | 45: [12, inf] | leadership 's taliban | Taliban |
| 379. | patents | 45: [12, inf] | patents aids drugs | Prizes_as_an_alternative_to_patents |
| 380. | capture | 45: [11, inf] | capture taliban american | Taliban |
| 381. | describes | 45: [10, inf] | describes 's says | Say's_law |
| 382. | red | 45: [10, inf] | red 's cross | International_Red_Cross_and_Red_Crescent_Movement |
| 383. | order | 46: [14, inf] | order 's says | Order_of_the_British_Empire |
| 384. | pashtuns | 46: [10, inf] | pashtuns taliban alliance | Northern_Alliance |
| 385. | quickly | 46: [10, inf] | quickly 's taliban | Taliban |
| 386. | lives | 46: [10, inf] | lives 's photo | Black_Lives_Matter |
| 387. | omar | 46: [25, inf] | omar taliban 's | Mohammed_Omar |
| 388. | wars | 46: [10, inf] | wars milosevic 's | Slobodan_Milošević |
| 389. | cuba | 46: [10, inf] | cuba 's pres | Cuba–United_States_relations |
| 390. | construction | 46: [10, inf] | construction 's world | Construction_of_the_World_Trade_Center |
| 391. | kunduz | 46: [17, inf] | kunduz taliban alliance | Kunduz_airlift |
| 392. | mountains | 46: [10, inf], 50: [16, 8.0] | mountains 's taliban | Taliban |
| 393. | envoys | 47: [11, inf] | envoys peace 's | United_States_Special_Envoy_for_Northern_Ireland |
| 394. | mandela | 47: [10, inf] | mandela africa 's | Nelson_Mandela |
| 395. | madikizela-mandela | 47: [10, inf] | madikizela-mandela 's mandela | Winnie_Madikizela-Mandela |
| 396. | hamas | 47: [10, inf], 49: [31, 15.5] | hamas palestinian israeli | Hamas |
| 397. | predator | 47: [10, inf] | predator air aircraft | General_Atomics_MQ-1_Predator |
| 398. | sports | 47: [12, inf] | sports job find | Dave_Holmes_(sportscaster) |
| 399. | yemen | 47: [10, inf] | yemen cole attack | USS_Cole_bombing |
| 400. | wounded | 48: [13, inf] | wounded killed 's | List_of_United_States_Congress_members_killed_or_wounded_in_office |
| 401. | uncertain | 48: [10, inf] | uncertain 's taliban | Taliban_insurgency |
| 402. | fortress | 48: [12, inf] | fortress prisoners alliance | Battle_of_Qala-i-Jangi |
| 403. | zinni | 48: [12, inf] | zinni palestinian israeli | List_of_Israeli_assassinations |
| 404. | prisoner | 48: [12, inf] | prisoner taliban prisoners | Bagram_torture_and_prisoner_abuse |
| 405. | fort | 48: [16, inf] | fort taliban prisoners | Bowe_Bergdahl |
| 406. | belgian | 48: [10, inf] | belgian belgium 's | Belgian_chocolate |
| 407. | chile | 48: [10, inf] | chile pinochet augusto | Lucía_Pinochet |
| 408. | delegation | 48: [10, inf] | delegation 's world | Delegation_(band) |
| 409. | vietnam | 48: [16, inf] | vietnam 's asia | Vietnam |
| 410. | meets | 48: [11, inf] | meets 's bush | George_H._W._Bush |
| 411. | extremists | 49: [15, inf] | extremists 's arafat | Raymonda_Tawil |
| 412. | draft | 49: [12, inf] | draft 's would | 2012_NFL_Draft |
| 413. | parliamentary | 49: [13, inf] | parliamentary 's elections | General_election |
| 414. | hamid | 49: [11, inf] | hamid karzai taliban | Hamid_Karzai |
| 415. | karzai | 49: [18, inf] | karzai taliban afghanistan | Afghanistan_conflict_(1978–present) |
| 416. | violent | 49: [10, inf] | violent 's photo | Donald_Trump_photo_op_at_St._John's_Church |
| 417. | yemeni | 49: [10, inf] | yemeni yemen us | Yemeni_Civil_War_(2014–present) |
| 418. | continued | 50: [11, inf] | continued 's says | To_Be_Continued..._(box_set) |
| 419. | videotape | 50: [16, inf] | videotape laden says | Bin_Laden_family |
| 420. | tape | 50: [24, inf], 52: [12, 6.0] | tape laden 's | Videos_and_audio_recordings_of_Osama_bin_Laden |
| 421. | antiballistic | 50: [12, inf] | antiballistic missile treaty | Anti-Ballistic_Missile_Treaty |
| 422. | contact | 50: [10, inf] | contact 's arafat | Yasser_Arafat |
| 423. | orders | 50: [11, inf] | orders 's world | Superior_orders |
| 424. | prodi | 50: [10, inf] | prodi european commission | Prodi_Commission |
| 425. | peacekeeping | 51: [15, inf] | peacekeeping nato troops | List_of_NATO_operations |
| 426. | agents | 51: [10, inf] | agents 's officials | Agents_of_S.H.I.E.L.D. |
| 427. | recalls | 51: [10, inf] | recalls india pakistan | Indo-Pakistani_War_of_1971 |
| 428. | brought | 51: [10, inf] | brought 's says | Brought_by_the_Sea |
| 429. | buildup | 52: [10, inf] | buildup china 's | China–United_States_relations |
| 430. | reid | 52: [23, inf] | reid northern 's | Harry_Reid |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | kabila | 3: [12, inf] | kabila 's congo | Laurent-Désiré_Kabila |
| 2. | spy | 14: [13, inf] | spy plane us | Hainan_Island_incident |
| 3. | plane | 14: [12, inf] | plane spy us | Hainan_Island_incident |
| 4. | anthrax | 41: [19, inf] | anthrax us case | 2001_anthrax_attacks |
| 5. | aid | 46: [16, inf] | aid workers taliban | Taliban_treatment_of_women |
| 6. | workers | 46: [12, inf] | workers aid taliban | Taliban_treatment_of_women |
| 7. | kunduz | 47: [10, inf] | kunduz surrender alliance | Siege_of_Kunduz |
| 8. | arafat | 49: [12, inf] | arafat 's israel | Yasser_Arafat |