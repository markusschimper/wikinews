# Keywords with the highest 'interestingness' in 2002

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
| 1. | singapore | 2: [16, inf], 4: [14, 7.0] | singapore qaeda indonesia | Jemaah_Islamiyah |
| 2. | speech | 2: [23, inf], 14: [22, 22.0], 26: [33, 6.6], 32: [17, inf] | speech 's bush | Mission_Accomplished_speech |
| 3. | nation | 2: [16, inf], 35: [11, 11.0] | nation 's function | List_of_specialized_agencies_of_the_United_Nations |
| 4. | day | 2: [10, inf], 45: [12, 6.0] | day 's israeli | Independence_Day_(Israel) |
| 5. | saint | 2: [10, inf] | saint 's pope | Pope_Pius_X |
| 6. | laurent | 2: [10, inf] | laurent saint french | Yves_Saint_Laurent_(designer) |
| 7. | mr. | 2: [19, inf], 24: [18, inf], 29: [10, inf], 40: [10, inf], 46: [17, 17.0], 49: [12, inf] | mr. 's world | Toyota_MR2 |
| 8. | gaza | 2: [19, 9.5], 16: [11, inf], 19: [36, inf], 30: [16, 8.0], 39: [23, 23.0], 41: [19, 19.0] | gaza israeli palestinian | Gaza_War_(2008–2009) |
| 9. | turkey | 2: [16, 8.0], 18: [11, inf], 40: [15, 7.5], 44: [15, 5.0] | turkey 's iraq | Iraq–Turkey_relations |
| 10. | building | 2: [12, inf] | building 's palestinian | Palestinian_Legislative_Council |
| 11. | terror | 2: [12, inf], 19: [15, inf] | terror 's bush | War_on_terror |
| 12. | issued | 2: [12, inf], 46: [14, 14.0] | issued 's says | Say_Say_Say |
| 13. | general | 2: [10, 10.0], 36: [11, inf], 43: [15, inf] | general 's iraq | Iraq_War |
| 14. | saying | 2: [14, 7.0], 42: [11, inf] | saying 's bush | George_W._Bush |
| 15. | nuclear | 2: [37, inf], 31: [21, 5.25], 34: [10, 5.0], 42: [38, 5.43] | nuclear north korea | North_Korea_and_weapons_of_mass_destruction |
| 16. | protest | 2: [10, 10.0], 28: [12, inf], 35: [10, 5.0] | protest 's world | Protest |
| 17. | airport | 2: [17, 8.5], 49: [11, inf] | airport american 's | List_of_busiest_airports_by_passenger_traffic |
| 18. | plane | 2: [18, inf], 16: [14, inf], 48: [17, 5.67] | plane 's crash | Lynyrd_Skynyrd_plane_crash |
| 19. | visit | 2: [10, inf], 30: [12, 6.0], 42: [13, 6.5], 49: [15, 5.0] | visit 's bush | George_W._Bush |
| 20. | aboard | 2: [10, inf] | aboard plane crash | Germanwings_Flight_9525 |
| 21. | vatican | 2: [11, inf], 42: [11, inf] | vatican pope church | Second_Vatican_Council |
| 22. | power | 2: [10, inf] | power 's government | Federal_government_of_the_United_States |
| 23. | cuba | 2: [10, inf], 19: [15, 7.5], 38: [12, inf] | cuba 's prisoners | Cuban_Five |
| 24. | sec | 2: [10, inf], 11: [11, 5.5] | sec 's says | U.S._Securities_and_Exchange_Commission |
| 25. | catholic | 2: [10, inf], 46: [10, 5.0] | catholic church 's | Catholic_Church |
| 26. | colombia | 2: [12, inf], 5: [13, 6.5] | colombia rebels 's | Revolutionary_Armed_Forces_of_Colombia |
| 27. | pastrana | 2: [15, inf], 8: [11, inf] | pastrana rebels colombia | Revolutionary_Armed_Forces_of_Colombia |
| 28. | zone | 2: [12, inf], 48: [11, 11.0] | zone 's north | Eastern_Time_Zone |
| 29. | colin | 2: [10, inf], 14: [21, 7.0], 36: [17, 17.0], 51: [10, 10.0] | colin powell 's | Colin_Powell |
| 30. | powell | 2: [12, inf], 14: [27, 9.0], 36: [26, 26.0], 51: [18, 18.0] | powell 's bush | Colin_Powell |
| 31. | home | 2: [10, inf] | home 's photo | Photo_Booth |
| 32. | fashion | 3: [12, inf], 11: [11, 5.5], 41: [16, 8.0] | fashion 's luxury | Italian_fashion |
| 33. | schools | 3: [18, 9.0], 44: [12, inf], 47: [13, 6.5] | schools 's government | Federal_government_of_the_United_States |
| 34. | jerusalem | 3: [11, inf], 25: [21, 10.5], 31: [25, 12.5] | jerusalem israeli palestinian | East_Jerusalem |
| 35. | town | 3: [13, inf] | town 's israeli | List_of_cities_in_Israel |
| 36. | jewish | 3: [10, inf], 14: [11, 5.5], 22: [10, 10.0], 43: [20, 10.0] | jewish israeli palestinian | Israeli–Palestinian_conflict |
| 37. | book | 3: [12, inf] | book 's photo | Photo-book |
| 38. | haiti | 3: [10, inf], 36: [10, 10.0] | haiti 's aristide | Jean-Bertrand_Aristide |
| 39. | opium | 3: [10, inf] | opium 's afghanistan | Opium_production_in_Afghanistan |
| 40. | return | 4: [10, 5.0], 9: [12, inf], 12: [18, 6.0] | return 's iraq | Iraq_War |
| 41. | raid | 4: [16, 5.33], 39: [13, inf] | raid israeli 's | Raid_on_Entebbe_(film) |
| 42. | arabia | 4: [12, 6.0], 25: [10, inf], 38: [11, inf] | arabia saudi 's | Saudi_Arabia |
| 43. | congress | 4: [10, 5.0], 6: [10, inf], 9: [10, inf], 35: [15, 15.0] | congress 's bush | Cori_Bush |
| 44. | muslims | 4: [11, 5.5], 9: [17, 8.5], 18: [12, inf] | muslims 's muslim | Muslims |
| 45. | bomber | 4: [11, inf] | bomber suicide israeli | Use_of_child_suicide_bombers_by_Palestinian_militant_groups |
| 46. | arms | 4: [15, 7.5], 9: [14, 14.0], 23: [11, inf] | arms iraq 's | Coat_of_arms_of_Iraq |
| 47. | ago | 4: [10, inf], 30: [10, 5.0] | ago 's years | All_Those_Years_Ago |
| 48. | district | 4: [10, inf] | district 's killed | List_of_law_enforcement_officers_killed_in_the_line_of_duty_in_the_United_States |
| 49. | main | 5: [10, inf] | main 's government | Federal_government_of_the_United_States |
| 50. | captives | 5: [16, inf] | captives prisoners 's | List_of_Guantanamo_Bay_detainees |
| 51. | message | 5: [22, inf] | message 's bush | Marvin_Bush |
| 52. | pearl | 5: [33, 16.5], 17: [27, inf] | pearl pakistan reporter | Mariane_Pearl |
| 53. | militant | 5: [10, 5.0], 9: [10, 5.0], 17: [13, inf] | militant 's pakistan | Insurgency_in_Khyber_Pakhtunkhwa |
| 54. | york | 5: [21, 10.5], 16: [28, inf] | york function 's | Riemann_zeta_function |
| 55. | policy | 5: [21, 5.25], 14: [14, 7.0], 49: [11, inf] | policy 's bush | Foreign_policy_of_the_George_W._Bush_administration |
| 56. | office | 5: [10, 5.0], 8: [20, 5.0], 43: [10, inf] | office 's government | Government_Accountability_Office |
| 57. | outside | 5: [11, 5.5], 12: [12, 6.0], 24: [11, 11.0], 38: [12, inf], 43: [11, 5.5], 49: [13, inf] | outside 's government | Federal_government_of_the_United_States |
| 58. | school | 5: [11, inf], 9: [15, 5.0], 17: [18, inf], 42: [18, 9.0], 49: [11, inf] | school 's children | Professional_Children's_School |
| 59. | journalists | 5: [11, 11.0], 13: [13, inf] | journalists 's government | List_of_journalists_killed_in_Europe |
| 60. | mugabe | 5: [11, inf], 33: [12, inf] | mugabe zimbabwe 's | Robert_Mugabe |
| 61. | 'axis | 5: [14, inf] | 'axis bush 's | Axis_of_evil |
| 62. | swiss | 5: [10, 10.0], 27: [23, inf] | swiss switzerland 's | Demographics_of_Switzerland |
| 63. | politicians | 5: [10, inf] | politicians 's government | List_of_foreign-born_United_States_politicians |
| 64. | koizumi | 5: [10, inf] | koizumi japan 's | Junichiro_Koizumi |
| 65. | abuse | 5: [10, inf], 43: [18, inf] | abuse 's priests | Catholic_Church_sexual_abuse_cases |
| 66. | dept | 5: [10, inf] | dept 's state | United_States_Department_of_State |
| 67. | intelligence | 6: [24, 6.0], 18: [11, inf] | intelligence 's officials | William_Binney_(intelligence_official) |
| 68. | ends | 6: [13, 6.5], 16: [10, inf], 36: [10, inf] | ends 's world | It's_the_End_of_the_World |
| 69. | musharraf | 6: [13, inf], 17: [11, inf], 22: [19, 9.5], 33: [13, 13.0] | musharraf pakistan 's | Pervez_Musharraf |
| 70. | kashmir | 6: [12, 6.0], 20: [15, inf], 29: [19, 6.33], 37: [12, 6.0], 51: [14, 14.0] | kashmir india pakistan | Kashmir |
| 71. | missing | 6: [14, inf], 49: [12, 6.0] | missing 's dead | The_Missing_and_the_Dead |
| 72. | heisenberg | 6: [12, inf] | heisenberg bohr 's | Niels_Bohr |
| 73. | bohr | 6: [12, inf] | bohr heisenberg 's | Niels_Bohr |
| 74. | sheikh | 6: [16, inf], 11: [16, 8.0], 17: [11, inf] | sheikh pearl pakistan | Daniel_Pearl |
| 75. | vaccine | 7: [10, 5.0], 13: [10, inf] | vaccine smallpox health | Smallpox_vaccine |
| 76. | saudi | 7: [14, 7.0], 9: [33, 8.25], 13: [29, 5.8], 25: [14, 7.0], 33: [17, inf], 38: [13, 13.0], 47: [31, 15.5] | saudi 's arabia | Saudi_Arabia |
| 77. | trial | 7: [28, inf], 17: [35, 5.83], 24: [28, 28.0], 40: [22, 7.33] | trial 's milosevic | Trial_of_Slobodan_Milošević |
| 78. | milosevic | 7: [40, inf], 18: [11, 5.5], 24: [10, inf], 30: [11, inf], 34: [10, inf], 39: [19, inf] | milosevic crimes trial | Trial_of_Slobodan_Milošević |
| 79. | slobodan | 7: [12, inf] | slobodan milosevic crimes | Trial_of_Slobodan_Milošević |
| 80. | yugoslavia | 7: [11, inf] | yugoslavia milosevic europe | Slobodan_Milošević |
| 81. | feb | 7: [12, inf] | feb 's government | Government_of_the_United_Kingdom |
| 82. | crimes | 7: [25, inf], 40: [10, 5.0], 49: [10, 10.0] | crimes milosevic trial | Trial_of_Slobodan_Milošević |
| 83. | kosovo | 7: [12, inf], 52: [11, inf] | kosovo milosevic crimes | Slobodan_Milošević |
| 84. | rockets | 7: [12, inf] | rockets israeli palestinian | Palestinian_rocket_attacks_on_Israel |
| 85. | border | 7: [10, 10.0], 21: [12, 12.0], 31: [13, inf] | border pakistan 's | India–Pakistan_border |
| 86. | budget | 7: [11, 5.5], 11: [11, 5.5], 44: [13, inf] | budget 's government | Government_budget |
| 87. | protests | 7: [10, inf] | protests 's government | Protest |
| 88. | genocide | 7: [14, inf] | genocide crimes trial | Genocide |
| 89. | serb | 7: [10, inf], 40: [11, 11.0] | serb crimes bosnian | Bosnian_War |
| 90. | falun | 7: [12, inf], 14: [12, inf] | falun gong china | Persecution_of_Falun_Gong |
| 91. | gong | 7: [12, inf], 14: [12, inf] | gong falun china | Persecution_of_Falun_Gong |
| 92. | nato | 7: [10, inf], 9: [21, 21.0], 17: [14, inf], 20: [18, 6.0], 35: [11, 5.5], 47: [57, 6.33] | nato 's bush | Major_non-NATO_ally |
| 93. | italy | 7: [12, 12.0], 16: [12, inf], 19: [15, inf], 38: [16, 5.33] | italy 's europe | Italy |
| 94. | kenya | 7: [10, inf], 48: [32, 8.0], 52: [12, inf] | kenya 's africa | Kenya |
| 95. | marxist | 8: [10, inf] | marxist rebels 's | Marxism–Leninism |
| 96. | rebel | 8: [21, inf], 15: [12, 6.0], 25: [12, inf] | rebel 's government | Rebellion |
| 97. | seven | 8: [10, inf], 10: [10, inf], 31: [10, 10.0] | seven 's israeli | Israel–United_States_relations |
| 98. | armed | 8: [10, inf], 15: [11, inf] | armed 's military | United_States_Armed_Forces |
| 99. | board | 8: [10, inf] | board 's plane | Plane_(tool) |
| 100. | overseas | 8: [11, inf] | overseas 's us | Territories_of_the_United_States |
| 101. | mexican | 8: [10, inf], 33: [12, 6.0], 43: [11, 11.0] | mexican mexico 's | History_of_Mexico |
| 102. | rumsfeld | 8: [11, 5.5], 13: [13, inf] | rumsfeld defense donald | Donald_Rumsfeld |
| 103. | train | 8: [12, inf] | train 's military | Military_marine_mammal |
| 104. | guerrilla | 8: [10, inf], 30: [14, 7.0] | guerrilla 's group | People's_Guerrilla_Group |
| 105. | colombian | 8: [12, inf] | colombian colombia rebels | Revolutionary_Armed_Forces_of_Colombia |
| 106. | hope | 9: [10, inf] | hope 's bush | Bush_family |
| 107. | case | 9: [17, 5.67], 16: [10, inf], 25: [19, 9.5], 35: [12, inf], 43: [17, 8.5], 45: [23, 11.5] | case 's say | Say_Say_Say |
| 108. | muslim | 9: [12, 12.0], 17: [10, inf] | muslim 's american | Islam_in_the_United_States |
| 109. | region | 9: [13, 6.5], 19: [14, inf] | region 's function | Riemann_zeta_function |
| 110. | hindu | 9: [17, inf], 18: [10, inf], 20: [11, 5.5], 39: [13, inf] | hindu india 's | Hindu_Mahasabha |
| 111. | demand | 9: [10, 5.0], 26: [13, inf], 38: [10, inf] | demand 's bush | George_W._Bush |
| 112. | soviet | 9: [15, 7.5], 22: [10, inf] | soviet 's russia | Russian_Soviet_Federative_Socialist_Republic |
| 113. | lake | 9: [11, inf] | lake 's city | Salt_Lake_City |
| 114. | calls | 9: [16, inf], 50: [11, 5.5] | calls 's bush | Bush_family |
| 115. | groups | 9: [22, inf], 15: [11, 5.5] | groups 's government | Federal_government_of_the_United_States |
| 116. | abdullah | 9: [13, 6.5], 17: [20, inf] | abdullah saudi 's | Abdullah_of_Saudi_Arabia |
| 117. | future | 9: [16, inf], 29: [11, 11.0], 47: [12, 6.0] | future 's says | Say's_law |
| 118. | quebec | 9: [10, inf] | quebec province 's | Quebec |
| 119. | arab | 9: [21, inf], 13: [61, 6.1], 46: [14, inf] | arab 's israeli | Arab–Israeli_conflict |
| 120. | idea | 9: [10, inf] | idea 's bush | George_H._W._Bush |
| 121. | opposition | 9: [17, 5.67], 36: [13, inf] | opposition 's government | Parliamentary_opposition |
| 122. | witnesses | 9: [10, inf] | witnesses 's israeli | Criticism_of_Jehovah's_Witnesses |
| 123. | georgia | 9: [26, inf], 33: [20, 10.0] | georgia russia 's | Russo-Georgian_War |
| 124. | dozens | 9: [10, inf] | dozens 's israeli | Israel |
| 125. | mosque | 9: [12, inf] | mosque 's people | Sheikh_Zayed_Mosque |
| 126. | dna | 9: [18, inf] | dna 's say | The_DNA_Will_Have_Its_Say |
| 127. | kong | 9: [10, 5.0], 12: [11, inf], 25: [15, inf] | kong hong 's | Hong_Kong |
| 128. | total | 10: [10, inf] | total 's military | Total_SE |
| 129. | strategy | 10: [10, inf], 38: [10, 5.0], 43: [11, 5.5] | strategy 's bush | Bush_Doctrine |
| 130. | egypt | 10: [11, inf] | egypt 's israel | Egypt–Israel_peace_treaty |
| 131. | voters | 10: [11, inf] | voters 's party | Political_party_strength_in_U.S._states |
| 132. | helicopter | 10: [11, inf], 34: [19, inf] | helicopter military crash | 2011_Afghanistan_Boeing_Chinook_shootdown |
| 133. | another | 10: [10, 10.0], 44: [14, 14.0], 46: [14, inf] | another 's says | Say's_law |
| 134. | vienna | 10: [10, inf] | vienna 's united | Vienna |
| 135. | uterus | 10: [12, inf] | uterus transplant say | Organ_transplantation |
| 136. | design | 11: [10, inf] | design fashion 's | Fashion_design |
| 137. | march | 11: [11, 5.5], 14: [12, inf] | march 's israeli | Nuclear_weapons_and_Israel |
| 138. | press | 11: [10, inf], 13: [12, inf], 37: [15, 7.5] | press 's bush | George_W._Bush |
| 139. | korean | 11: [11, 5.5], 26: [22, 22.0], 47: [20, inf] | korean north korea | North_Korea–South_Korea_relations |
| 140. | camp | 11: [16, 5.33], 15: [20, inf], 22: [16, 8.0], 39: [22, 22.0], 48: [20, 5.0] | camp israeli palestinian | 2000_Camp_David_Summit |
| 141. | civilians | 11: [12, inf], 29: [14, 14.0], 33: [10, inf] | civilians israeli palestinian | 2006_Israeli_operation_in_Beit_Hanoun |
| 142. | yemen | 11: [14, inf], 41: [10, inf], 45: [14, inf] | yemen qaeda american | Al-Qaeda_insurgency_in_Yemen |
| 143. | begin | 11: [10, inf], 20: [10, 5.0], 34: [12, 6.0] | begin 's bush | George_W._Bush |
| 144. | montenegro | 11: [10, inf] | montenegro serbia yugoslavia | Serbia_and_Montenegro |
| 145. | monterrey | 12: [24, inf] | monterrey mexico aid | Mexico |
| 146. | labor | 12: [22, inf], 15: [11, inf], 28: [11, 5.5], 40: [11, 5.5], 44: [18, 9.0] | labor 's party | Minnesota_Democratic–Farmer–Labor_Party |
| 147. | list | 12: [10, inf] | list 's says | Say's_law |
| 148. | summit | 12: [10, 5.0], 35: [26, inf] | summit 's meeting | Summit_(meeting) |
| 149. | peru | 12: [15, inf] | peru 's pres | Pre-Columbian_Peru |
| 150. | seen | 12: [11, inf] | seen 's iraq | Iraq_War |
| 151. | tax | 12: [10, inf] | tax 's government | List_of_countries_by_tax_rates |
| 152. | arabs | 13: [22, inf] | arabs israeli israel | Arab_citizens_of_Israel |
| 153. | quake | 13: [10, inf] | quake earthquake people | 1994_Northridge_earthquake |
| 154. | polish | 13: [12, inf] | polish poland paetz | Juliusz_Paetz |
| 155. | paetz | 13: [10, inf] | paetz polish pope | Pope_John_Paul_II |
| 156. | young | 13: [10, inf], 27: [10, 5.0] | young 's people | Young_People_Fucking |
| 157. | turmoil | 13: [11, inf] | turmoil 's government | S._Venkitaramanan |
| 158. | iraq | 13: [27, 5.4], 27: [10, inf], 31: [50, 5.0] | iraq 's bush | George_W._Bush |
| 159. | challenged | 13: [16, inf], 16: [21, inf] | challenged function purl | Permalink |
| 160. | smallpox | 13: [10, inf] | smallpox health vaccine | Smallpox_vaccine |
| 161. | jews | 14: [17, 5.67], 22: [12, inf] | jews 's jewish | American_Jews |
| 162. | bethlehem | 14: [21, inf], 34: [13, 13.0] | bethlehem israeli palestinian | Bethlehem |
| 163. | abu | 14: [15, 7.5], 34: [12, inf], 38: [10, 10.0] | abu american philippines | Abu_Sayyaf |
| 164. | opponents | 14: [10, inf] | opponents 's government | Divided_government_in_the_United_States |
| 165. | church | 14: [34, 6.8], 28: [11, inf], 30: [10, inf], 43: [12, 6.0], 46: [17, inf] | church 's israeli | Church_of_Israel |
| 166. | streets | 14: [12, inf] | streets 's government | Federal_government_of_the_United_States |
| 167. | job | 14: [15, inf] | job 's photo | Steve_Jobs |
| 168. | statement | 14: [14, inf], 49: [12, inf] | statement 's says | Mission_statement |
| 169. | vehicles | 14: [12, inf] | vehicles israeli 's | Vehicle_registration_plates_of_Israel |
| 170. | crisis | 14: [21, 10.5], 20: [13, 13.0], 32: [10, inf] | crisis 's bush | Savings_and_loan_crisis |
| 171. | synagogue | 14: [10, inf] | synagogue tunisia attack | Ghriba_synagogue_bombing |
| 172. | gunmen | 14: [14, inf] | gunmen israeli palestinian | 2010_Palestinian_militancy_campaign |
| 173. | defendants | 14: [10, inf] | defendants trial court | Chicago_Seven |
| 174. | sweep | 14: [15, inf] | sweep israeli 's | Israel |
| 175. | northern | 14: [16, inf] | northern 's ireland | Northern_Ireland |
| 176. | union | 14: [14, inf], 33: [12, 12.0], 35: [24, 8.0], 40: [18, 9.0], 50: [50, 6.25] | union european 's | European_Union |
| 177. | put | 14: [13, inf] | put 's bush | George_H._W._Bush |
| 178. | parts | 14: [10, inf] | parts 's israeli | Israel |
| 179. | venezuela | 15: [35, inf] | venezuela chavez 's | Hugo_Chávez |
| 180. | company | 15: [12, 6.0], 38: [11, inf] | company 's oil | Shell_Oil_Company |
| 181. | hugo | 15: [15, inf] | hugo chavez venezuela | Hugo_Chávez |
| 182. | chavez | 15: [26, inf], 33: [12, inf] | chavez venezuela 's | Hugo_Chávez |
| 183. | business | 15: [17, inf], 37: [10, 10.0] | business 's function | Business_process |
| 184. | battle | 15: [14, inf], 21: [14, 14.0] | battle 's american | List_of_American_Civil_War_battles |
| 185. | sri | 15: [10, inf], 38: [10, inf] | sri lanka tamil | Sri_Lankan_Tamils |
| 186. | refugees | 15: [12, inf], 39: [14, 7.0], 50: [14, 7.0] | refugees 's north | North_Korean_defectors |
| 187. | bus | 15: [14, inf], 23: [10, inf], 25: [14, inf], 29: [17, inf], 41: [10, inf], 43: [20, inf] | bus israeli suicide | Dizengoff_Street_bus_bombing |
| 188. | dutch | 15: [10, inf], 19: [19, inf] | dutch netherlands fortuyn | Pim_Fortuyn |
| 189. | barakaat | 15: [10, inf] | barakaat 's somalia | Al-Barakat |
| 190. | coup | 16: [22, inf] | coup 's chavez | 1992_Venezuelan_coup_d'état_attempts |
| 191. | surrender | 16: [11, inf] | surrender 's says | Battle_of_Appomattox_Court_House |
| 192. | clear | 16: [11, 11.0], 21: [11, inf] | clear 's bush | George_H._W._Bush |
| 193. | died | 16: [17, 5.67], 44: [14, inf] | died 's say | Never_Say_Die! |
| 194. | votes | 16: [10, inf] | votes 's party | Party-line_vote |
| 195. | weather | 16: [26, inf] | weather function purl | Clear_Lake_(California) |
| 196. | greece | 16: [10, inf], 30: [12, 6.0] | greece europe world | Greece |
| 197. | settlement | 16: [12, inf], 29: [12, 6.0] | settlement israeli palestinian | 2010–11_Israeli–Palestinian_peace_talks |
| 198. | science | 16: [22, inf] | science function purl | Persistent_uniform_resource_locator |
| 199. | titl | 16: [21, inf], 36: [21, 7.0] | titl | G-Eazy |
| 200. | function | 16: [63, inf] | function purl features | Permalink |
| 201. | pop_me_up | 16: [21, inf] | pop_me_up function purl | Happy_Days |
| 202. | purl | 16: [42, inf] | purl function features | Permalink |
| 203. | new_window | 16: [21, inf] | new_window function purl | Happy_Days |
| 204. | window.open | 16: [21, inf] | window.open function purl | Office_Open_XML_file_formats |
| 205. | popup_window | 16: [21, inf] | popup_window function purl | EMPTY MATCHING |
| 206. | new_window.focus | 16: [21, inf] | new_window.focus function purl | Happy_Days |
| 207. | changeimage | 16: [21, inf] | changeimage function purl | EMPTY MATCHING |
| 208. | image_name | 16: [42, inf] | image_name function purl | Permalink |
| 209. | image_src | 16: [42, inf] | image_src function purl | EPUB |
| 210. | document.images | 16: [21, inf] | document.images function purl | Office_Open_XML_file_formats |
| 211. | .src | 16: [21, inf] | .src function purl | EPUB |
| 212. | mm_jumpmenu | 16: [21, inf] | mm_jumpmenu function purl | EMPTY MATCHING |
| 213. | targ | 16: [21, inf] | targ function purl | EMPTY MATCHING |
| 214. | selobj | 16: [21, inf] | selobj function purl | EMPTY MATCHING |
| 215. | restore | 16: [42, inf] | restore function purl | Persistent_uniform_resource_locator |
| 216. | //v.eval | 16: [21, inf] | //v.eval function purl | Bosnia_and_Herzegovina |
| 217. | targ+ | 16: [21, inf] | targ+ function purl | EMPTY MATCHING |
| 218. | .location= | 16: [21, inf] | .location= function purl | Persistent_uniform_resource_locator |
| 219. | +selobj.options | 16: [21, inf] | +selobj.options function purl | EMPTY MATCHING |
| 220. | selobj.selectedindex | 16: [21, inf] | selobj.selectedindex function purl | EMPTY MATCHING |
| 221. | .value+ | 16: [21, inf] | .value+ function purl | Persistent_uniform_resource_locator |
| 222. | selobj.selectedindex= | 16: [21, inf] | selobj.selectedindex= function purl | EMPTY MATCHING |
| 223. | // | 16: [21, inf] | // function purl | Permalink |
| 224. | technology | 16: [21, inf] | technology function purl | Persistent_uniform_resource_locator |
| 225. | education | 16: [21, inf] | education function purl | Charlotte_of_Mecklenburg-Strelitz |
| 226. | obituaries | 16: [21, inf] | obituaries function purl | Stanford_University |
| 227. | page | 16: [21, inf] | page function purl | Permalink |
| 228. | corrections | 16: [21, inf] | corrections function purl | Portugal |
| 229. | editorials/op-ed | 16: [21, inf] | editorials/op-ed function purl | EMPTY MATCHING |
| 230. | readers | 16: [21, inf] | readers function purl | EPUB |
| 231. | opinions | 16: [21, inf] | opinions function purl | Paolo_Sarpi |
| 232. | pen | 17: [52, 10.4], 23: [15, inf] | pen french chirac | 2002_French_presidential_election |
| 233. | local | 17: [18, inf], 20: [11, inf] | local 's officials | Official |
| 234. | pakistan | 17: [22, inf] | pakistan 's india | India–Pakistan_relations |
| 235. | argentine | 17: [15, inf] | argentine 's argentina | Argentina |
| 236. | argentina | 17: [12, inf] | argentina 's duhalde | Eduardo_Duhalde |
| 237. | eduardo | 17: [11, inf] | eduardo argentina duhalde | Eduardo_Duhalde |
| 238. | duhalde | 17: [16, inf] | duhalde argentina 's | Eduardo_Duhalde |
| 239. | immigration | 17: [15, 5.0], 25: [23, inf] | immigration 's immigrants | Illegal_immigration_to_the_United_States |
| 240. | success | 17: [11, inf] | success 's says | NXIVM |
| 241. | rightist | 17: [18, 9.0], 32: [14, inf] | rightist 's pen | Anti-Rightist_Campaign |
| 242. | chirac | 17: [22, 5.5], 29: [11, inf] | chirac france jacques | Jacques_Chirac |
| 243. | guilty | 17: [17, inf], 40: [10, inf] | guilty world briefing | Stephanie_Grisham |
| 244. | reporter | 17: [18, inf], 29: [11, 5.5] | reporter pearl 's | Daniel_Pearl |
| 245. | daniel | 17: [12, inf] | daniel pearl 's | Daniel_Pearl |
| 246. | viagra | 17: [10, inf] | viagra china shenzhen | 2013_Summer_Universiade |
| 247. | member | 17: [15, inf], 22: [10, 5.0] | member 's say | Say_Say_Say |
| 248. | free | 17: [13, 6.5], 38: [12, inf] | free 's says | Say's_law |
| 249. | suspended | 17: [10, inf] | suspended world briefing | Stephanie_Grisham |
| 250. | castro | 17: [14, inf] | castro cuba 's | Cuban_Revolution |
| 251. | fox | 17: [13, inf] | fox mexico 's | Vicente_Fox |
| 252. | crown | 17: [16, inf] | crown saudi bush | Abdullah_of_Saudi_Arabia |
| 253. | good | 17: [12, inf] | good 's photo | Google_Photos |
| 254. | evicted | 17: [12, inf] | evicted palestinians says | Palestinians |
| 255. | nepal | 17: [14, inf], 40: [15, inf] | nepal rebels asia | Nepalese_Civil_War |
| 256. | pakistani | 17: [11, 5.5], 31: [12, 6.0], 37: [10, 5.0], 44: [10, inf], 47: [10, 5.0] | pakistani pakistan 's | Pakistanis |
| 257. | shooting | 17: [10, inf] | shooting israeli 's | Stoneman_Douglas_High_School_shooting |
| 258. | n't | 18: [10, inf] | n't 's says | T.N.T._(album) |
| 259. | journalist | 18: [11, inf] | journalist 's pearl | Daniel_Pearl |
| 260. | research | 18: [10, inf] | research 's says | Say's_law |
| 261. | wins | 18: [10, inf] | wins 's party | WIN_Party |
| 262. | raffarin | 19: [10, inf] | raffarin chirac jean-pierre | Jean-Pierre_Raffarin |
| 263. | fortuyn | 19: [11, inf] | fortuyn dutch pim | Pim_Fortuyn |
| 264. | burma | 19: [10, inf] | burma government envoy | Saffron_Revolution |
| 265. | hamas | 19: [11, inf], 41: [13, inf] | hamas palestinian israeli | Hamas |
| 266. | asylum | 19: [10, inf], 36: [12, inf] | asylum north seekers | Asylum_seeker |
| 267. | session | 19: [14, inf] | session 's iraq | List_of_Congressional_opponents_of_the_Iraq_War |
| 268. | assembly | 19: [13, inf] | assembly 's government | Victoria_State_Government |
| 269. | carter | 20: [36, 6.0], 41: [15, inf], 50: [14, inf] | carter 's pres | Jay-Z |
| 270. | terrorist | 20: [16, inf], 25: [12, 12.0], 29: [12, 12.0], 41: [24, 12.0] | terrorist 's attacks | September_11_attacks |
| 271. | putin | 20: [12, 6.0], 34: [29, inf], 40: [22, 11.0], 43: [14, inf] | putin russia pres | Russian_interference_in_the_2016_United_States_elections |
| 272. | independent | 20: [11, inf] | independent 's says | Say's_law |
| 273. | prison | 20: [10, inf] | prison 's years | Prison |
| 274. | every | 20: [12, inf] | every 's government | Federal_government_of_the_United_States |
| 275. | basra | 20: [12, inf] | basra 's pakistan | Riaz_Basra |
| 276. | reform | 20: [13, inf] | reform 's palestinian | 2006_Palestinian_legislative_election |
| 277. | rape | 20: [10, inf] | rape 's charges | Mahmudiyah_rape_and_killings |
| 278. | medicine | 20: [10, inf] | medicine 's israeli | Healthcare_in_Israel |
| 279. | brazil | 20: [10, inf], 27: [10, 5.0], 48: [10, 10.0] | brazil 's world | Brazil_v_Germany_(2014_FIFA_World_Cup) |
| 280. | hair | 20: [13, inf] | hair 's schroder | Ricky_Schroder |
| 281. | weisfeiler | 20: [12, inf] | weisfeiler state 's | Boris_Weisfeiler |
| 282. | israelis | 21: [11, inf] | israelis israeli palestinian | Israeli–Palestinian_conflict |
| 283. | whaling | 21: [19, inf] | whaling japan commission | International_Whaling_Commission |
| 284. | offshore | 21: [10, inf] | offshore 's oil | Oil_platform |
| 285. | funds | 21: [16, 16.0], 38: [14, inf], 51: [15, 7.5] | funds 's government | Federal_government_of_the_United_States |
| 286. | percent | 22: [11, 5.5], 28: [13, inf], 32: [13, 13.0], 35: [10, 5.0] | percent 's government | Federal_government_of_the_United_States |
| 287. | full | 22: [11, inf] | full 's iraq | Occupation_of_Iraq_(2003–2011) |
| 288. | aimed | 22: [10, inf] | aimed 's government | Top_100_Contractors_of_the_U.S._federal_government |
| 289. | anti-semitism | 22: [10, inf] | anti-semitism jewish 's | Antisemitism |
| 290. | raids | 22: [10, inf] | raids israeli 's | 1968_Israeli_raid_on_Lebanon |
| 291. | official | 22: [13, inf], 33: [14, 7.0] | official 's says | Say_Say_Say |
| 292. | nablus | 22: [17, inf], 31: [14, inf] | nablus israeli palestinian | Nablus |
| 293. | week | 22: [13, inf], 27: [10, 5.0], 46: [11, 11.0] | week 's bush | George_H._W._Bush |
| 294. | point | 22: [13, inf] | point 's american | United_States |
| 295. | problem | 22: [10, inf] | problem 's says | Scunthorpe_problem |
| 296. | zimbabwe | 22: [12, inf], 37: [10, 5.0] | zimbabwe mugabe 's | Robert_Mugabe |
| 297. | efforts | 23: [11, 11.0], 25: [11, inf], 29: [11, 5.5] | efforts 's bush | Efforts_to_impeach_George_W._Bush |
| 298. | french | 23: [12, inf], 37: [10, 5.0], 41: [22, 7.33] | french france 's | France |
| 299. | guerrillas | 23: [12, 12.0], 43: [19, inf] | guerrillas 's rebels | Guerrilla_warfare |
| 300. | farm | 24: [10, inf] | farm 's subsidies | Agricultural_subsidy |
| 301. | bomb | 24: [16, 8.0], 36: [14, inf] | bomb 's israeli | Nuclear_weapons_and_Israel |
| 302. | suspect | 24: [13, inf], 27: [16, 5.33] | suspect 's police | Prime_Suspect |
| 303. | mandela | 24: [10, inf] | mandela africa south | Nelson_Mandela |
| 304. | ban | 24: [12, inf], 51: [12, inf] | ban 's world | Ban_Ki-moon |
| 305. | karzai | 24: [10, inf], 30: [10, 10.0] | karzai afghanistan afghan | Politics_of_Afghanistan |
| 306. | threats | 24: [11, inf] | threats 's iraq | Iraq_War |
| 307. | threat | 24: [11, 5.5], 32: [14, inf] | threat 's iraq | Iraq_War |
| 308. | plant | 24: [12, inf], 48: [14, inf], 52: [14, 7.0] | plant nuclear 's | Chernobyl_Nuclear_Power_Plant |
| 309. | mexico | 25: [11, inf], 31: [19, inf], 33: [13, 6.5], 41: [10, 5.0], 48: [23, inf] | mexico 's mexican | Crime_in_Mexico |
| 310. | prosecution | 25: [11, inf] | prosecution court 's | Prosecutor |
| 311. | legal | 25: [10, inf] | legal 's court | Court_dress |
| 312. | land | 25: [13, 6.5], 27: [15, inf] | land 's israeli | Land_of_Israel |
| 313. | ouster | 26: [14, inf] | ouster 's bush | Cori_Bush |
| 314. | violence | 26: [11, inf] | violence 's israeli | Israeli_settler_violence |
| 315. | chile | 26: [10, inf] | chile 's trade | Economy_of_Chile |
| 316. | suit | 26: [10, inf] | suit 's american | Suit |
| 317. | starts | 26: [10, inf] | starts 's world | The_World_Starts_Tonight |
| 318. | removal | 26: [11, inf] | removal 's bush | George_W._Bush |
| 319. | secret | 27: [12, inf] | secret 's nuclear | Nuclear_Secrets |
| 320. | peacekeeping | 27: [12, inf] | peacekeeping force 's | United_Nations_peacekeeping |
| 321. | code | 27: [10, inf] | code 's legal | Philippine_legal_codes |
| 322. | czech | 27: [10, inf], 33: [10, inf], 43: [17, 17.0] | czech republic europe | Czech_Republic |
| 323. | republic | 27: [12, inf], 43: [10, 10.0] | republic 's czech | Czech_Republic |
| 324. | settlements | 27: [10, inf] | settlements israeli says | Israeli_settlement |
| 325. | flight | 27: [11, inf], 35: [11, inf] | flight say air | Lion_Air_Flight_610 |
| 326. | paid | 27: [11, inf] | paid 's says | Say's_law |
| 327. | collision | 27: [19, inf] | collision crash air | Mid-air_collision |
| 328. | aids | 27: [20, 20.0], 46: [11, inf] | aids 's africa | HIV/AIDS_in_Africa |
| 329. | africa | 27: [12, inf], 46: [29, 5.8] | africa world 's | South_Africa |
| 330. | conviction | 28: [12, inf] | conviction 's court | Conviction |
| 331. | soon | 28: [16, inf] | soon 's says | Say_This_Sooner |
| 332. | marijuana | 28: [10, inf] | marijuana 's use | Cannabis_use_disorder |
| 333. | factory | 29: [11, inf] | factory 's workers | Workers'_self-management |
| 334. | month | 29: [11, inf] | month 's last | The_Last_Month_of_the_Year |
| 335. | call | 29: [11, inf], 43: [11, inf] | call 's bush | George_H._W._Bush |
| 336. | kill | 29: [10, inf] | kill israeli palestinian | Timeline_of_the_Israeli–Palestinian_conflict |
| 337. | different | 29: [10, inf] | different 's bush | Bush_family |
| 338. | growing | 29: [12, inf], 34: [11, 5.5], 39: [10, 10.0] | growing 's bush | George_H._W._Bush |
| 339. | suspects | 29: [12, inf] | suspects 's qaeda | Al-Qaeda |
| 340. | ambush | 29: [11, inf] | ambush israeli killed | Ansariya_ambush |
| 341. | agreement | 30: [13, inf] | agreement 's north | North_American_Free_Trade_Agreement |
| 342. | shehada | 30: [11, inf] | shehada hamas israeli | Hamas |
| 343. | menem | 30: [21, inf] | menem argentina pres | Argentina |
| 344. | taliban | 30: [10, inf], 41: [11, inf], 44: [16, 8.0] | taliban afghanistan qaeda | Taliban_insurgency |
| 345. | cease-fire | 30: [11, inf] | cease-fire israeli israel | Yom_Kippur_War |
| 346. | cafeteria | 31: [12, inf] | cafeteria bomb jerusalem | Propane_bomb |
| 347. | university | 31: [24, inf] | university 's students | Queen's_University_at_Kingston |
| 348. | japanese | 31: [12, inf] | japanese japan north | Japan |
| 349. | rejects | 31: [13, inf], 35: [11, inf], 44: [10, inf] | rejects 's pres | Pre-existence |
| 350. | invasion | 31: [10, inf] | invasion iraq 's | 2003_invasion_of_Iraq |
| 351. | campus | 31: [10, inf] | campus students attack | 2020_Jawaharlal_Nehru_University_attack |
| 352. | bombers | 32: [12, inf] | bombers israeli palestinian | Use_of_child_suicide_bombers_by_Palestinian_militant_groups |
| 353. | christian | 32: [18, inf], 39: [12, inf], 41: [13, 6.5] | christian 's church | Christian_Church |
| 354. | loan | 32: [10, inf] | loan 's billion | Savings_and_loan_crisis |
| 355. | money | 32: [12, inf] | money 's government | Fiat_money |
| 356. | web | 32: [10, inf] | web 's px | 500px |
| 357. | historic | 33: [10, inf] | historic 's photos | Donald_Trump_photo_op_at_St._John's_Church |
| 358. | prague | 33: [21, inf], 43: [16, 5.33] | prague nato czech | Prague |
| 359. | floods | 33: [14, inf] | floods europe 's | 2002_European_floods |
| 360. | georgian | 33: [10, inf] | georgian georgia russia | Russo-Georgian_War |
| 361. | timor | 33: [13, inf] | timor east indonesia | Indonesian_invasion_of_East_Timor |
| 362. | pope | 33: [23, inf] | pope john paul | Pope_John_Paul_II |
| 363. | john | 33: [14, inf] | john pope 's | Pope_John_Paul_II |
| 364. | suarez | 33: [10, inf] | suarez united mexico | Cecilia_Suárez |
| 365. | dresden | 33: [11, inf] | dresden floods germany | Dresden |
| 366. | nidal | 34: [11, inf] | nidal abu palestinian | Abu_Nidal |
| 367. | vladimir | 34: [20, 5.0], 40: [16, 8.0], 43: [11, inf] | vladimir putin russia | Russia_under_Vladimir_Putin |
| 368. | moscow | 34: [25, inf], 43: [30, 6.0] | moscow 's russia | Moscow |
| 369. | parliament | 34: [10, inf] | parliament 's world | Parliament_of_the_World's_Religions |
| 370. | apartment | 34: [10, inf] | apartment 's say | The_Apartment |
| 371. | embassy | 34: [11, inf] | embassy american north | List_of_diplomatic_missions_of_the_United_States |
| 372. | johannesburg | 35: [19, inf] | johannesburg world summit | Earth_Summit_2002 |
| 373. | sustainable | 35: [15, inf] | sustainable world summit | World_Sustainable_Development_Summit |
| 374. | trying | 35: [14, inf] | trying 's says | The_Try_Guys |
| 375. | already | 35: [13, inf] | already 's say | It's_Already_Written |
| 376. | dispute | 35: [11, inf], 45: [10, 5.0] | dispute 's united | China–United_States_trade_war |
| 377. | approval | 35: [10, inf] | approval 's iraq | British_Parliamentary_approval_for_the_invasion_of_Iraq |
| 378. | energy | 35: [10, inf], 52: [11, inf] | energy nuclear north | Nuclear_power |
| 379. | allies | 35: [13, inf] | allies 's bush | George_H._W._Bush |
| 380. | psychiatric | 35: [10, inf] | psychiatric hospital china | Psychiatric_hospital |
| 381. | visa | 35: [10, inf] | visa europe russia | Visa_policy_of_Russia |
| 382. | ireland | 36: [22, inf] | ireland northern europe | Northern_Europe |
| 383. | immigrants | 36: [10, 5.0], 38: [12, 12.0], 49: [10, inf] | immigrants 's europe | Immigration_to_Europe |
| 384. | september | 37: [18, inf] | september attacks us | September_11_attacks |
| 385. | level | 37: [12, inf] | level 's united | Cabinet_of_the_United_States |
| 386. | equipment | 37: [11, inf], 49: [11, 5.5] | equipment 's iraq | List_of_current_equipment_of_the_Iraqi_Army |
| 387. | resolutions | 37: [14, inf], 44: [10, 5.0] | resolutions iraq bush | Authorization_for_Use_of_Military_Force_Against_Iraq_Resolution_of_2002 |
| 388. | al-shibh | 37: [11, inf] | al-shibh qaeda officials | Ramzi_bin_al-Shibh |
| 389. | bavaria | 37: [10, inf] | bavaria 's stoiber | Edmund_Stoiber |
| 390. | investigators | 37: [13, inf] | investigators 's american | Special_Counsel_investigation_(2017–2019) |
| 391. | karachi | 37: [16, 16.0], 44: [18, inf] | karachi pearl pakistan | Pearl-Continental_Hotels_&_Resorts |
| 392. | jordan | 37: [10, 10.0], 44: [19, inf] | jordan israel 's | Israel–Jordan_relations |
| 393. | population | 38: [10, inf] | population 's world | World_population |
| 394. | release | 38: [15, inf] | release 's arafat | Yasser_Arafat |
| 395. | maya | 38: [10, inf] | maya mexico palenque | Palenque |
| 396. | coffee | 38: [10, inf] | coffee day 's | Café_Coffee_Day |
| 397. | papon | 38: [16, inf] | papon release french | Maurice_Papon |
| 398. | hedge | 38: [10, inf] | hedge funds fund | Hedge_fund |
| 399. | foreigners | 39: [13, inf] | foreigners 's foreign | Xenophobia |
| 400. | ivory | 39: [15, inf] | ivory coast africa | Ivory_Coast |
| 401. | trapped | 39: [10, inf] | trapped israeli troops | Yom_Kippur_War |
| 402. | radar | 39: [12, inf] | radar iraq american | American-led_intervention_in_Iraq_(2014–present) |
| 403. | complex | 39: [12, inf] | complex 's north | North_Complex_fire |
| 404. | draft | 39: [12, inf] | draft iraq 's | Iraq_War |
| 405. | hezbollah | 39: [12, inf] | hezbollah israeli israel | Iran–Israel_proxy_conflict |
| 406. | dostum | 39: [10, inf] | dostum prisoners taliban | Abdul_Rashid_Dostum |
| 407. | delay | 40: [12, inf], 49: [10, 5.0] | delay 's bush | George_W._Bush |
| 408. | ira | 40: [12, inf] | ira ireland northern | Provisional_Irish_Republican_Army |
| 409. | kurdish | 40: [10, inf] | kurdish iraq kurds | Kurds_in_Iraq |
| 410. | philippines | 40: [15, inf] | philippines american abu | Abu_Sayyaf |
| 411. | kurds | 40: [16, inf] | kurds iraq iraqi | Iraqi_Kurdistan |
| 412. | spending | 40: [10, inf] | spending 's government | Government_spending |
| 413. | sinn | 40: [13, inf] | sinn fein ireland | Sinn_Féin |
| 414. | fein | 40: [13, inf] | fein sinn ireland | Sinn_Féin |
| 415. | king | 40: [15, inf] | king 's former | Angus_King |
| 416. | deuba | 40: [11, inf] | deuba nepal rebels | Sher_Bahadur_Deuba |
| 417. | tanker | 41: [14, inf] | tanker oil spain | Prestige_oil_spill |
| 418. | blast | 41: [10, inf], 45: [11, 11.0] | blast israeli 's | Iran–Israel_proxy_conflict |
| 419. | sentences | 41: [12, inf] | sentences court years | Suspended_sentence |
| 420. | indonesia | 41: [10, inf], 45: [13, inf], 47: [12, 6.0] | indonesia 's indonesian | Indonesia |
| 421. | kuwaiti | 41: [10, inf], 47: [11, 5.5] | kuwaiti kuwait american | Demographics_of_Kuwait |
| 422. | kuwait | 41: [18, inf] | kuwait iraq 's | Invasion_of_Kuwait |
| 423. | nobel | 41: [15, inf] | nobel prize carter | Nobel_Prize |
| 424. | prize | 41: [15, inf], 50: [10, inf] | prize carter nobel | Nobel_Prize |
| 425. | committee | 41: [12, inf], 46: [14, 14.0] | committee 's says | United_States_congressional_committee |
| 426. | pinocchio | 41: [16, inf] | pinocchio italians rome | The_Adventures_of_Pinocchio |
| 427. | warnings | 42: [10, inf], 46: [12, inf] | warnings 's say | Miranda_warning |
| 428. | heavy | 42: [10, inf] | heavy 's israeli | Nuclear_weapons_and_Israel |
| 429. | iraqis | 42: [13, inf], 49: [21, 5.25] | iraqis iraq hussein | Saddam_Hussein_and_al-Qaeda_link_allegations |
| 430. | jemaah | 42: [10, inf] | jemaah indonesian islamiyah | Christmas_Eve_2000_Indonesia_bombings |
| 431. | gerdt | 42: [11, inf] | gerdt bombing including | Myyrmanni_bombing |
| 432. | claim | 43: [10, inf] | claim 's government | Federal_government_of_the_United_States |
| 433. | mohamed | 43: [13, inf] | mohamed sept say | Mohamed_Atta |
| 434. | atta | 43: [13, inf] | atta sept attacks | September_11_attacks |
| 435. | havel | 43: [10, inf] | havel czech pres | Václav_Havel |
| 436. | prisons | 43: [14, inf] | prisons prisoners 's | Prisoner_security_categories_in_the_United_Kingdom |
| 437. | cities | 43: [11, inf] | cities 's israeli | List_of_cities_in_Israel |
| 438. | get | 43: [10, inf] | get 's photo | Google_Photos |
| 439. | theater | 43: [33, inf] | theater moscow chechen | Moscow_theater_hostage_crisis |
| 440. | formally | 43: [12, inf] | formally 's iraq | 2003_invasion_of_Iraq |
| 441. | hostages | 43: [26, inf] | hostages moscow theater | Moscow_theater_hostage_crisis |
| 442. | bedouin | 43: [11, inf] | bedouin israel israeli | Negev_Bedouin |
| 443. | silva | 44: [12, inf] | silva brazil 's | Thiago_Silva |
| 444. | foley | 44: [11, inf] | foley jordan american | Jordan_Foley |
| 445. | extremists | 44: [10, inf] | extremists 's pakistan | Tehreek-e-Labbaik_Pakistan |
| 446. | issues | 44: [15, inf] | issues 's bush | Prescott_Bush |
| 447. | girls | 44: [18, inf], 47: [16, 16.0] | girls 's two | 2_Girls_1_Cup |
| 448. | denmark | 44: [10, inf] | denmark chechen 's | Chechens |
| 449. | zakayev | 44: [12, inf] | zakayev chechen russia | Akhmed_Zakayev |
| 450. | danish | 44: [10, inf] | danish chechen zakayev | Akhmed_Zakayev |
| 451. | bombings | 44: [12, inf] | bombings palestinian israel | List_of_Palestinian_suicide_attacks |
| 452. | water | 44: [18, 9.0], 50: [15, inf] | water 's united | Water_fluoridation_in_the_United_States |
| 453. | appeals | 45: [11, inf] | appeals 's court | United_States_courts_of_appeals |
| 454. | catfish | 45: [12, inf] | catfish vietnamese fish | Basa_(fish) |
| 455. | spy | 45: [15, inf] | spy 's intelligence | Espionage |
| 456. | cod | 45: [10, inf] | cod fishing north | Atlantic_cod |
| 457. | voice | 46: [13, inf] | voice 's government | Indigenous_voice_to_government |
| 458. | gates | 46: [10, inf] | gates north asylum | Gladesville_Mental_Hospital |
| 459. | foundation | 46: [10, inf] | foundation 's india | American_India_Foundation |
| 460. | migrants | 46: [12, inf] | migrants 's north | European_migrant_crisis |
| 461. | kibbutz | 46: [10, inf] | kibbutz israeli palestinian | 1948_Arab–Israeli_War |
| 462. | setback | 46: [10, inf] | setback 's government | Setback_(land_use) |
| 463. | cyprus | 46: [10, inf] | cyprus europe union | Northern_Cyprus_and_the_European_Union |
| 464. | apartheid | 46: [11, inf] | apartheid africa south | Apartheid |
| 465. | chechnya | 46: [19, inf], 50: [10, 5.0] | chechnya russian russia | Chechnya |
| 466. | students | 46: [16, inf] | students 's school | Student |
| 467. | tape | 46: [18, inf] | tape laden 's | Videos_and_audio_recordings_of_Osama_bin_Laden |
| 468. | supporters | 46: [10, inf] | supporters 's government | Government_shutdowns_in_the_United_States |
| 469. | chancellor | 46: [10, inf] | chancellor 's schroder | Gerhard_Schröder |
| 470. | coast | 46: [11, inf] | coast 's oil | Gulf_Coast_of_the_United_States |
| 471. | fuel | 47: [18, 18.0], 50: [10, 5.0], 52: [13, inf] | fuel north nuclear | North_Korea_and_weapons_of_mass_destruction |
| 472. | g.i | 47: [14, inf] | g.i 's american | G.I._Joe |
| 473. | sergeant | 47: [14, inf] | sergeant korea army | Republic_of_Korea_Army |
| 474. | vehicle | 47: [11, inf] | vehicle israeli two | Vehicle_registration_plates_of_Israel |
| 475. | fail | 47: [10, inf] | fail 's bush | George_W._Bush |
| 476. | andreotti | 47: [12, inf] | andreotti italy prime | Giulio_Andreotti |
| 477. | petersburg | 47: [10, inf] | petersburg bush putin | Vladimir_Putin |
| 478. | berlin | 47: [10, inf] | berlin germany 's | Berlin |
| 479. | deaths | 47: [12, inf] | deaths 's military | United_States_military_casualties_of_war |
| 480. | athomeabroad | 47: [18, inf] | athomeabroad culture 's | EMPTY MATCHING |
| 481. | detention | 48: [11, inf] | detention 's government | Indefinite_detention |
| 482. | infected | 48: [10, inf] | infected aids 's | HIV/AIDS |
| 483. | ford | 48: [14, inf] | ford 's argentina | Ford_Motor_Argentina |
| 484. | missiles | 48: [13, inf] | missiles 's israeli | Arrow_(Israeli_missile) |
| 485. | israeli-owned | 48: [13, inf] | israeli-owned kenya israeli | Israel–Kenya_relations |
| 486. | mombasa | 48: [19, inf] | mombasa kenya israeli | 2002_Mombasa_attacks |
| 487. | target | 48: [10, inf] | target 's israeli | Targeted_killings_by_Israel_Defense_Forces |
| 488. | kenyans | 48: [13, inf] | kenyans kenya qaeda | Timeline_of_Kenya |
| 489. | amber | 48: [12, inf] | amber world miners | 2015–16_ISU_World_Standings |
| 490. | scientists | 49: [12, inf] | scientists 's iraq | Iran–Iraq_War |
| 491. | afghans | 49: [10, inf] | afghans afghanistan afghan | Women_in_Afghanistan |
| 492. | luxury | 49: [14, inf] | luxury 's fashion | Italian_fashion |
| 493. | palace | 49: [11, inf] | palace 's royal | St_James's_Palace |
| 494. | asks | 49: [14, inf] | asks 's iraq | Iraq |
| 495. | warns | 50: [13, inf] | warns 's bush | George_H._W._Bush |
| 496. | rivers | 50: [10, inf] | rivers water 's | List_of_water_deities |
| 497. | negotiations | 50: [10, inf] | negotiations 's bush | George_H._W._Bush |
| 498. | norway | 51: [13, inf] | norway world 's | German_occupation_of_Norway |
| 499. | wall | 51: [10, inf] | wall pearl 's | Daniel_Pearl |
| 500. | radio | 51: [12, inf] | radio 's says | Say_Say_Say |
| 501. | neighbors | 52: [10, inf] | neighbors 's photo | America's_Next_Top_Model_(season_20) |
| 502. | plutonium | 52: [15, inf] | plutonium north korea | North_Korea_and_weapons_of_mass_destruction |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | world | 6: [14, 7.0], 10: [11, inf] | world brief 's | World_Prison_Brief |
| 2. | guide | 6: [10, inf] | guide world news | News_of_the_World_(film) |
| 3. | pen | 17: [17, inf] | pen 's chirac | Jacques_Chirac |
