# Keywords with the highest 'interestingness' in 2004

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
| 1. | region | 2: [23, inf], 11: [12, 12.0], 22: [17, 8.5] | region 's sudan | South_Sudan |
| 2. | forces | 2: [15, inf], 15: [44, 6.29], 39: [11, 5.5] | forces 's american | American_Forces_Network |
| 3. | even | 2: [10, inf], 9: [18, 18.0], 49: [11, 11.0] | even 's iraq | Iraq_War |
| 4. | foreign | 2: [22, inf] | foreign 's iraq | Foreign_hostages_in_Iraq |
| 5. | taliban | 2: [21, inf], 8: [10, 5.0], 23: [14, inf], 41: [12, inf] | taliban afghanistan afghan | War_in_Afghanistan_(2001–present) |
| 6. | seen | 2: [12, 12.0], 49: [11, inf] | seen 's government | Divided_government_in_the_United_States |
| 7. | cats | 2: [11, inf] | cats sars civet | Asian_palm_civet |
| 8. | found | 2: [11, inf] | found 's iraq | Iraq_War |
| 9. | harvard | 2: [10, inf] | harvard bells 's | Harvard_of_the_South_(band) |
| 10. | bells | 2: [12, inf] | bells harvard 's | Harvard_of_the_South_(band) |
| 11. | civet | 2: [13, inf] | civet sars china | SARS_conspiracy_theory |
| 12. | west | 2: [12, inf], 16: [28, 14.0], 22: [16, 8.0] | west 's bank | West_Bank |
| 13. | secretary | 2: [12, inf], 4: [10, 5.0], 26: [10, 5.0] | secretary 's iraq | 2003_invasion_of_Iraq |
| 14. | european | 2: [25, inf] | european 's union | European_Union |
| 15. | georgia | 2: [20, inf], 15: [14, 7.0], 32: [11, inf] | georgia world saakashvili | Mikheil_Saakashvili |
| 16. | saakashvili | 2: [11, inf] | saakashvili georgia mikhail | Mikheil_Saakashvili |
| 17. | deal | 2: [12, inf], 35: [10, inf] | deal 's iraqi | Iraq |
| 18. | europe | 2: [32, inf] | europe world briefing | BBC_World_News |
| 19. | schools | 2: [10, inf] | schools 's public | Public_school_(United_Kingdom) |
| 20. | general | 2: [16, inf], 24: [15, 15.0], 35: [13, 6.5], 49: [11, 11.0] | general 's iraq | Iraq_War |
| 21. | jewish | 2: [10, 10.0], 30: [10, 10.0], 33: [10, inf] | jewish gaza israeli | Israeli_disengagement_from_Gaza |
| 22. | powell | 2: [11, inf], 12: [23, 11.5], 26: [13, 13.0] | powell colin state | Colin_Powell |
| 23. | africa | 2: [11, inf] | africa world 's | South_Africa |
| 24. | occupation | 2: [11, inf], 19: [10, 10.0], 21: [17, 5.67], 27: [14, inf] | occupation iraq american | Occupation_of_Iraq_(2003–2011) |
| 25. | proposed | 2: [10, inf] | proposed 's government | List_of_proposed_amendments_to_the_United_States_Constitution |
| 26. | mexico | 2: [14, 7.0], 19: [10, 10.0], 28: [11, 11.0], 36: [10, 10.0], 44: [12, inf], 48: [11, inf] | mexico 's mexican | Crime_in_Mexico |
| 27. | eggs | 2: [10, inf] | eggs world 's | World_egg |
| 28. | putin | 2: [10, 5.0], 30: [10, inf], 47: [10, 5.0] | putin 's russia | Russia_under_Vladimir_Putin |
| 29. | without | 3: [15, 5.0], 14: [19, inf] | without 's government | Federal_government_of_the_United_States |
| 30. | swedish | 3: [12, inf] | swedish minister foreign | Minister_for_Foreign_Affairs_(Sweden) |
| 31. | woman | 3: [12, inf] | woman 's two | Two-Faced_Woman |
| 32. | parmalat | 3: [12, inf] | parmalat italian tanzi | Parmalat |
| 33. | companies | 3: [12, 12.0], 33: [10, inf] | companies 's iraq | Iraq_Petroleum_Company |
| 34. | large | 3: [11, 5.5], 15: [10, 5.0], 36: [10, inf] | large 's american | List_of_U.S._cities_with_large_African-American_populations |
| 35. | fox | 3: [12, inf], 50: [11, inf] | fox mexico 's | Vicente_Fox |
| 36. | known | 3: [12, inf] | known 's iraq | There_are_known_knowns |
| 37. | bomber | 3: [11, 5.5], 5: [19, inf] | bomber suicide israeli | Use_of_child_suicide_bombers_by_Palestinian_militant_groups |
| 38. | gaza | 3: [20, inf], 9: [10, 5.0], 12: [26, 5.2], 16: [33, 33.0] | gaza israeli palestinian | Gaza–Israel_conflict |
| 39. | israelis | 3: [10, 10.0], 40: [12, 6.0], 47: [11, inf] | israelis israeli palestinians | Israeli–Palestinian_conflict |
| 40. | aids | 3: [10, 10.0], 7: [18, inf], 20: [12, 6.0] | aids africa drugs | HIV/AIDS_denialism |
| 41. | hamas | 3: [11, inf], 13: [41, 20.5], 17: [27, 6.75], 39: [15, 7.5], 47: [11, 5.5] | hamas israeli israel | Gaza–Israel_conflict |
| 42. | bremer | 3: [10, 10.0], 17: [14, 14.0], 27: [10, inf] | bremer american iraq | Paul_Bremer |
| 43. | sudan | 3: [12, 6.0], 19: [13, 6.5], 26: [18, inf], 30: [23, 5.75], 44: [13, inf], 52: [10, inf] | sudan darfur government | War_in_Darfur |
| 44. | japan | 3: [11, inf], 12: [10, 5.0], 20: [10, inf], 42: [12, 12.0] | japan 's japanese | Japan |
| 45. | hicks | 4: [10, inf] | hicks australian guantanamo | David_Hicks |
| 46. | khan | 4: [10, 5.0], 32: [10, inf] | khan nuclear 's | Abdul_Qadeer_Khan |
| 47. | father | 4: [10, inf] | father 's israeli | Law_of_Return |
| 48. | infected | 4: [11, inf] | infected aids people | List_of_countries_by_HIV/AIDS_adult_prevalence_rate |
| 49. | hezbollah | 4: [18, inf] | hezbollah israeli israel | 2006_Lebanon_War |
| 50. | missile | 4: [12, inf], 10: [10, inf] | missile israeli 's | Arrow_(Israeli_missile) |
| 51. | lebanon | 4: [12, inf] | lebanon hezbollah syria | Hezbollah |
| 52. | vatican | 4: [14, inf], 26: [10, 5.0] | vatican pope john | Pope_John_Paul_I_conspiracy_theories |
| 53. | pope | 4: [12, inf] | pope john paul | Pope_John_Paul_II |
| 54. | john | 4: [13, 6.5], 10: [12, inf], 14: [11, 5.5], 29: [12, 6.0] | john iraq 's | Iraq_War |
| 55. | movie | 4: [10, inf] | movie 's vatican | The_Vatican_Tapes |
| 56. | economic | 4: [24, 6.0], 6: [10, inf], 49: [11, 5.5] | economic 's government | Chief_Economic_Advisor_to_the_Government_of_India |
| 57. | paramilitary | 4: [10, inf] | paramilitary colombia 's | Right-wing_paramilitarism_in_Colombia |
| 58. | scientists | 4: [11, inf], 10: [11, inf] | scientists 's nuclear | Assassination_of_Iranian_nuclear_scientists |
| 59. | davos | 4: [30, inf] | davos forum economic | World_Economic_Forum |
| 60. | forum | 4: [24, inf] | forum davos world | World_Economic_Forum |
| 61. | food | 4: [10, inf], 14: [13, 6.5] | food 's united | Food_and_Drug_Administration |
| 62. | virus | 4: [18, inf] | virus health spread | 2015–2016_Zika_virus_epidemic |
| 63. | thailand | 4: [10, 5.0], 40: [16, inf] | thailand avian flu | Avian_influenza |
| 64. | cheney | 4: [13, 6.5], 16: [23, inf], 25: [21, 21.0] | cheney 's pres | Liz_Cheney |
| 65. | mugabe | 4: [12, inf] | mugabe zimbabwe 's | Robert_Mugabe |
| 66. | lebanese | 5: [11, inf] | lebanese hezbollah lebanon | 2006_Lebanon_War |
| 67. | white | 5: [18, 18.0], 12: [11, 11.0], 28: [10, 10.0], 32: [11, inf], 42: [10, inf] | white bush 's | George_W._Bush |
| 68. | image | 5: [10, inf] | image 's photo | Photo_manipulation |
| 69. | blair | 5: [29, 5.8], 9: [11, 5.5], 13: [11, 5.5], 28: [10, inf], 40: [22, 7.33] | blair prime tony | Tony_Blair |
| 70. | scientist | 5: [12, 6.0], 22: [10, inf] | scientist nuclear 's | Assassination_of_Iranian_nuclear_scientists |
| 71. | guerrilla | 5: [11, inf] | guerrilla 's group | People's_Guerrilla_Group |
| 72. | taiwan | 5: [15, inf], 12: [12, inf], 37: [10, inf], 50: [12, inf], 53: [12, inf] | taiwan china 's | Taiwan,_China |
| 73. | sec | 5: [17, 8.5], 12: [18, 6.0], 19: [20, inf] | sec iraq says | Iraq_War |
| 74. | chirac | 5: [14, 7.0], 23: [19, inf] | chirac france jacques | Jacques_Chirac |
| 75. | resigns | 5: [11, inf] | resigns 's minister | Union_Council_of_Ministers |
| 76. | network | 5: [10, inf], 25: [11, inf] | network 's nuclear | Nuclear_weapons_of_the_United_States |
| 77. | gilligan | 5: [10, inf] | gilligan bbc 's | Mo_Gilligan |
| 78. | jerusalem | 5: [12, inf], 9: [10, 10.0] | jerusalem israeli palestinian | East_Jerusalem |
| 79. | bus | 5: [10, inf], 51: [13, inf] | bus attack bomb | 2012_Burgas_bus_bombing |
| 80. | expert | 5: [10, inf] | expert 's khan | Jiah_Khan |
| 81. | settlers | 6: [14, inf], 38: [14, 7.0], 42: [12, inf] | settlers gaza sharon | Israeli_disengagement_from_Gaza |
| 82. | strip | 6: [11, inf], 16: [11, 11.0], 20: [15, 5.0] | strip gaza israeli | Gaza_War_(2008–2009) |
| 83. | musharraf | 6: [21, 7.0], 22: [10, inf] | musharraf pakistan pakistani | Pervez_Musharraf |
| 84. | groups | 6: [16, 8.0], 15: [12, 6.0], 18: [10, 10.0], 41: [13, inf] | groups 's government | Federal_government_of_the_United_States |
| 85. | panel | 6: [14, 14.0], 25: [11, inf], 30: [21, 5.25], 35: [21, inf] | panel 's intelligence | Robertson_Panel |
| 86. | injured | 6: [10, inf] | injured people killed | Killed_or_Seriously_Injured |
| 87. | run | 6: [10, inf] | run 's iraq | Iraq |
| 88. | spain | 6: [20, 6.67], 11: [27, inf] | spain 's spanish | Spain |
| 89. | cities | 6: [11, inf], 15: [25, 25.0], 19: [16, 16.0] | cities 's american | List_of_U.S._cities_with_large_African-American_populations |
| 90. | terror | 6: [10, inf], 32: [22, 5.5] | terror 's attacks | 2008_Mumbai_attacks |
| 91. | liberia | 6: [10, inf] | liberia million united | Liberia–United_States_relations |
| 92. | rumsfeld | 6: [14, 7.0], 9: [10, inf], 19: [41, inf], 33: [16, 8.0] | rumsfeld iraq defense | Donald_Rumsfeld |
| 93. | tenet | 6: [10, 5.0], 23: [25, inf], 28: [11, inf] | tenet intelligence 's | George_Tenet |
| 94. | subway | 6: [12, inf], 36: [10, inf] | subway moscow bombing | 2010_Moscow_Metro_bombings |
| 95. | raid | 7: [14, 7.0], 21: [21, 5.25], 26: [11, inf], 46: [10, inf] | raid israeli 's | Raid_on_Entebbe_(film) |
| 96. | months | 7: [13, inf] | months 's iraq | 2003_invasion_of_Iraq |
| 97. | militias | 7: [13, inf] | militias sudan government | Slavery_in_Sudan |
| 98. | barrier | 7: [10, 5.0], 27: [24, inf] | barrier israel west | Israeli_West_Bank_barrier |
| 99. | faces | 7: [10, 10.0], 44: [12, inf] | faces 's iraq | Iran–Iraq_War |
| 100. | rybkin | 7: [14, inf] | rybkin 's putin | Ivan_Rybkin |
| 101. | station | 7: [10, inf] | station police iraqi | Iraqi_Police |
| 102. | haitian | 7: [12, inf] | haitian aristide haiti | Haiti |
| 103. | aristide | 7: [24, inf] | aristide haiti 's | Jean-Bertrand_Aristide |
| 104. | candidate | 7: [10, inf], 22: [11, 5.5] | candidate 's election | Perennial_candidate |
| 105. | middle | 7: [10, 5.0], 26: [11, inf] | middle east 's | Middle_East |
| 106. | centrifuge | 7: [10, inf] | centrifuge nuclear iran | Iran_nuclear_deal_framework |
| 107. | haiti | 8: [21, 7.0], 14: [14, 7.0], 22: [11, inf], 43: [11, 11.0] | haiti aristide 's | Jean-Bertrand_Aristide |
| 108. | zimbabwe | 9: [20, 10.0], 11: [10, 5.0], 41: [12, 6.0], 44: [14, inf] | zimbabwe 's africa | Zimbabweans_in_South_Africa |
| 109. | stele | 9: [10, inf] | stele antiquities egypt | Merneptah_Stele |
| 110. | agents | 9: [10, inf], 33: [10, 10.0] | agents 's american | U.S._Agent |
| 111. | hearing | 9: [18, inf] | hearing 's court | Hearing_(law) |
| 112. | land | 9: [16, inf] | land 's government | Federal_government_of_the_United_States |
| 113. | mines | 9: [10, inf] | mines land bombs | Land_mine |
| 114. | nato | 9: [10, inf], 14: [14, 14.0], 21: [14, inf], 26: [27, 6.75] | nato iraq 's | NATO_Training_Mission_–_Iraq |
| 115. | fashion | 9: [15, 7.5], 27: [12, inf] | fashion 's paris— | Paris_Fashion_Week |
| 116. | short | 9: [13, inf] | short 's says | Say's_law |
| 117. | space | 9: [12, inf] | space 's world | Space_World |
| 118. | port-au-prince | 9: [11, inf] | port-au-prince aristide haiti | Port-au-Prince |
| 119. | protest | 9: [11, 5.5], 35: [12, inf] | protest 's government | Protest |
| 120. | qatar | 9: [10, inf] | qatar russian 's | Qatar–Russia_relations |
| 121. | province | 10: [13, inf], 29: [13, inf] | province 's killed | Islamic_State_of_Iraq_and_the_Levant_–_Khorasan_Province |
| 122. | week | 10: [10, inf], 51: [13, 6.5] | week 's iraq | Iraq_War |
| 123. | coalition | 10: [14, inf], 33: [10, 5.0] | coalition 's party | National_Coalition_Party |
| 124. | restore | 10: [10, inf] | restore 's iraq | 2003_invasion_of_Iraq |
| 125. | system | 10: [12, inf], 13: [12, 6.0] | system 's government | List_of_countries_by_system_of_government |
| 126. | amb | 10: [10, inf] | amb says american | Pa_amb_tomàquet |
| 127. | roma | 10: [12, inf] | roma cuts slovakia | Antiziganism |
| 128. | march | 10: [21, 5.25], 23: [12, inf], 27: [11, 5.5] | march 's government | Federal_government_of_the_United_States |
| 129. | departure | 10: [10, inf], 23: [15, inf] | departure 's government | Constitution_of_the_United_States |
| 130. | seek | 10: [12, inf] | seek 's says | Asylum_seeker |
| 131. | holy | 10: [10, inf], 33: [10, inf] | holy american shiite | Holy_Shiite |
| 132. | shiites | 10: [22, 11.0], 15: [18, inf] | shiites iraq shiite | Faisal_I_of_Iraq |
| 133. | gunfire | 10: [11, inf] | gunfire palestinian killed | Timeline_of_the_Israeli–Palestinian_conflict |
| 134. | paris— | 10: [10, inf] | paris— fashion 's | Paris_Fashion_Week |
| 135. | ice | 10: [10, inf] | ice says arctic | Arctic |
| 136. | plane | 11: [15, 7.5], 35: [10, inf], 42: [13, inf] | plane 's crash | Lynyrd_Skynyrd_plane_crash |
| 137. | ford | 11: [11, inf] | ford 's gucci | Tom_Ford |
| 138. | madrid | 11: [36, inf] | madrid spain bombings | 2004_Madrid_train_bombings |
| 139. | impeachment | 11: [17, inf] | impeachment 's south | Impeachment |
| 140. | iran | 11: [28, 7.0], 14: [11, 11.0], 25: [30, 30.0], 37: [10, inf], 41: [10, 5.0] | iran nuclear 's | Nuclear_program_of_Iran |
| 141. | syria | 11: [14, inf], 20: [10, inf] | syria 's israel | Israel–Syria_relations |
| 142. | spanish | 11: [17, inf] | spanish spain 's | Spain |
| 143. | civilians | 11: [11, inf], 14: [12, 12.0], 21: [11, inf] | civilians american killed | Civilian_casualties_in_the_war_in_Afghanistan_(2001–present) |
| 144. | information | 11: [10, inf], 30: [13, 6.5] | information 's intelligence | Intelligence_assessment |
| 145. | visit | 11: [10, 10.0], 20: [19, 9.5], 52: [10, inf] | visit 's says | Conjugal_visit |
| 146. | eta | 11: [12, inf] | eta spain basque | ETA_(separatist_group) |
| 147. | washington | 12: [10, 5.0], 23: [12, inf] | washington 's iraq | Iraq_War |
| 148. | suspect | 12: [15, 5.0], 15: [11, inf] | suspect 's attacks | List_of_fatal_alligator_attacks_in_the_United_States |
| 149. | zougam | 12: [12, inf] | zougam madrid attacks | Jamal_Zougam |
| 150. | kosovo | 12: [14, inf] | kosovo united nations | United_Nations_Interim_Administration_Mission_in_Kosovo |
| 151. | pakistani | 12: [29, inf], 16: [13, 13.0], 22: [16, 16.0], 30: [10, inf] | pakistani pakistan nuclear | Pakistan_and_weapons_of_mass_destruction |
| 152. | chen | 12: [13, inf], 21: [13, 6.5] | chen taiwan china | Chen_Shui-bian |
| 153. | serbs | 12: [12, inf] | serbs 's bosnian | Serbs_of_Bosnia_and_Herzegovina |
| 154. | zambia | 12: [10, inf] | zambia 's zimbabwe | Tonga_language_(Zambia_and_Zimbabwe) |
| 155. | sheik | 13: [21, inf] | sheik 's israel | Israeli–Palestinian_conflict |
| 156. | yassin | 13: [44, inf] | yassin hamas israel | Ahmed_Yassin |
| 157. | demands | 13: [11, inf] | demands 's iraq | Iraq |
| 158. | organization | 13: [10, inf] | organization 's world | World_Health_Organization |
| 159. | russian | 13: [14, inf] | russian russia 's | Russia |
| 160. | far | 13: [17, 8.5], 21: [12, 6.0], 35: [10, inf] | far 's says | Spider-Man:_Far_From_Home |
| 161. | confirm | 13: [10, inf] | confirm 's officials | Resistbot |
| 162. | egypt | 13: [11, inf], 41: [11, inf] | egypt israel israeli | Egypt–Israel_peace_treaty |
| 163. | gandhi | 13: [10, inf], 20: [10, inf] | gandhi india prime | Rajiv_Gandhi |
| 164. | resolution | 13: [10, 5.0], 30: [13, inf] | resolution united iraq | Authorization_for_Use_of_Military_Force_Against_Iraq_Resolution_of_2002 |
| 165. | loves | 13: [10, inf] | loves 's british | Everybody_Loves_a_Happy_Ending |
| 166. | threats | 13: [11, inf] | threats 's bush | Security_incidents_involving_George_W._Bush |
| 167. | korea | 13: [10, inf], 16: [33, 16.5], 26: [40, inf], 30: [16, 16.0], 34: [22, 22.0] | korea north south | North_Korea–South_Korea_relations |
| 168. | medical | 13: [12, inf] | medical 's health | Medical_officer_of_health |
| 169. | journalists | 14: [12, 6.0], 46: [11, inf] | journalists 's iraq | Media_coverage_of_the_Iraq_War |
| 170. | explosion | 14: [11, inf] | explosion killed people | 2020_Beirut_explosion |
| 171. | orders | 14: [16, inf] | orders 's court | Superior_orders |
| 172. | muslim | 14: [17, inf], 27: [13, 6.5] | muslim 's iraq | Islam_in_Iraq |
| 173. | uzbekistan | 14: [31, inf] | uzbekistan killed world | Uzbekistan |
| 174. | deaths | 14: [10, inf], 21: [14, 7.0], 42: [10, inf] | deaths killed 's | Killed_by_Death |
| 175. | building | 14: [12, inf], 27: [16, 16.0] | building 's american | United_States_Capitol |
| 176. | rules | 14: [11, inf], 18: [10, inf] | rules 's court | Merrick_Garland_Supreme_Court_nomination |
| 177. | mexicans | 14: [10, inf] | mexicans court mexico | Mexico |
| 178. | courts | 14: [12, inf] | courts court 's | United_States_courts_of_appeals |
| 179. | lithuania | 14: [15, inf] | lithuania nato russia | Russia–NATO_relations |
| 180. | falluja | 14: [23, 11.5], 22: [11, inf], 28: [11, 11.0], 45: [10, 5.0] | falluja american iraqi | Fallujah |
| 181. | grisly | 14: [10, inf] | grisly american iraq | Sabrina_Harman |
| 182. | bodies | 14: [13, inf] | bodies american found | Mermaids:_The_Body_Found |
| 183. | / | 15: [12, inf], 30: [44, 44.0] | / 's qaeda | Al-Qaeda |
| 184. | sadr | 15: [33, inf], 33: [43, 7.17] | sadr american 's | Muqtada_al-Sadr |
| 185. | shiite | 15: [63, 12.6], 50: [11, inf] | shiite american iraqi | January_2005_Iraqi_parliamentary_election |
| 186. | militia | 15: [23, inf], 19: [13, inf] | militia american 's | American_militia_movement |
| 187. | american-led | 15: [10, inf] | american-led iraq american | American-led_intervention_in_Iraq_(2014–present) |
| 188. | militiamen | 15: [11, inf], 33: [11, 11.0] | militiamen american najaf | Peace_Companies |
| 189. | followers | 15: [13, inf] | followers american sadr | Muqtada_al-Sadr |
| 190. | control | 15: [21, inf] | control 's government | Divided_government_in_the_United_States |
| 191. | small | 15: [12, inf] | small 's iraq | Iraq_War |
| 192. | karzai | 15: [10, 5.0], 19: [12, 6.0], 39: [11, 5.5], 41: [19, inf] | karzai afghan hamid | Hamid_Karzai |
| 193. | abu | 15: [12, inf], 19: [49, 7.0], 35: [31, 7.75] | abu iraq prison | Abu_Ghraib_torture_and_prisoner_abuse |
| 194. | insurgents | 15: [26, 26.0], 51: [10, inf] | insurgents american iraq | Iraqi_insurgency_(2003–2011) |
| 195. | sayyaf | 15: [11, inf] | sayyaf abu philippines | Abu_Sayyaf |
| 196. | project | 15: [10, inf] | project 's photos | Google_Photos |
| 197. | philippines | 15: [10, 5.0], 49: [14, inf] | philippines iraq philippine | Philippine_passport |
| 198. | japanese | 15: [17, inf], 33: [12, 6.0] | japanese japan 's | Japan |
| 199. | archaeologists | 15: [10, inf] | archaeologists ancient bc | Ancient_history_of_Afghanistan |
| 200. | african | 16: [20, inf], 46: [11, 5.5] | african africa south | South_Africa |
| 201. | standoff | 16: [10, inf] | standoff 's american | Bundy_standoff |
| 202. | negotiations | 16: [11, inf], 33: [11, inf] | negotiations 's american | Negotiation |
| 203. | judge | 16: [13, inf], 51: [14, inf] | judge 's court | United_States_district_court |
| 204. | vice | 16: [16, inf] | vice 's cheney | Dick_Cheney |
| 205. | dick | 16: [10, inf] | dick cheney 's | Dick_Cheney |
| 206. | press | 16: [11, 11.0], 24: [10, inf] | press 's iraq | 2003_invasion_of_Iraq |
| 207. | halliburton | 16: [12, inf] | halliburton iraq says | Halliburton |
| 208. | settlements | 16: [17, inf], 44: [16, inf] | settlements sharon gaza | Israeli_disengagement_from_Gaza |
| 209. | palestinian | 16: [29, 29.0], 24: [13, inf], 38: [15, inf] | palestinian israeli gaza | 2012_Israeli_operation_in_the_Gaza_Strip |
| 210. | training | 16: [12, 6.0], 35: [10, inf] | training iraq 's | NATO_Training_Mission_–_Iraq |
| 211. | italian | 16: [11, inf], 40: [12, inf] | italian italy 's | Demographics_of_Italy |
| 212. | gave | 17: [10, inf] | gave 's iraq | Iraq_War |
| 213. | begins | 17: [10, inf] | begins 's iraqi | Iran–Iraq_War |
| 214. | museum | 17: [10, inf] | museum 's germany | German_Museum_of_Technology |
| 215. | jordanian | 17: [18, 18.0], 33: [10, inf] | jordanian iraq iraqi | Iraq_War |
| 216. | river | 17: [11, inf] | river 's world | List_of_rivers_by_length |
| 217. | disappearance | 17: [12, inf] | disappearance military marine | Disappearance_of_Royal_Marine_Alan_Addis |
| 218. | car | 17: [12, inf], 22: [13, 6.5], 31: [16, 8.0], 40: [10, inf] | car killed bomb | Car_bomb |
| 219. | arafat | 17: [13, inf], 19: [10, inf], 34: [12, inf], 44: [26, 8.67] | arafat palestinian 's | Yasser_Arafat |
| 220. | basra | 17: [15, inf] | basra iraq iraqi | Iraqi_Navy |
| 221. | anger | 17: [10, inf] | anger 's iraq | Iran–Iraq_War |
| 222. | norad | 17: [10, inf] | norad commission pentagon | Criticism_of_the_9/11_Commission |
| 223. | mosque | 18: [10, inf] | mosque 's american | Mosque |
| 224. | hong | 18: [15, 7.5], 27: [23, inf], 37: [11, inf] | hong kong 's | Hong_Kong |
| 225. | kong | 18: [15, 7.5], 27: [23, inf], 37: [11, inf] | kong hong 's | Hong_Kong |
| 226. | positions | 18: [12, inf] | positions 's american | American_football_positions |
| 227. | photographs | 18: [11, inf] | photographs iraq prisoners | Abu_Ghraib_torture_and_prisoner_abuse |
| 228. | commander | 19: [14, inf], 22: [12, 6.0] | commander iraq 's | Assassination_of_Qasem_Soleimani |
| 229. | criminal | 19: [11, inf] | criminal 's iraqi | Supreme_Iraqi_Criminal_Tribunal |
| 230. | rights | 19: [20, 10.0], 25: [15, 5.0], 43: [10, inf] | rights 's human | Human_rights |
| 231. | cuba | 19: [18, inf] | cuba 's mexico | Cuba–Mexico_relations |
| 232. | contractors | 19: [16, inf] | contractors iraq american | List_of_defense_contractors |
| 233. | oil | 19: [14, 7.0], 25: [29, 7.25], 42: [14, inf] | oil 's iraq | Oil_reserves_in_Iraq |
| 234. | prisons | 19: [11, inf] | prisons iraq abuse | Iraq_prison_abuse_scandals |
| 235. | inquiry | 19: [10, inf] | inquiry 's iraq | Iraq_Inquiry |
| 236. | scandal | 19: [12, 6.0], 32: [10, inf] | scandal abuse 's | Catholic_Archdiocese_of_Boston_sex_abuse_scandal |
| 237. | family | 19: [10, inf] | family 's american | An_American_Family |
| 238. | statement | 19: [11, inf] | statement 's iraq | Iraqi_insurgency_(2003–2011) |
| 239. | mistreatment | 19: [11, inf] | mistreatment prisoners abuse | Prisoner_abuse |
| 240. | donald | 19: [15, inf] | donald rumsfeld iraq | Donald_Rumsfeld |
| 241. | king | 19: [11, inf] | king 's world | King_World_Productions |
| 242. | karbala | 19: [14, inf] | karbala american 's | Karbala |
| 243. | interviews | 19: [14, inf] | interviews 's iraq | 2003_invasion_of_Iraq |
| 244. | kadyrov | 20: [11, inf] | kadyrov 's chechnya | Ramzan_Kadyrov |
| 245. | municipal | 20: [10, inf] | municipal elections palestinian | 2004–05_Palestinian_local_elections |
| 246. | later | 20: [10, 5.0], 24: [20, 5.0], 26: [10, inf] | later 's iraq | Iraq_War |
| 247. | drugs | 20: [10, inf], 27: [12, inf] | drugs aids health | Epidemiology_of_HIV/AIDS |
| 248. | beheading | 20: [14, inf] | beheading iraq american | Beheading_video |
| 249. | nicholas | 20: [11, inf] | nicholas berg american | Nick_Berg |
| 250. | berg | 20: [17, inf] | berg american beheading | Nick_Berg |
| 251. | canada | 20: [11, inf], 49: [17, inf] | canada canadian 's | Canadians |
| 252. | release | 20: [16, 16.0], 24: [10, inf], 34: [13, inf], 40: [14, 7.0] | release 's iraq | Islamic_State_of_Iraq_and_the_Levant |
| 253. | document | 20: [10, 10.0], 26: [10, inf] | document 's iraq | Iraq_War_documents_leak |
| 254. | unclear | 21: [11, inf] | unclear 's american | United_States |
| 255. | target | 21: [13, inf] | target 's iraq | Iraqi_insurgency_(2003–2011) |
| 256. | airport | 21: [12, inf], 25: [14, inf] | airport 's world | List_of_busiest_airports_by_passenger_traffic |
| 257. | approval | 21: [12, inf] | approval 's government | Federal_government_of_the_United_States |
| 258. | homes | 21: [10, inf] | homes 's israeli | Israeli_demolition_of_Palestinian_property |
| 259. | provided | 21: [11, inf] | provided 's officials | Threatening_government_officials_of_the_United_States |
| 260. | cast | 21: [12, inf] | cast 's iraq | Iraq_War |
| 261. | singh | 21: [17, inf] | singh india prime | List_of_prime_ministers_of_India |
| 262. | path | 21: [10, inf] | path 's israel | Israel |
| 263. | payments | 21: [10, inf] | payments 's government | Transfer_payment |
| 264. | letter | 21: [10, inf] | letter 's bush | Mahmoud_Ahmadinejad's_letter_to_George_W._Bush |
| 265. | strike | 21: [11, 11.0], 25: [10, inf] | strike 's american | 2007–08_Writers_Guild_of_America_strike |
| 266. | chalabi | 21: [19, inf], 23: [21, 7.0], 33: [49, inf] | chalabi 's iraqi | Ahmed_Chalabi |
| 267. | korean | 22: [11, 5.5], 26: [23, inf] | korean north korea | North_Korea–South_Korea_relations |
| 268. | envoy | 22: [12, inf] | envoy iraq united | Brett_McGurk |
| 269. | lakhdar | 22: [10, inf] | lakhdar iraq brahimi | Lakhdar_Brahimi |
| 270. | brahimi | 22: [15, inf] | brahimi iraq government | Lakhdar_Brahimi |
| 271. | largest | 22: [13, inf] | largest 's world | Largest_airlines_in_the_world |
| 272. | dam | 22: [10, inf] | dam 's project | Hoover_Dam |
| 273. | mahdi | 22: [10, inf], 36: [10, inf] | mahdi 's american | Mahdi |
| 274. | dr | 22: [11, inf] | dr 's says | Dr._Dre |
| 275. | choice | 22: [12, inf] | choice 's iraq | Iraq |
| 276. | iyad | 22: [11, inf] | iyad iraq iraqi | Politics_of_Iraq |
| 277. | alawi | 22: [12, inf] | alawi iraqi minister | Alawi_(name) |
| 278. | enough | 23: [11, inf] | enough 's says | Enough_(film) |
| 279. | internet | 23: [10, 5.0], 26: [10, 5.0], 36: [10, inf] | internet 's government | Internet |
| 280. | crackdown | 23: [12, inf] | crackdown 's government | 709_crackdown |
| 281. | step | 23: [13, inf] | step 's says | List_of_Step_by_Step_episodes |
| 282. | sierra | 23: [12, inf] | sierra leone court | Special_Court_for_Sierra_Leone |
| 283. | leone | 23: [12, inf] | leone sierra court | Special_Court_for_Sierra_Leone |
| 284. | code | 23: [11, inf] | code 's turkey | Telephone_numbers_in_Turkey |
| 285. | like | 24: [12, inf] | like 's iraq | Islamic_State_of_Iraq_and_the_Levant |
| 286. | schroder | 24: [10, inf] | schroder 's german | Dennis_Schröder |
| 287. | officer | 24: [11, inf], 28: [10, 5.0] | officer iraq 's | Iraq_War |
| 288. | mohammed | 25: [11, inf] | mohammed qaeda 's | Khalid_Sheikh_Mohammed |
| 289. | johnson | 25: [21, inf] | johnson saudi american | Paul_Marshall_Johnson_Jr. |
| 290. | good | 25: [10, inf] | good 's iraq | Iraq_War |
| 291. | jr | 25: [11, inf] | jr american saudi | Vanessa_Trump |
| 292. | web | 25: [10, inf] | web site 's | Website |
| 293. | martin | 25: [10, inf] | martin 's canada | Mae_Martin |
| 294. | finds | 25: [10, inf] | finds 's report | U.S._News_&_World_Report |
| 295. | body | 26: [10, inf] | body 's iraq | Iraq_Body_Count_project |
| 296. | send | 26: [10, inf] | send iraq 's | American-led_intervention_in_Iraq_(2014–present) |
| 297. | demonstrations | 26: [10, inf] | demonstrations 's government | Government-organized_demonstration |
| 298. | guantanamo | 26: [11, inf] | guantanamo bay military | Guantanamo_Bay_detention_camp |
| 299. | seized | 26: [13, inf] | seized 's american | American_Civil_War |
| 300. | boats | 26: [13, inf] | boats iran british | Anglo-Soviet_invasion_of_Iran |
| 301. | techniques | 26: [10, inf] | techniques interrogation iraq | Enhanced_interrogation_techniques |
| 302. | switzerland | 26: [10, inf] | switzerland world 's | Switzerland_during_the_World_Wars |
| 303. | prosecution | 26: [11, inf] | prosecution 's court | Prosecutor |
| 304. | memo | 26: [20, inf] | memo bush pres | George_H._W._Bush |
| 305. | torture | 26: [13, inf] | torture 's report | Senate_Intelligence_Committee_report_on_CIA_torture |
| 306. | exhibit | 26: [14, inf] | exhibit germany corpses | Soap_made_from_human_corpses |
| 307. | rockets | 27: [14, inf] | rockets israeli gaza | 2014_Gaza_War |
| 308. | decision | 27: [17, 17.0], 41: [11, inf], 49: [13, inf] | decision 's iraq | Iraq_War |
| 309. | rocket | 27: [13, inf] | rocket israeli gaza | 2012_Israeli_operation_in_the_Gaza_Strip |
| 310. | custody | 27: [15, 7.5], 46: [10, inf] | custody 's american | Custody |
| 311. | camp | 27: [10, inf] | camp 's israeli | 2000_Camp_David_Summit |
| 312. | families | 28: [14, inf] | families 's government | Federal_government_of_the_United_States |
| 313. | bahrain | 28: [10, inf] | bahrain families attacks | Bahrain |
| 314. | embassy | 28: [10, inf], 37: [10, 5.0], 41: [10, 5.0] | embassy american says | Embassy_of_the_United_States,_Baghdad |
| 315. | wahed | 28: [10, inf] | wahed afghan 's | Second_Anglo-Afghan_War |
| 316. | paris | 28: [10, inf], 35: [29, 5.8], 41: [38, 6.33] | paris france 's | Paris |
| 317. | c.i.a | 28: [12, inf] | c.i.a intelligence 's | Director_of_the_Central_Intelligence_Agency |
| 318. | committee | 28: [21, inf] | committee intelligence iraq | United_States_Senate_Select_Committee_on_Intelligence |
| 319. | concrete | 28: [10, inf] | concrete 's iraqi | Concrete_bomb |
| 320. | defectors | 28: [10, inf] | defectors north korea | North_Korean_defectors |
| 321. | idema | 28: [12, inf], 30: [14, inf] | idema american afghan | Jonathan_Idema |
| 322. | agencies | 28: [12, inf] | agencies intelligence 's | Intelligence_agency |
| 323. | company | 29: [10, inf], 39: [15, inf] | company 's iraq | Iraq_Petroleum_Company |
| 324. | anti-semitic | 29: [10, inf] | anti-semitic france jewish | Antisemitic_canard |
| 325. | france | 29: [15, 5.0], 40: [12, inf], 43: [26, 5.2], 50: [24, 12.0] | france 's french | France |
| 326. | donors | 29: [13, inf] | donors aids million | The_Global_Fund_to_Fight_AIDS,_Tuberculosis_and_Malaria |
| 327. | lord | 29: [11, inf] | lord 's intelligence | Joint_Intelligence_Committee_(United_Kingdom) |
| 328. | tuberculosis | 29: [10, inf] | tuberculosis aids fund | The_Global_Fund_to_Fight_AIDS,_Tuberculosis_and_Malaria |
| 329. | seminary | 29: [10, 5.0], 33: [11, inf] | seminary st polten | Catholic_Church_sexual_abuse_scandal_in_Austria |
| 330. | school | 29: [17, 8.5], 36: [40, inf], 42: [10, inf] | school 's children | Professional_Children's_School |
| 331. | area | 30: [10, inf], 35: [10, 10.0] | area 's american | American_Viticultural_Area |
| 332. | running | 30: [17, inf] | running 's government | Federal_government_of_the_United_States |
| 333. | directly | 30: [10, inf] | directly 's report | Mueller_report |
| 334. | pentagon | 30: [12, 12.0], 33: [11, inf] | pentagon iraq 's | The_Pentagon |
| 335. | captured | 30: [12, inf] | captured american 's | Captured_Tracks |
| 336. | bureau | 30: [12, inf] | bureau intelligence 's | Intelligence_Bureau_(India) |
| 337. | genocide | 30: [14, inf] | genocide sudan 's | Darfur_genocide |
| 338. | city | 30: [17, 8.5], 48: [16, 8.0], 52: [13, inf] | city 's american | List_of_U.S._cities_with_large_African-American_populations |
| 339. | abuses | 30: [11, inf], 35: [26, 6.5] | abuses military prison | Abu_Ghraib_torture_and_prisoner_abuse |
| 340. | pledge | 30: [10, inf] | pledge 's says | Pledge_of_Allegiance |
| 341. | passengers | 30: [10, inf] | passengers plane airport | Dulles_International_Airport |
| 342. | wine | 30: [10, inf] | wine france food | French_wine |
| 343. | assesses | 30: [10, inf] | assesses looking panel | Cohort_study |
| 344. | opportunities | 30: [10, inf] | opportunities 's looking | Career_Opportunities_(film) |
| 345. | prosecutor | 30: [10, inf] | prosecutor 's court | Prosecutor |
| 346. | york | 30: [10, inf], 32: [19, inf] | york 's officials | List_of_U.S._statewide_elected_officials |
| 347. | fahim | 31: [10, inf] | fahim karzai president | Mohammed_Fahim |
| 348. | embassies | 31: [10, inf] | embassies say officials | Diplomatic_mission |
| 349. | appeals | 31: [12, inf] | appeals 's court | United_States_courts_of_appeals |
| 350. | durban | 31: [10, inf] | durban south africa | Durban |
| 351. | mr. | 31: [10, inf], 41: [11, inf], 50: [12, inf] | mr. 's president | Mr._President_(title) |
| 352. | paraguay | 32: [10, inf] | paraguay fire people | Ycuá_Bolaños_supermarket_fire |
| 353. | store | 32: [10, inf] | store 's people | People's_store |
| 354. | christians | 32: [17, inf] | christians 's iraq | Christianity_in_Iraq |
| 355. | financial | 32: [16, inf] | financial 's says | Say's_law |
| 356. | institutions | 32: [12, inf] | institutions 's iraq | Iraq |
| 357. | federal | 32: [12, inf] | federal 's officials | Threatening_government_officials_of_the_United_States |
| 358. | plant | 33: [17, inf] | plant nuclear 's | Chernobyl_Nuclear_Power_Plant |
| 359. | ahmad | 33: [10, inf] | ahmad chalabi 's | Ahmed_Chalabi |
| 360. | soccer | 33: [10, inf] | soccer 's stadium | Soccer-specific_stadium |
| 361. | chinese | 33: [10, inf] | chinese china 's | China |
| 362. | dept | 33: [14, inf] | dept 's iraq | Ministry_of_Health_(Iraq) |
| 363. | immigration | 33: [11, inf] | immigration 's illegal | Illegal_immigration |
| 364. | immigrants | 33: [12, inf] | immigrants europe illegal | Illegal_immigration_to_the_United_States |
| 365. | singapore | 33: [13, inf] | singapore 's lee | Lee_family_(Singapore) |
| 366. | lee | 33: [13, inf] | lee 's singapore | Lee_family_(Singapore) |
| 367. | shrine | 33: [13, inf] | shrine najaf 's | Imam_Ali_Shrine |
| 368. | carter | 34: [10, inf] | carter chavez recall | 2004_Venezuelan_recall_referendum |
| 369. | journalist | 34: [10, inf] | journalist 's american | Michael_Tracey_(American_journalist) |
| 370. | garen | 34: [11, inf] | garen sadr american | Micah_Garen |
| 371. | koreans | 34: [11, inf] | koreans korea north | North_Korea–South_Korea_relations |
| 372. | james | 35: [10, inf] | james 's military | John_E._James |
| 373. | munch | 35: [10, inf] | munch museum oslo | Munch_Museum |
| 374. | interrogations | 35: [11, inf] | interrogations military iraq | Interrogation |
| 375. | guilty | 35: [10, inf] | guilty prison 's | Larry_Nassar |
| 376. | sistani | 35: [11, inf] | sistani 's iraqi | Ali_al-Sistani |
| 377. | politics | 36: [10, inf] | politics 's photo | Donald_Trump_photo_op_at_St._John's_Church |
| 378. | shift | 36: [10, inf] | shift 's bush | George_H._W._Bush |
| 379. | beslan | 36: [15, inf] | beslan school russian | Beslan_school_siege |
| 380. | ahern | 38: [10, inf] | ahern irish prime | Cecelia_Ahern |
| 381. | adultery | 38: [11, inf] | adultery turkey union | Adultery |
| 382. | greece | 39: [11, inf] | greece athens greek | Athens |
| 383. | peru | 40: [10, inf] | peru 's toledo | Alejandro_Toledo |
| 384. | urges | 40: [10, inf] | urges 's says | Urge_(film) |
| 385. | four | 40: [10, inf], 50: [19, inf] | four 's american | List_of_active_duty_United_States_four-star_officers |
| 386. | islamic | 41: [12, inf] | islamic 's group | Islamic_State_of_Iraq_and_the_Levant |
| 387. | khmer | 41: [10, inf] | khmer rouge leaders | Khmer_Rouge |
| 388. | rouge | 41: [10, inf] | rouge khmer leaders | Khmer_Rouge |
| 389. | next | 41: [10, inf] | next 's iraq | Iraq_War |
| 390. | prize | 41: [12, inf] | prize nobel 's | Nobel_Prize |
| 391. | rejects | 42: [12, inf] | rejects 's says | Say's_law |
| 392. | indians | 42: [10, inf] | indians 's india | Indian_independence_movement |
| 393. | finish | 42: [10, inf] | finish 's projects | Works_Progress_Administration |
| 394. | counting | 42: [10, inf] | counting election votes | Vote_counting |
| 395. | hassan | 43: [11, inf] | hassan 's iran | Hassan_Rouhani |
| 396. | myanmar | 43: [10, inf] | myanmar 's government | Politics_of_Myanmar |
| 397. | typhoon | 43: [14, inf] | typhoon japan 's | Typhoon_Hagibis |
| 398. | dead | 44: [12, inf] | dead 's people | Conversations_with_Dead_People |
| 399. | dogs | 44: [12, inf] | dogs 's prison | War_Dogs_(2016_film) |
| 400. | thatcher | 44: [12, inf] | thatcher africa south | Mark_Thatcher |
| 401. | tests | 44: [11, inf] | tests 's says | Student's_t-test |
| 402. | irregularities | 45: [10, inf] | irregularities election 's | 2004_United_States_election_voting_controversies |
| 403. | agreement | 45: [10, 5.0], 48: [16, inf] | agreement 's iraq | U.S.–Iraq_Status_of_Forces_Agreement |
| 404. | appeal | 45: [10, inf] | appeal 's court | United_States_courts_of_appeals |
| 405. | annan | 45: [11, inf], 49: [17, inf] | annan united kofi | Kofi_Annan |
| 406. | dutch | 45: [10, inf] | dutch netherlands police | Law_enforcement_in_the_Netherlands |
| 407. | abbas | 45: [10, inf] | abbas palestinian arafat | Mahmoud_Abbas |
| 408. | newmont | 46: [10, inf] | newmont indonesian bay | Newmont_Corporation |
| 409. | discussed | 46: [12, inf] | discussed 's officials | United_States_Senate |
| 410. | cyprus | 46: [10, inf] | cyprus turkey european | Turkish_Cypriots |
| 411. | ukraine | 48: [28, inf] | ukraine 's election | 2019_Ukrainian_presidential_election |
| 412. | captain | 48: [10, inf] | captain army military | Captain_(armed_forces) |
| 413. | viktor | 48: [17, inf] | viktor 's election | Viktor_Yushchenko |
| 414. | yushchenko | 48: [12, inf] | yushchenko viktor election | Viktor_Yushchenko |
| 415. | southeast | 49: [10, inf] | southeast 's nations | ASEAN |
| 416. | lure | 49: [12, inf] | lure 's luxury | Maurice_Lacroix |
| 417. | law | 49: [15, inf] | law 's government | Constitutional_law |
| 418. | kojo | 49: [10, inf] | kojo 's annan | Kojo_Annan |
| 419. | hospital | 50: [10, inf] | hospital 's american | American_Mission_Hospital |
| 420. | monday | 50: [22, inf] | monday 's iraq | Occupation_of_Iraq_(2003–2011) |
| 421. | students | 50: [10, inf] | students school 's | Student |
| 422. | village | 50: [10, inf] | village 's government | Government_of_Kerala |
| 423. | salinas | 50: [14, inf] | salinas 's mexico | Carlos_Salinas_de_Gortari |
| 424. | old | 51: [10, inf] | old 's iraq | Iraq_War |
| 425. | turks | 51: [10, inf] | turks 's turkey | Turkish_people |
| 426. | congo | 51: [10, inf] | congo world briefing | Second_Congo_War |
| 427. | christian | 52: [10, inf] | christian 's iraq | Christianity_in_Iraq |
| 428. | darfur | 52: [10, inf] | darfur sudan government | War_in_Darfur |
| 429. | waves | 53: [11, inf] | waves 's indian | 2004_Indian_Ocean_earthquake_and_tsunami |
| 430. | indian | 53: [20, inf] | indian india 's | Economy_of_India |
| 431. | ocean | 53: [13, inf] | ocean indian tsunami | 2004_Indian_Ocean_earthquake_and_tsunami |
| 432. | earthquake | 53: [21, inf] | earthquake 's iran | 2003_Bam_earthquake |
| 433. | struck | 53: [11, inf] | struck 's say | Gloria_Struck |
| 434. | disaster | 53: [21, inf] | disaster 's people | Disaster |
| 435. | tsunami | 53: [37, inf] | tsunami indian indonesia | 2004_Indian_Ocean_earthquake_and_tsunami |
| 436. | cost | 53: [11, inf] | cost 's iraq | Financial_cost_of_the_Iraq_War |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | voices | 12: [21, inf] | voices iraq geoff | Gulf_War |
| 2. | hamas | 13: [10, inf] | hamas israel leader | Hamas |
| 3. | hostage | 39: [10, inf] | hostage us 's | Iran_hostage_crisis |
| 4. | arafat | 44: [11, inf] | arafat 's yasser | Cause_of_Yasser_Arafat's_death |
| 5. | ukraine | 48: [18, inf] | ukraine poll 's | Languages_of_Ukraine |
