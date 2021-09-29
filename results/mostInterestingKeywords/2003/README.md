# Keywords with the highest 'interestingness' in 2003

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
| 1. | campaign | 2: [10, inf], 43: [11, inf], 49: [10, inf] | campaign 's iraq | Iraq_Campaign_Medal |
| 2. | research | 2: [10, inf] | research 's nuclear | Bhabha_Atomic_Research_Centre |
| 3. | use | 2: [17, inf], 28: [12, 6.0] | use iraq 's | Authorization_for_Use_of_Military_Force_Against_Iraq_Resolution_of_2002 |
| 4. | sought | 2: [10, inf] | sought 's iraq | Iran–Iraq_War |
| 5. | trade | 2: [16, 8.0], 6: [10, inf], 12: [11, inf], 42: [22, 5.5] | trade 's world | World_Trade_Center_site |
| 6. | missiles | 2: [10, inf], 8: [14, 7.0], 12: [35, 17.5] | missiles iraq 's | Scud_missile |
| 7. | qaeda | 2: [22, 7.33], 14: [16, 5.33], 20: [40, 13.33], 24: [23, 11.5], 26: [26, inf], 32: [11, 5.5], 46: [26, 5.2] | qaeda 's iraq | Saddam_Hussein_and_al-Qaeda_link_allegations |
| 8. | gun | 2: [12, inf] | gun iraq 's | Katharine_Gun |
| 9. | ireland | 2: [10, inf], 14: [15, 5.0], 25: [18, 9.0], 32: [16, 16.0] | ireland northern world | Northern_Ireland |
| 10. | japan | 2: [16, 8.0], 8: [16, inf], 13: [15, 5.0], 33: [27, 13.5], 41: [10, 5.0], 45: [10, 10.0] | japan north korea | Japan–North_Korea_relations |
| 11. | blair | 2: [14, inf], 17: [14, 7.0], 28: [24, 12.0], 47: [35, 5.83] | blair iraq prime | Tony_Blair |
| 12. | terror | 2: [12, 6.0], 10: [19, 19.0], 47: [11, inf] | terror 's iraq | War_on_terror |
| 13. | suspects | 2: [11, inf], 15: [10, inf], 46: [11, 11.0] | suspects american 's | The_Usual_Suspects |
| 14. | wife | 2: [10, inf] | wife 's says | The_Wife_of_Bath's_Tale |
| 15. | week | 2: [15, 5.0], 32: [10, inf] | week 's iraq | Iraq_War |
| 16. | sri | 2: [19, inf] | sri lanka world | Sri_Lanka_national_cricket_team |
| 17. | lanka | 2: [12, inf] | lanka sri world | Sri_Lanka_national_cricket_team |
| 18. | tamil | 2: [10, inf] | tamil sri lanka | Sri_Lankan_Tamils |
| 19. | taken | 2: [11, inf] | taken 's iraq | List_of_Congressional_opponents_of_the_Iraq_War |
| 20. | rebels | 2: [10, 5.0], 5: [16, 8.0], 17: [12, inf], 38: [11, inf] | rebels government 's | List_of_Star_Wars_Rebels_characters |
| 21. | energy | 2: [17, inf], 25: [12, 12.0] | energy nuclear iran | Nuclear_program_of_Iran |
| 22. | indonesia | 2: [16, inf], 8: [12, inf], 20: [11, inf] | indonesia indonesian 's | Indonesia |
| 23. | increases | 2: [12, inf] | increases 's iraq | Iraq |
| 24. | show | 2: [10, inf], 10: [14, inf], 13: [11, 5.5] | show 's iraq | Iraq_War |
| 25. | conference | 2: [12, inf], 10: [18, 9.0], 49: [10, inf] | conference 's iraq | Iraq_War |
| 26. | atomic | 2: [13, inf], 25: [15, 15.0] | atomic nuclear iran | Nuclear_facilities_in_Iran |
| 27. | food | 2: [11, 11.0], 5: [24, 6.0], 13: [23, inf], 20: [11, 5.5], 32: [10, inf], 47: [18, 18.0], 50: [15, 15.0] | food 's says | Food_and_Drug_Administration |
| 28. | talk | 2: [11, inf] | talk 's iraq | 2003_invasion_of_Iraq |
| 29. | giving | 2: [10, inf] | giving 's iraq | Iraq_War |
| 30. | arms | 2: [19, inf] | arms iraq 's | Coat_of_arms_of_Iraq |
| 31. | diplomats | 2: [10, inf], 20: [11, 5.5] | diplomats iraq 's | Abduction_of_Russian_diplomats_in_Iraq |
| 32. | bill | 2: [15, inf], 27: [25, 25.0], 44: [20, 5.0] | bill 's bush | George_H._W._Bush |
| 33. | richardson | 2: [19, inf] | richardson north korea | Bill_Richardson |
| 34. | jewish | 2: [13, inf], 11: [15, inf], 23: [17, 8.5] | jewish israel 's | Jewish_Agency_for_Israel |
| 35. | polish | 2: [10, inf] | polish poland 's | History_of_Jews_in_Poland |
| 36. | dutch | 2: [10, inf] | dutch 's europe | Dutch_language |
| 37. | duisenberg | 2: [10, inf] | duisenberg dutch bank | Wim_Duisenberg |
| 38. | arafat | 2: [10, 10.0], 23: [10, inf] | arafat palestinian israel | Yasser_Arafat |
| 39. | terrorist | 2: [13, inf], 12: [13, 13.0] | terrorist 's attacks | September_11_attacks |
| 40. | election | 2: [10, inf] | election 's party | 2024_United_States_presidential_election |
| 41. | nonproliferation | 2: [13, inf] | nonproliferation nuclear north | Treaty_on_the_Non-Proliferation_of_Nuclear_Weapons |
| 42. | greece | 2: [10, inf], 6: [12, inf], 50: [12, inf] | greece europe world | Greece |
| 43. | roh | 3: [13, inf], 9: [19, 9.5] | roh korea north | Roh_Moo-hyun |
| 44. | moo | 3: [11, inf], 9: [13, 6.5] | moo korea north | North_Korea–South_Korea_relations |
| 45. | hyun | 3: [11, inf], 9: [13, 6.5] | hyun korea north | Hyun_Bin |
| 46. | pope | 3: [16, inf], 23: [14, inf], 37: [16, 8.0], 52: [11, inf] | pope paul john | Pope_John_Paul_II |
| 47. | taliban | 3: [10, inf], 23: [12, 12.0], 41: [13, 6.5] | taliban afghanistan afghan | War_in_Afghanistan_(2001–present) |
| 48. | kurdish | 3: [13, inf], 6: [30, 5.0] | kurdish iraq american | Iraqi–Kurdish_conflict |
| 49. | date | 3: [10, inf] | date iraq 's | Dating |
| 50. | zimbabwe | 3: [10, inf], 5: [18, inf], 19: [14, inf], 24: [11, inf], 38: [22, 5.5] | zimbabwe mugabe africa | Robert_Mugabe |
| 51. | officer | 3: [16, inf], 6: [12, 6.0], 16: [12, 12.0] | officer 's american | Officer_(armed_forces) |
| 52. | manchester | 3: [10, inf] | manchester police officer | Murders_of_Nicola_Hughes_and_Fiona_Bone |
| 53. | officers | 3: [13, inf], 47: [11, inf] | officers 's american | List_of_active_duty_United_States_four-star_officers |
| 54. | scientists | 3: [14, inf] | scientists 's weapons | List_of_states_with_nuclear_weapons |
| 55. | cyprus | 3: [16, inf], 9: [10, inf] | cyprus europe world | Cyprus |
| 56. | vatican | 3: [15, inf], 5: [18, 18.0], 31: [10, inf] | vatican pope world | Vatican_City_in_World_War_II |
| 57. | back | 3: [10, inf], 21: [25, 5.0] | back 's iraq | Iraq |
| 58. | politicians | 3: [11, inf] | politicians 's government | List_of_foreign-born_United_States_politicians |
| 59. | comments | 3: [11, inf], 24: [11, inf], 43: [11, inf] | comments 's iraq | 2003_invasion_of_Iraq |
| 60. | votes | 3: [11, inf] | votes 's iraq | Iraq_War |
| 61. | chemical | 3: [11, inf], 33: [11, inf] | chemical iraq weapons | Iraqi_chemical_weapons_program |
| 62. | polio | 3: [12, inf] | polio india cases | Pulse_Polio |
| 63. | private | 4: [10, inf], 29: [13, inf], 45: [12, 6.0] | private 's iraq | Private_militias_in_Iraq |
| 64. | colin | 4: [13, inf], 16: [14, 14.0], 43: [10, 5.0], 49: [12, inf] | colin powell iraq | Colin_Powell |
| 65. | powell | 4: [25, inf], 16: [17, 5.67], 28: [15, 5.0], 32: [27, 13.5], 43: [21, 10.5], 49: [28, inf] | powell iraq state | Colin_Powell |
| 66. | crimes | 4: [15, 15.0], 11: [14, 7.0], 23: [10, inf], 31: [19, 9.5] | crimes 's tribunal | International_Military_Tribunal_for_the_Far_East |
| 67. | college | 4: [16, inf] | college 's students | Student |
| 68. | kuwait | 4: [13, inf] | kuwait iraq american | Invasion_of_Kuwait |
| 69. | u.n | 4: [10, 10.0], 6: [16, inf] | u.n iraq 's | Iraq_War |
| 70. | much | 4: [12, 6.0], 10: [22, 22.0], 42: [12, inf] | much 's iraq | Iraq_War |
| 71. | cleric | 4: [11, inf], 35: [25, 25.0], 41: [10, inf] | cleric 's iraq | Muqtada_al-Sadr |
| 72. | taiwan | 4: [10, inf], 18: [14, 7.0] | taiwan china sars | 2002–2004_SARS_outbreak |
| 73. | team | 4: [15, 7.5], 9: [18, inf], 23: [13, 6.5] | team iraq 's | Iraq_national_football_team |
| 74. | pilots | 4: [14, inf] | pilots iraq air | Iraqi_Air_Force |
| 75. | zones | 4: [10, inf] | zones american iraq | Iraqi_no-fly_zones_conflict |
| 76. | address | 5: [13, inf], 36: [11, inf] | address 's bush | George_W._Bush |
| 77. | signs | 5: [10, inf], 12: [13, inf], 15: [11, inf] | signs 's iraq | Iraqi_Sign_Language |
| 78. | divided | 5: [11, inf] | divided 's iraq | Iraq |
| 79. | fight | 5: [14, inf], 43: [11, 11.0] | fight 's iraq | War_in_Iraq_(2013–2017) |
| 80. | tibetan | 5: [14, inf] | tibetan chinese china | Sino-Tibetan_languages |
| 81. | monk | 5: [12, inf] | monk tibetan court | Tibetan_Buddhism |
| 82. | rebel | 5: [14, 7.0], 18: [12, inf], 26: [11, 5.5] | rebel 's government | Rebellion |
| 83. | kandahar | 5: [12, inf] | kandahar taliban afghanistan | United_States_invasion_of_Afghanistan |
| 84. | accord | 5: [17, inf], 10: [13, inf], 18: [10, 5.0], 29: [10, 5.0] | accord 's peace | Camp_David_Accords |
| 85. | letter | 5: [12, inf], 21: [10, 5.0] | letter 's iraq | Iraqi_insurgency_(2003–2011) |
| 86. | journalists | 5: [14, inf], 12: [10, inf], 14: [23, 23.0], 17: [11, inf], 19: [12, 12.0] | journalists 's american | List_of_Jewish_American_journalists |
| 87. | abuse | 5: [10, inf] | abuse children 's | Child_abuse |
| 88. | sex | 5: [11, inf] | sex 's europe | Recognition_of_same-sex_unions_in_Europe |
| 89. | explosion | 5: [13, inf], 52: [11, 11.0] | explosion killed people | 2020_Beirut_explosion |
| 90. | militant | 5: [15, inf], 32: [11, 11.0] | militant palestinian israeli | Israeli–Palestinian_conflict |
| 91. | helicopter | 5: [13, inf], 45: [28, inf] | helicopter american iraq | List_of_aviation_shootdowns_and_accidents_during_the_Iraq_War |
| 92. | operations | 5: [10, inf], 18: [14, 14.0], 50: [10, 5.0] | operations iraq 's | Iraq_War |
| 93. | prison | 5: [10, 10.0], 38: [20, inf] | prison 's years | Prison |
| 94. | christians | 5: [11, inf] | christians 's muslims | Christianity_and_Islam |
| 95. | analysts | 5: [10, inf] | analysts 's say | Tiffany_Cross |
| 96. | chechen | 5: [13, inf] | chechen russia russian | Chechen–Russian_conflict |
| 97. | freed | 5: [12, inf] | freed 's world | Free_World |
| 98. | rising | 5: [10, inf] | rising 's iraq | Iraq |
| 99. | bus | 5: [15, inf], 34: [13, 13.0] | bus israeli hamas | Hamas |
| 100. | columbia | 6: [11, inf] | columbia space canada | Canadian_Space_Agency |
| 101. | attempts | 6: [10, inf] | attempts 's american | List_of_United_States_presidential_assassination_attempts_and_plots |
| 102. | park | 6: [17, inf], 37: [16, inf] | park 's national | List_of_national_parks_of_the_United_States |
| 103. | mugabe | 6: [12, inf], 14: [14, 14.0], 19: [11, inf] | mugabe zimbabwe 's | Robert_Mugabe |
| 104. | rumsfeld | 6: [16, inf], 12: [15, 5.0], 24: [19, 19.0], 36: [10, 10.0], 41: [12, inf], 43: [13, inf], 46: [17, 17.0], 49: [32, 10.67] | rumsfeld iraq defense | Donald_Rumsfeld |
| 105. | text | 6: [12, inf], 10: [10, 5.0] | text following 's | Text_messaging |
| 106. | suicide | 6: [11, 5.5], 13: [24, 6.0], 44: [20, 5.0], 47: [15, 5.0], 52: [16, inf] | suicide 's palestinian | List_of_Palestinian_suicide_attacks |
| 107. | michigan | 6: [12, inf] | michigan mr. iraq | Gulf_War |
| 108. | congo | 7: [13, inf], 19: [10, inf], 22: [14, inf], 29: [10, inf] | congo africa force | Belgian_Congo |
| 109. | laden | 7: [18, 9.0], 21: [10, 5.0], 37: [16, inf] | laden qaeda osama | Hamza_bin_Laden |
| 110. | planning | 7: [15, 7.5], 37: [12, inf], 50: [12, inf] | planning iraq 's | 2003_invasion_of_Iraq |
| 111. | philippines | 7: [11, inf], 12: [10, 5.0] | philippines asia world | Philippines |
| 112. | major | 7: [16, inf], 27: [12, 6.0], 32: [12, inf] | major 's iraq | Iraq |
| 113. | foods | 7: [12, inf] | foods europe european | Europe |
| 114. | children | 7: [10, 10.0], 31: [14, 7.0], 34: [19, 6.33], 39: [10, inf] | children 's american | Children's_literature |
| 115. | target | 7: [10, inf] | target 's iraq | Iraqi_insurgency_(2003–2011) |
| 116. | tape | 7: [10, inf] | tape hussein 's | Qusay_Hussein |
| 117. | cia | 7: [14, inf], 40: [20, inf], 44: [11, 5.5] | cia 's intelligence | Central_Intelligence_Agency |
| 118. | tenet | 7: [14, inf], 28: [10, inf] | tenet cia iraq | George_Tenet |
| 119. | berlusconi | 7: [12, 12.0], 19: [12, 12.0], 22: [13, inf], 25: [10, 5.0], 31: [12, 6.0], 34: [10, inf], 46: [10, inf] | berlusconi italy prime | Silvio_Berlusconi |
| 120. | embassy | 8: [12, inf], 32: [19, inf], 45: [10, 10.0] | embassy american 's | 1998_United_States_embassy_bombings |
| 121. | town | 8: [15, 7.5], 12: [11, inf], 26: [18, inf] | town 's american | S-Town |
| 122. | abdullah | 8: [12, inf], 20: [11, inf] | abdullah 's american | Abdullah_Abdullah |
| 123. | training | 8: [11, inf], 27: [10, inf] | training iraq 's | NATO_Training_Mission_–_Iraq |
| 124. | hamas | 8: [22, 11.0], 10: [15, inf], 18: [18, 18.0], 49: [10, inf] | hamas palestinian israeli | Hamas |
| 125. | fire | 8: [22, 22.0], 38: [12, inf], 45: [10, 10.0] | fire 's american | St._Elmo's_fire |
| 126. | chirac | 8: [18, inf], 15: [12, 6.0], 38: [10, inf], 47: [15, 7.5] | chirac france iraq | Jacques_Chirac |
| 127. | lived | 8: [10, inf] | lived 's iraq | Iraq |
| 128. | arab | 8: [19, 19.0], 26: [11, inf], 49: [15, inf] | arab iraq 's | Arab_Federation |
| 129. | shields | 8: [11, inf] | shields iraqi american | Operation_Desert_Shield_(Iraq) |
| 130. | egypt | 8: [13, inf], 12: [20, 5.0] | egypt 's arab | Egypt |
| 131. | nigerian | 8: [10, 10.0], 17: [11, inf] | nigerian pres 's | Nigeria |
| 132. | croatia | 8: [10, inf], 23: [13, inf] | croatia 's europe | 2013_enlargement_of_the_European_Union |
| 133. | arabia | 8: [12, inf], 12: [15, inf], 18: [13, 6.5], 20: [32, 32.0] | arabia saudi 's | Saudi_Arabia |
| 134. | scotland | 8: [10, inf] | scotland libya 's | History_of_Libya_under_Muammar_Gaddafi |
| 135. | department | 9: [12, inf] | department state iraq | Islamic_State_of_Iraq_and_the_Levant |
| 136. | mideast | 9: [11, 5.5], 30: [10, inf], 45: [11, 5.5] | mideast bush palestinian | Israeli–Palestinian_conflict |
| 137. | cbs | 9: [14, inf] | cbs interview hussein | February_2003_Saddam_Hussein_interview |
| 138. | claims | 9: [11, inf] | claims 's iraq | Territory_of_the_Islamic_State |
| 139. | reactor | 9: [16, inf] | reactor nuclear north | List_of_nuclear_reactors |
| 140. | concerns | 9: [12, inf] | concerns 's iraq | Iraq |
| 141. | cabinet | 9: [17, inf], 20: [10, inf], 36: [10, inf], 39: [12, inf] | cabinet 's palestinian | Palestinian_National_Authority |
| 142. | far-right | 9: [11, inf] | far-right party 's | Far-right_politics |
| 143. | parade | 9: [11, inf] | parade 's first | Macy's_Thanksgiving_Day_Parade |
| 144. | samba | 9: [10, inf] | samba carnival parade | Brazilian_Carnival |
| 145. | labor | 9: [11, 5.5], 11: [15, 7.5], 22: [12, inf], 40: [10, inf] | labor 's blair | Battle_of_Blair_Mountain |
| 146. | netanyahu | 9: [10, inf] | netanyahu israel sharon | Benjamin_Netanyahu |
| 147. | decision | 9: [13, 13.0], 22: [11, inf], 36: [15, 7.5] | decision 's iraq | Iraq_War |
| 148. | lawmakers | 9: [10, inf] | lawmakers 's iraq | Iraq_and_weapons_of_mass_destruction |
| 149. | tobacco | 9: [10, inf], 18: [10, inf], 21: [10, inf] | tobacco treaty health | WHO_Framework_Convention_on_Tobacco_Control |
| 150. | airlines | 9: [10, inf], 14: [11, 5.5] | airlines sars taiwan | COVID-19_pandemic_in_Taiwan |
| 151. | camp | 10: [18, inf], 24: [12, 6.0], 41: [21, 5.25] | camp iraq 's | Camp_Justice_(Iraq) |
| 152. | deployment | 10: [12, inf], 14: [10, 5.0] | deployment iraq troops | Multi-National_Force_–_Iraq |
| 153. | pakistan | 10: [39, 5.57], 17: [24, 8.0], 22: [12, 12.0], 39: [10, inf] | pakistan 's india | India–Pakistan_relations |
| 154. | bank | 10: [17, inf] | bank israeli palestinian | Israeli_West_Bank_barrier |
| 155. | joint | 10: [10, inf], 13: [11, inf], 26: [12, inf] | joint iraq 's | Authorization_for_Use_of_Military_Force_Against_Iraq_Resolution_of_2002 |
| 156. | study | 10: [12, inf], 19: [10, 10.0], 42: [12, 6.0], 49: [10, inf] | study 's iraq | Iraq_Study_Group |
| 157. | stalin | 10: [10, inf] | stalin 's trials | Moscow_Trials |
| 158. | records | 10: [10, inf] | records 's iraq | Iraq |
| 159. | transcript | 10: [32, inf] | transcript following 's | The_Transcript |
| 160. | recorded | 10: [32, inf] | recorded 's following | Cult_following |
| 161. | zoo | 10: [10, inf] | zoo 's animals | Zoo |
| 162. | oil | 10: [20, 10.0], 12: [31, 15.5], 24: [18, inf], 26: [28, 28.0], 33: [14, 14.0], 44: [25, 6.25] | oil 's iraq | Oil_reserves_in_Iraq |
| 163. | post | 10: [10, 5.0], 44: [10, inf] | post 's palestinian | Palestinians |
| 164. | haifa | 10: [11, inf] | haifa israeli israel | Israelis |
| 165. | abbas | 10: [12, inf], 16: [36, 9.0], 27: [15, 5.0] | abbas palestinian prime | Mahmoud_Abbas |
| 166. | annan | 11: [11, inf], 13: [11, 11.0], 34: [10, inf] | annan iraq kofi | Kofi_Annan |
| 167. | hong | 11: [13, 6.5], 50: [14, inf] | hong kong sars | Hong_Kong |
| 168. | kong | 11: [13, 6.5], 50: [14, inf] | kong hong sars | 2002–2004_SARS_outbreak |
| 169. | german | 11: [15, 5.0], 42: [13, 13.0], 50: [13, inf] | german 's germany | Germany |
| 170. | mexico | 11: [21, 21.0], 47: [23, inf], 49: [12, inf] | mexico 's world | Mexico |
| 171. | gain | 11: [11, inf] | gain 's iraq | Iraq |
| 172. | border | 11: [17, 8.5], 19: [12, 12.0], 22: [10, inf], 45: [16, 8.0] | border 's american | Canada–United_States_border |
| 173. | carrier | 11: [10, inf], 18: [10, 10.0] | carrier iraq 's | Nimitz-class_aircraft_carrier |
| 174. | tribunal | 11: [10, inf], 31: [13, 13.0] | tribunal crimes united | International_Military_Tribunal_for_the_Far_East |
| 175. | island | 11: [11, inf], 28: [11, 5.5] | island 's taiwan | Geography_of_Taiwan |
| 176. | prince | 11: [12, inf], 20: [12, inf] | prince saudi 's | Salman_of_Saudi_Arabia |
| 177. | canada | 11: [10, inf], 16: [12, 6.0], 27: [11, 11.0], 30: [10, 5.0], 32: [14, inf], 45: [10, inf] | canada 's canadian | Canada |
| 178. | orgn | 12: [17, inf] | orgn health world | .uk |
| 179. | york | 12: [20, 6.67], 16: [10, inf] | york iraq 's | Iraq_War |
| 180. | sons | 12: [15, 15.0], 15: [11, inf], 30: [40, inf] | sons hussein 's | Qusay_Hussein |
| 181. | leave | 12: [25, inf], 45: [15, 15.0] | leave 's iraq | Iraq_War |
| 182. | sars | 12: [13, inf], 37: [18, inf], 43: [10, inf] | sars health cases | 2002–2004_SARS_outbreak |
| 183. | thought | 12: [11, inf] | thought 's american | Thought |
| 184. | clear | 12: [12, inf], 46: [10, 5.0] | clear 's iraq | List_of_Congressional_opponents_of_the_Iraq_War |
| 185. | exile | 12: [12, inf], 15: [11, 5.5] | exile iraqi 's | Exile |
| 186. | command | 12: [16, inf], 36: [14, 7.0] | command iraq american | Revolutionary_Command_Council_(Iraq) |
| 187. | farmers | 12: [10, inf] | farmers 's trade | Farmers'_Produce_Trade_and_Commerce_(Promotion_and_Facilitation)_Act,_2020 |
| 188. | train | 12: [10, inf] | train american say | 50_Ways_to_Say_Goodbye |
| 189. | missile | 12: [33, 8.25], 24: [12, inf], 45: [11, 11.0] | missile iraq 's | Scud_missile |
| 190. | cruise | 12: [14, inf] | cruise american iraq | 1996_cruise_missile_strikes_on_Iraq |
| 191. | targets | 12: [19, 9.5], 20: [14, inf] | targets american iraq | American-led_intervention_in_Iraq_(2014–present) |
| 192. | unit | 12: [12, inf] | unit iraq 's | Multi-National_Force_–_Iraq |
| 193. | saudi | 12: [24, inf], 20: [76, 25.33], 26: [10, 5.0], 38: [20, 5.0] | saudi arabia 's | Saudi_Arabia |
| 194. | bunker | 12: [10, inf] | bunker hussein officials | Mount_Weather_Emergency_Operations_Center |
| 195. | defiance | 12: [10, inf] | defiance iraqi 's | 2003_invasion_of_Iraq |
| 196. | strike | 12: [35, 17.5], 24: [14, inf], 33: [13, 13.0], 43: [12, inf] | strike 's american | 2007–08_Writers_Guild_of_America_strike |
| 197. | basra | 12: [15, inf], 33: [15, 5.0] | basra iraq city | Basra |
| 198. | constitution | 12: [10, inf], 50: [10, inf] | constitution 's iraq | Constitution_of_Iraq |
| 199. | poll | 12: [10, inf], 44: [11, inf] | poll 's iraq | Iraq_War |
| 200. | surrender | 12: [16, inf] | surrender 's iraqi | 2003_invasion_of_Iraq |
| 201. | guard | 12: [10, inf], 29: [10, inf] | guard 's iraq | Republican_Guard_(Iraq) |
| 202. | videotape | 12: [10, inf] | videotape hussein says | Uday_Hussein |
| 203. | launched | 12: [12, inf] | launched 's iraq | Iran–Iraq_War |
| 204. | red | 12: [10, 5.0], 29: [15, inf] | red 's cross | International_Red_Cross_and_Red_Crescent_Movement |
| 205. | gear | 12: [10, inf] | gear american iraq | Withdrawal_of_U.S._troops_from_Iraq_(2020–21) |
| 206. | buildings | 12: [15, inf], 15: [23, 11.5] | buildings 's american | United_States_Capitol |
| 207. | bombardment | 12: [11, inf] | bombardment baghdad iraqi | Green_Zone |
| 208. | afghan | 12: [12, 6.0], 17: [16, 5.33], 21: [14, inf] | afghan afghanistan taliban | War_in_Afghanistan_(2001–present) |
| 209. | ruins | 12: [10, inf] | ruins 's iraq | Iraq |
| 210. | dissidents | 12: [11, inf] | dissidents 's cuba | Cuban_dissident_movement |
| 211. | patriot | 12: [10, inf] | patriot missile missiles | MIM-104_Patriot |
| 212. | fighters | 13: [22, 5.5], 46: [11, inf] | fighters iraq american | American-led_intervention_in_Iraq_(2014–present) |
| 213. | battle | 13: [43, 8.6], 18: [10, inf] | battle 's american | List_of_American_Civil_War_battles |
| 214. | ambushes | 13: [11, inf] | ambushes american soldiers | Tongo_Tongo_ambush |
| 215. | convoy | 13: [13, inf], 26: [24, 24.0], 51: [10, inf] | convoy american iraq | 2004_Iraq_KBR_convoy_ambush |
| 216. | najaf | 13: [33, inf], 35: [13, 6.5] | najaf iraqi iraq | Najaf |
| 217. | armor | 13: [11, inf] | armor iraq baghdad | Battle_of_Baghdad_(2003) |
| 218. | inside | 13: [10, 5.0], 40: [12, inf] | inside 's iraq | 2003_invasion_of_Iraq |
| 219. | symptoms | 13: [10, inf] | symptoms sars disease | Severe_acute_respiratory_syndrome |
| 220. | relief | 13: [16, 16.0], 43: [10, inf] | relief iraq 's | Iraq_Relief_and_Reconstruction_Fund |
| 221. | tells | 13: [11, 5.5], 20: [11, inf] | tells iraq 's | Iraq_War |
| 222. | committee | 13: [12, 12.0], 25: [24, inf] | committee iraq 's | Committee_for_the_Liberation_of_Iraq |
| 223. | delays | 13: [10, inf] | delays iraq 's | 2003_invasion_of_Iraq |
| 224. | postwar | 13: [16, inf], 28: [11, 11.0], 37: [15, 7.5] | postwar iraq 's | Iran–Iraq_War |
| 225. | skirmishes | 13: [11, inf] | skirmishes iraqi baghdad | Battle_of_Baghdad_(2003) |
| 226. | thrust | 13: [12, inf] | thrust baghdad 's | 2003_Baghdad_DHL_attempted_shootdown_incident |
| 227. | paramilitary | 13: [10, inf] | paramilitary american 's | Special_Activities_Center |
| 228. | india | 13: [12, inf], 22: [15, 7.5], 26: [26, 26.0], 29: [10, 5.0], 33: [10, 10.0] | india 's world | Mister_India_World |
| 229. | passengers | 13: [14, inf], 19: [15, 7.5] | passengers 's flights | Longest_flights |
| 230. | franks | 14: [11, inf], 28: [11, inf] | franks iraq 's | Tommy_Franks |
| 231. | bombings | 14: [11, inf], 20: [17, inf], 33: [10, inf], 44: [14, 7.0], 46: [13, inf] | bombings suicide 's | Suicide_attack |
| 232. | informant | 14: [10, inf] | informant hussein 's | Uday_Hussein |
| 233. | rabin | 14: [12, inf] | rabin informant israel | USS_Liberty_incident |
| 234. | driver | 14: [10, inf] | driver iraqi american | Foreign_hostages_in_Iraq |
| 235. | complete | 14: [10, inf] | complete iraq 's | Occupation_of_Iraq_(2003–2011) |
| 236. | -- | 14: [18, 6.0], 23: [14, 14.0], 37: [13, inf], 45: [14, 7.0] | -- 's iraq | 2003_invasion_of_Iraq |
| 237. | fleeing | 14: [11, inf] | fleeing iraq hussein | Uday_Hussein |
| 238. | agrees | 14: [11, inf] | agrees 's iraq | 2003_invasion_of_Iraq |
| 239. | arrest | 14: [17, 5.67], 38: [12, inf] | arrest 's police | Arrest |
| 240. | programs | 14: [14, 14.0], 19: [21, 10.5], 21: [14, inf], 51: [11, inf] | programs 's weapons | North_Korea_and_weapons_of_mass_destruction |
| 241. | bushmen | 14: [10, inf] | bushmen san south | San_people |
| 242. | african | 14: [14, inf] | african africa 's | Africa |
| 243. | information | 14: [11, 5.5], 28: [16, inf], 40: [15, 7.5] | information 's iraq | List_of_Iraqi_Information_Ministers |
| 244. | milosevic | 14: [10, inf], 17: [10, inf] | milosevic trial former | Trial_of_Slobodan_Milošević |
| 245. | airport | 14: [42, inf] | airport 's baghdad | Baghdad_International_Airport |
| 246. | order | 15: [26, 5.2], 44: [13, inf] | order iraq 's | 2003_invasion_of_Iraq_order_of_battle |
| 247. | hits | 15: [10, inf] | hits 's iraqi | Hit,_Iraq |
| 248. | moved | 15: [10, inf], 19: [11, inf] | moved 's iraq | 2003_invasion_of_Iraq |
| 249. | palace | 15: [11, inf], 48: [10, 10.0] | palace 's hussein | Uday_Hussein |
| 250. | differences | 15: [11, inf] | differences iraq 's | 2003_invasion_of_Iraq |
| 251. | fall | 15: [25, 6.25], 21: [14, inf], 45: [12, 6.0] | fall 's iraq | Iraq_War |
| 252. | looting | 15: [37, inf] | looting 's iraq | Archaeological_looting_in_Iraq |
| 253. | fallen | 15: [10, inf] | fallen 's iraqi | Iran–Iraq_War |
| 254. | fell | 15: [13, inf] | fell 's american | Norman_Fell |
| 255. | urges | 15: [16, 8.0], 36: [11, inf] | urges 's iraq | Iran–Iraq_War |
| 256. | alert | 15: [11, inf], 21: [20, inf] | alert 's iraq | Islamic_State_of_Iraq_and_the_Levant |
| 257. | rule | 15: [27, 5.4], 21: [14, 7.0], 44: [11, 11.0], 50: [12, inf] | rule 's iraq | Ba'athist_Iraq |
| 258. | putin | 15: [11, inf], 20: [26, 13.0], 44: [25, 12.5], 49: [19, 6.33] | putin russia 's | Russia_under_Vladimir_Putin |
| 259. | grip | 15: [11, inf] | grip 's hussein | Saddam_Hussein |
| 260. | infected | 15: [12, inf], 21: [10, 10.0] | infected sars disease | 2002–2004_SARS_outbreak |
| 261. | looters | 15: [12, inf] | looters 's american | Looting |
| 262. | beijing | 15: [13, inf], 28: [10, inf] | beijing china 's | Beijing |
| 263. | tikrit | 15: [11, inf] | tikrit hussein 's | Tikrit |
| 264. | refugees | 15: [10, inf], 35: [12, inf] | refugees 's iraq | Refugees_of_Iraq |
| 265. | museum | 15: [10, inf], 18: [22, 11.0] | museum 's iraq | National_Museum_of_Iraq |
| 266. | syria | 16: [99, 7.62], 41: [31, 7.75], 49: [18, inf] | syria iraq 's | Iraq–Syria_relations |
| 267. | liberal | 16: [10, inf] | liberal 's party | Liberal_Party |
| 268. | rate | 16: [12, inf] | rate 's percent | List_of_countries_by_obesity_rate |
| 269. | jenin | 16: [14, inf] | jenin israeli palestinian | Battle_of_Jenin_(2002) |
| 270. | policy | 16: [15, inf], 41: [12, 12.0] | policy 's iraq | Foreign_policy_of_the_Barack_Obama_administration |
| 271. | sanctions | 16: [24, inf], 19: [27, 5.4], 26: [10, 10.0], 33: [12, inf], 41: [11, inf], 51: [10, inf] | sanctions iraq 's | Sanctions_against_Iraq |
| 272. | mayor | 16: [10, inf] | mayor 's city | Mayor_of_New_York_City |
| 273. | penalties | 16: [12, inf] | penalties north bush | George_H._W._Bush |
| 274. | create | 16: [10, inf] | create 's iraq | Iraq |
| 275. | families | 16: [12, 6.0], 45: [13, inf] | families 's iraq | Iraq |
| 276. | business | 16: [15, 7.5], 46: [13, inf], 49: [12, inf] | business 's iraq | Iraq_War |
| 277. | particularly | 16: [11, inf] | particularly 's iraq | Iraq_War |
| 278. | achille | 16: [11, inf] | achille american abbas | Achille_Lauro_hijacking |
| 279. | lauro | 16: [11, inf] | lauro american abbas | Achille_Lauro_hijacking |
| 280. | pipeline | 16: [11, inf] | pipeline oil iraq | Kirkuk–Ceyhan_Oil_Pipeline |
| 281. | crowd | 16: [11, inf] | crowd 's soldiers | Crowd_manipulation |
| 282. | lift | 16: [12, inf] | lift sanctions 's | United_States_sanctions |
| 283. | tariq | 17: [14, inf] | tariq 's iraqi | Tariq_Aziz |
| 284. | aziz | 17: [18, inf] | aziz 's iraqi | Tariq_Aziz |
| 285. | theft | 17: [14, inf] | theft 's former | Theft |
| 286. | opening | 17: [10, inf] | opening 's iraq | Iraq |
| 287. | scientist | 17: [10, inf] | scientist iraq 's | Iran–Iraq_War |
| 288. | percent | 17: [13, 13.0], 29: [12, 6.0], 32: [11, inf], 49: [12, 6.0] | percent 's government | Federal_government_of_the_United_States |
| 289. | fraud | 17: [25, inf] | fraud 's charges | Fraud |
| 290. | schools | 17: [15, 7.5], 21: [12, 12.0], 46: [12, inf] | schools 's children | Children's_literature |
| 291. | mandela | 17: [10, inf] | mandela south africa | Nelson_Mandela |
| 292. | visit | 17: [12, inf], 47: [25, 5.0] | visit 's bush | George_W._Bush |
| 293. | birthday | 18: [10, inf], 37: [11, inf] | birthday 's north | Washington's_Birthday |
| 294. | steps | 18: [10, inf], 33: [11, 11.0] | steps 's israel | Israel |
| 295. | vajpayee | 18: [11, inf] | vajpayee india prime | List_of_prime_ministers_of_India |
| 296. | bar | 18: [10, inf] | bar 's plan | Bar_Bar_Bar |
| 297. | italy | 18: [13, inf], 40: [14, 7.0], 43: [24, 6.0] | italy europe world | Italy |
| 298. | common | 18: [12, inf] | common 's iraq | Iraq_War |
| 299. | newspaper | 18: [11, inf], 38: [18, 9.0] | newspaper 's world | List_of_newspapers_by_circulation |
| 300. | transition | 18: [10, inf] | transition 's iraq | Iraqi_Transitional_Government |
| 301. | falluja | 18: [10, inf] | falluja american iraq | Fallujah |
| 302. | tel | 18: [12, inf] | tel aviv israeli | Tel_Aviv |
| 303. | aviv | 18: [12, inf] | aviv tel israeli | Tel_Aviv |
| 304. | rules | 18: [10, inf] | rules 's court | Merrick_Garland_Supreme_Court_nomination |
| 305. | relapses | 18: [10, inf] | relapses patients sars | Gilteritinib |
| 306. | earthquake | 18: [13, inf] | earthquake people least | 2011_Sikkim_earthquake |
| 307. | u.n. | 19: [13, inf], 34: [26, 8.67], 42: [12, 6.0] | u.n. iraq united | 2003_invasion_of_Iraq |
| 308. | shortages | 19: [13, inf], 33: [13, 13.0] | shortages iraq 's | Iran–Iraq_War |
| 309. | envoy | 19: [15, 5.0], 21: [10, inf], 47: [12, 12.0] | envoy 's iraq | Brett_McGurk |
| 310. | finds | 19: [10, 10.0], 39: [11, inf], 44: [10, inf] | finds 's iraq | 2003_invasion_of_Iraq |
| 311. | resolution | 19: [21, 7.0], 31: [18, inf] | resolution iraq council | Authorization_for_Use_of_Military_Force_Against_Iraq_Resolution_of_2002 |
| 312. | armitage | 19: [11, inf] | armitage state bush | Richard_Armitage_(government_official) |
| 313. | fund | 19: [11, inf], 29: [10, 10.0] | fund 's iraq | Development_Fund_for_Iraq |
| 314. | youths | 19: [10, inf] | youths programs israeli | Gadna_(Israel) |
| 315. | khatami | 20: [11, inf] | khatami iran 's | Mohammad_Khatami |
| 316. | arrives | 20: [11, inf] | arrives iraq 's | 2003_invasion_of_Iraq |
| 317. | truck | 20: [12, 6.0], 34: [10, inf] | truck iraq 's | Gun_truck |
| 318. | riyadh | 20: [29, inf] | riyadh saudi arabia | Riyadh |
| 319. | membership | 20: [11, inf] | membership european 's | 2016_United_Kingdom_European_Union_membership_referendum |
| 320. | republic | 20: [18, 9.0], 24: [13, inf] | republic 's czech | Czech_Republic |
| 321. | go | 20: [11, inf] | go 's iraq | Iraq_War |
| 322. | arabs | 20: [11, inf], 45: [10, 5.0] | arabs 's iraq | Iraqis |
| 323. | menem | 20: [12, inf] | menem 's argentine | Carlos_Menem |
| 324. | bali | 20: [12, inf], 32: [14, inf] | bali indonesia islamic | Bali |
| 325. | race | 20: [11, inf] | race 's party | Republican_Party_(United_States) |
| 326. | raid | 20: [10, 10.0], 26: [10, 10.0], 50: [10, inf] | raid israeli 's | Raid_on_Entebbe_(film) |
| 327. | bomber | 20: [12, inf] | bomber suicide israeli | Use_of_child_suicide_bombers_by_Palestinian_militant_groups |
| 328. | reportedly | 21: [19, 6.33], 35: [11, inf] | reportedly 's iraq | 2003_invasion_of_Iraq |
| 329. | sharply | 21: [11, inf] | sharply 's iraq | Iraq_and_weapons_of_mass_destruction |
| 330. | ban | 21: [20, 10.0], 26: [10, 10.0], 45: [10, inf] | ban 's world | Ban_Ki-moon |
| 331. | lawyers | 21: [12, inf] | lawyers 's court | Lawyer |
| 332. | companies | 21: [10, 5.0], 24: [10, inf], 26: [12, 12.0], 40: [13, inf], 49: [10, 10.0] | companies iraq 's | Iraq_Petroleum_Company |
| 333. | mad | 21: [18, inf] | mad cow disease | Bovine_spongiform_encephalopathy |
| 334. | cow | 21: [38, inf] | cow mad disease | Bovine_spongiform_encephalopathy |
| 335. | beef | 21: [14, inf] | beef cow canadian | Beef_cattle |
| 336. | afghanistan | 21: [18, 18.0], 27: [11, inf], 35: [25, 6.25] | afghanistan taliban 's | Islamic_Emirate_of_Afghanistan |
| 337. | ranch | 21: [11, inf] | ranch bush cow | Cowboy |
| 338. | technology | 21: [11, inf] | technology 's nuclear | Nuclear_technology |
| 339. | expert | 21: [10, 10.0], 29: [14, inf] | expert 's weapons | David_Kelly_(weapons_expert) |
| 340. | pole | 21: [10, inf] | pole north 's | North_Pole |
| 341. | liquor | 21: [10, inf] | liquor iraq 's | Gang_presence_in_the_United_States_military |
| 342. | costa | 21: [11, inf] | costa programs academy | Academy_at_Dundee_Ranch |
| 343. | academy | 21: [15, inf] | academy american costa | Costa-Gavras |
| 344. | send | 22: [15, 5.0], 34: [17, inf] | send iraq troops | American-led_intervention_in_Iraq_(2014–present) |
| 345. | climbers | 22: [11, inf] | climbers everest may | List_of_people_who_died_climbing_Mount_Everest |
| 346. | sherpa | 22: [10, inf] | sherpa climbers katmandu | 1953_British_Mount_Everest_expedition |
| 347. | poland | 22: [19, inf], 51: [14, 7.0] | poland 's europe | Poland_in_the_European_Union |
| 348. | arrests | 22: [11, inf], 26: [15, 7.5] | arrests police 's | Arrest |
| 349. | panel | 22: [10, inf], 28: [10, inf], 43: [13, inf] | panel iraq 's | 2003_invasion_of_Iraq |
| 350. | colombia | 22: [12, inf], 38: [19, inf] | colombia 's rebels | Revolutionary_Armed_Forces_of_Colombia |
| 351. | south | 22: [16, inf] | south korea north | North_Korea–South_Korea_relations |
| 352. | mass | 22: [14, inf] | mass iraq weapons | Iraq_and_weapons_of_mass_destruction |
| 353. | destruction | 22: [12, inf] | destruction iraq weapons | Iraq_and_weapons_of_mass_destruction |
| 354. | geneva | 22: [14, 14.0], 49: [12, inf] | geneva iraq would | Geneva_Conventions |
| 355. | sake | 22: [12, inf] | sake 's us | Sake |
| 356. | main | 23: [10, inf] | main 's iraq | 2003_invasion_of_Iraq |
| 357. | statements | 23: [11, inf] | statements 's korea | South_Korea |
| 358. | zone | 23: [10, inf], 29: [11, inf] | zone iraq 's | Saudi_Arabian–Iraqi_neutral_zone |
| 359. | jerusalem | 23: [14, 14.0], 34: [15, inf] | jerusalem palestinian israeli | East_Jerusalem |
| 360. | joining | 24: [12, inf] | joining 's union | Soviet_Union |
| 361. | faces | 24: [10, inf] | faces 's iraq | Iran–Iraq_War |
| 362. | chief | 24: [12, 6.0], 34: [13, inf] | chief 's iraq | Iraq_War |
| 363. | art | 24: [12, inf] | art 's museum | Museum_of_Modern_Art |
| 364. | ships | 24: [10, inf] | ships 's north | List_of_active_ships_of_the_Korean_People's_Navy |
| 365. | land | 24: [14, inf] | land 's iraq | Iraq |
| 366. | marriage | 24: [10, inf], 31: [18, inf] | marriage gay same-sex | Same-sex_marriage |
| 367. | areas | 24: [13, inf] | areas 's palestinian | West_Bank_Areas_in_the_Oslo_II_Accord |
| 368. | czech | 24: [15, inf] | czech republic europe | Czech_Republic |
| 369. | prisoner | 24: [12, inf] | prisoner prisoners israel | Palestinian_prisoners_of_Israel |
| 370. | senate | 25: [10, inf], 40: [13, 6.5], 42: [10, inf] | senate iraq 's | Senate_of_Iraq |
| 371. | rejects | 25: [10, inf], 37: [10, 5.0] | rejects 's iraq | Iraq_War |
| 372. | cease-fire | 25: [18, 6.0], 47: [10, inf] | cease-fire palestinian 's | Israeli–Palestinian_conflict |
| 373. | basque | 25: [16, inf] | basque spain spanish | Basque_Country_(autonomous_community) |
| 374. | evidence | 26: [19, 6.33], 50: [12, inf] | evidence iraq 's | Iraq_War |
| 375. | syrian | 26: [14, inf], 29: [15, 5.0], 41: [13, inf] | syrian syria iraq | Ba'ath_Party_(Syrian-dominated_faction) |
| 376. | liberia | 26: [14, inf], 47: [12, inf] | liberia taylor 's | Charles_Taylor_(Liberian_politician) |
| 377. | charles | 26: [11, inf] | charles taylor liberia | Charles_Taylor_(Liberian_politician) |
| 378. | taylor | 26: [13, inf] | taylor liberia pres | Charles_Taylor_(Liberian_politician) |
| 379. | musharraf | 26: [14, inf] | musharraf pakistan 's | Pervez_Musharraf |
| 380. | mosque | 27: [32, inf] | mosque 's shiite | Ar-Rahman_Mosque_(Pyongyang) |
| 381. | internal | 27: [15, inf] | internal 's security | Internal_security |
| 382. | spokesman | 28: [11, inf] | spokesman 's says | The_Spokesman-Review |
| 383. | congress | 28: [13, 13.0], 39: [10, 5.0], 49: [12, inf] | congress iraq 's | Iraqi_National_Congress |
| 384. | electric | 28: [10, inf] | electric power iraq | List_of_power_stations_in_Iraq |
| 385. | interim | 28: [12, inf] | interim iraq iraqi | Iraq_War |
| 386. | agreed | 28: [14, inf] | agreed iraq 's | Authorization_for_Use_of_Military_Force_Against_Iraq_Resolution_of_2002 |
| 387. | allied | 28: [11, 5.5], 49: [11, inf] | allied iraq forces | Iraqi_Armed_Forces |
| 388. | twins | 28: [11, inf] | twins father 's | Twin |
| 389. | mbeki | 28: [11, inf] | mbeki south pres | Thabo_Mbeki |
| 390. | uranium | 28: [24, inf] | uranium nuclear iraq | Niger_uranium_forgeries |
| 391. | body | 28: [10, inf], 33: [11, inf] | body 's iraq | Iraq_Body_Count_project |
| 392. | buy | 28: [10, inf] | buy 's iraq | Iran–Iraq_War |
| 393. | immigrants | 28: [10, inf], 43: [11, inf] | immigrants 's italy | Italian_diaspora |
| 394. | dispute | 29: [15, inf] | dispute 's iraq | Disputed_territories_of_Northern_Iraq |
| 395. | drought | 29: [10, inf] | drought 's aid | Drought |
| 396. | singapore | 29: [11, 5.5], 37: [14, inf] | singapore sars 's | 2002–2004_SARS_outbreak |
| 397. | missions | 30: [10, inf] | missions iraq forces | Multi-National_Force_–_Iraq |
| 398. | sandwich | 30: [10, inf] | sandwich 's family | Cuban_sandwich |
| 399. | uday | 30: [19, inf] | uday hussein 's | Uday_Hussein |
| 400. | qusay | 30: [19, inf] | qusay hussein 's | Qusay_Hussein |
| 401. | spain | 30: [10, inf], 45: [14, inf], 48: [15, 5.0] | spain world 's | Spain_during_World_War_II |
| 402. | tourists | 30: [11, inf] | tourists 's world | The_Tourists |
| 403. | library | 30: [10, inf] | library books oil | Oil! |
| 404. | gay | 31: [20, inf] | gay marriage 's | Same-sex_marriage |
| 405. | village | 31: [10, 10.0], 39: [12, inf], 47: [10, 5.0] | village 's map | Map |
| 406. | rwanda | 31: [16, inf] | rwanda world briefing | Healthcare_in_Rwanda |
| 407. | prosecutor | 31: [14, inf] | prosecutor 's court | Prosecutor |
| 408. | marriages | 31: [10, inf] | marriages marriage gay | Same-sex_marriage |
| 409. | jakarta | 32: [16, inf] | jakarta indonesia indonesian | COVID-19_pandemic_in_Indonesia |
| 410. | cantat | 32: [10, inf] | cantat france french | Bertrand_Cantat |
| 411. | small | 32: [11, inf], 45: [10, inf] | small 's say | Never_Say_Never_Again |
| 412. | jordanian | 32: [11, inf] | jordanian iraqi 's | Arab_Federation |
| 413. | jemaah | 32: [11, inf] | jemaah group islamiyah | Jemaah_Islamiyah |
| 414. | islamiyah | 32: [11, inf] | islamiyah group jemaah | Jemaah_Islamiyah |
| 415. | mr. | 32: [14, inf] | mr. 's president | Mr._President_(title) |
| 416. | canadian | 32: [10, inf], 40: [10, 5.0], 45: [11, inf] | canadian canada 's | Canadians |
| 417. | led | 33: [11, inf] | led 's iraq | American-led_intervention_in_Iraq_(2014–present) |
| 418. | proposal | 33: [10, inf] | proposal iraq 's | Proposals_for_Assyrian_autonomy_in_Iraq |
| 419. | incident | 33: [10, inf] | incident 's american | 1954_United_States_Capitol_shooting |
| 420. | israelis | 33: [17, 5.67], 49: [12, inf] | israelis palestinian israeli | Israeli–Palestinian_conflict |
| 421. | blow | 33: [10, inf] | blow 's iraq | Iran–Iraq_War |
| 422. | libya | 33: [25, inf], 51: [26, inf] | libya sanctions 's | Iran_and_Libya_Sanctions_Act |
| 423. | lockerbie | 33: [11, inf] | lockerbie libya sanctions | Pan_Am_Flight_103 |
| 424. | bbc | 33: [16, inf] | bbc 's blair | Lionel_Blair |
| 425. | action | 34: [12, inf] | action iraq 's | 2003_invasion_of_Iraq |
| 426. | questions | 34: [11, inf] | questions 's iraq | Iraq_War |
| 427. | cards | 34: [10, inf] | cards 's fake | Steam_Trading_Cards |
| 428. | head | 34: [12, inf] | head 's iraq | Iraq_War |
| 429. | soft | 34: [10, inf] | soft 's korean | Soft_power |
| 430. | charities | 34: [11, inf] | charities hamas 's | List_of_charities_accused_of_ties_to_terrorism |
| 431. | iran | 35: [25, 5.0], 50: [15, inf] | iran 's iraq | Iran–Iraq_War |
| 432. | bombs | 35: [11, inf] | bombs 's american | U.S._Bombs |
| 433. | al-hakim | 35: [10, inf] | al-hakim iraq shiite | Mohammad_Baqir_al-Hakim |
| 434. | shiite | 35: [20, 5.0], 41: [16, inf] | shiite iraq 's | Faisal_I_of_Iraq |
| 435. | holy | 35: [15, inf] | holy 's iraq | Iran–Iraq_War |
| 436. | lindbergh | 35: [12, inf] | lindbergh family bouteuil | Charles_Lindbergh |
| 437. | bakr | 35: [10, inf] | bakr iraq 's | Abu_Bakr_al-Baghdadi |
| 438. | submarine | 35: [10, inf] | submarine accident china | Chinese_submarine_361 |
| 439. | interview | 36: [10, inf], 38: [18, inf], 49: [10, 5.0] | interview 's says | The_Interview |
| 440. | chinese | 36: [15, inf], 38: [22, 11.0] | chinese china 's | China |
| 441. | chocolate | 36: [10, inf] | chocolate cocoa paris | Chocolate |
| 442. | qurei | 37: [23, inf] | qurei palestinian arafat | Ahmed_Qurei |
| 443. | developing | 37: [15, inf] | developing 's world | Developed_country |
| 444. | democrats | 37: [11, 11.0], 44: [10, inf] | democrats 's bush | Blue_Dog_Coalition |
| 445. | subsidies | 37: [25, inf] | subsidies trade world | Subsidy |
| 446. | swedish | 37: [10, inf] | swedish lindh foreign | Anna_Lindh |
| 447. | anna | 37: [10, inf] | anna lindh european | Anna_Lindh |
| 448. | lindh | 37: [13, inf] | lindh swedish foreign | Anna_Lindh |
| 449. | asylum | 37: [12, inf] | asylum britain world | Right_of_asylum |
| 450. | tibet | 38: [12, inf] | tibet chinese china | Annexation_of_Tibet_by_the_People's_Republic_of_China |
| 451. | tibetans | 38: [10, inf] | tibetans chinese tibet | Tibet_Autonomous_Region |
| 452. | making | 38: [10, inf] | making 's iraq | Iraq_War |
| 453. | increasingly | 38: [10, inf] | increasingly 's iraq | 2003_invasion_of_Iraq |
| 454. | robert | 38: [10, inf] | robert zimbabwe 's | Zimbabwe |
| 455. | jacques | 38: [10, inf] | jacques chirac france | Jacques_Chirac |
| 456. | big | 38: [11, inf] | big 's iraq | Iraq |
| 457. | allowed | 38: [10, inf] | allowed 's iraq | Iraq |
| 458. | divorce | 38: [12, inf] | divorce italy 's | Divorce_Italian_Style |
| 459. | compound | 39: [12, inf] | compound iraqi iraq | Iraq_War |
| 460. | bremer | 39: [17, inf], 46: [13, 6.5] | bremer iraq american | Paul_Bremer |
| 461. | aids | 39: [11, inf], 46: [24, 24.0] | aids africa bush | Barbara_Bush_(born_1981) |
| 462. | reserve | 39: [11, inf] | reserve iraq pentagon | Pentagon_Papers |
| 463. | leak | 40: [14, inf] | leak 's bush | LiveLeak |
| 464. | defectors | 40: [12, inf] | defectors north iraq | Islamic_State_of_Iraq_and_the_Levant |
| 465. | cardinal | 40: [13, inf] | cardinal pope 's | Pope_Francis |
| 466. | / | 41: [11, inf] | / 's attacks | Denial-of-service_attack |
| 467. | southeast | 41: [11, inf] | southeast 's asia | Southeast_Asia |
| 468. | harbor | 41: [12, inf] | harbor bush 's | The_New_Pearl_Harbor |
| 469. | nobel | 41: [16, inf] | nobel prize 's | Nobel_Prize_in_Literature |
| 470. | prize | 41: [17, inf] | prize 's nobel | Nobel_Prize |
| 471. | turkish | 41: [14, inf], 47: [21, 7.0] | turkish turkey iraq | Iraq–Turkey_relations |
| 472. | car | 41: [12, inf], 50: [16, 16.0] | car killed attack | Charlottesville_car_attack |
| 473. | portugal | 41: [11, inf] | portugal 's european | Portugal |
| 474. | models | 41: [10, inf] | models 's fashion | List_of_Victoria's_Secret_models |
| 475. | ebadi | 41: [11, inf] | ebadi rights prize | Shirin_Ebadi |
| 476. | protesters | 42: [11, inf], 46: [11, inf] | protesters 's iraq | Protests_against_the_Iraq_War |
| 477. | bolivia | 42: [20, inf] | bolivia 's sanchez | Gonzalo_Sánchez_de_Lozada |
| 478. | gonzalo | 42: [11, inf] | gonzalo bolivia sanchez | Gonzalo_Sánchez_de_Lozada |
| 479. | sanchez | 42: [16, inf] | sanchez 's iraq | Ricardo_Sanchez |
| 480. | nation | 42: [10, inf] | nation 's iraq | Sanctions_against_Iraq |
| 481. | lozada | 42: [14, inf] | lozada 's bolivia | Gonzalo_Sánchez_de_Lozada |
| 482. | welfare | 42: [12, inf] | welfare 's bush | George_W._Bush |
| 483. | mother | 42: [10, inf] | mother 's family | Mother's_Day |
| 484. | teresa | 42: [10, inf] | teresa mother pope | Mother_Teresa |
| 485. | sudan | 43: [15, inf] | sudan peace africa | Israel–Sudan_normalization_agreement |
| 486. | killings | 43: [10, inf] | killings 's two | ReMastered:_The_Two_Killings_of_Sam_Cooke |
| 487. | workers | 43: [11, inf] | workers 's government | Workers'_compensation |
| 488. | conservative | 44: [12, inf] | conservative 's party | Conservative_Party_(UK) |
| 489. | conservatives | 44: [11, inf] | conservatives 's iraq | Conservatism_in_the_United_States |
| 490. | iain | 44: [10, inf] | iain leader duncan | Iain_Duncan_Smith |
| 491. | duncan | 44: [15, inf] | duncan leader smith | Iain_Duncan_Smith |
| 492. | smith | 44: [15, inf] | smith leader duncan | Iain_Duncan_Smith |
| 493. | tories | 44: [10, inf] | tories party britain | Tories_(British_political_party) |
| 494. | leadership | 44: [10, inf] | leadership 's iraq | Iran–Iraq_War |
| 495. | secret | 44: [10, inf], 51: [10, inf] | secret 's iraq | Iraq_and_weapons_of_mass_destruction |
| 496. | suspends | 44: [10, inf] | suspends world briefing | Stephanie_Grisham |
| 497. | sent | 44: [11, inf] | sent 's iraq | 2003_invasion_of_Iraq |
| 498. | stock | 44: [12, inf] | stock 's us | List_of_stock_exchanges |
| 499. | sunday | 45: [10, inf] | sunday iraq 's | Iraq_War |
| 500. | cloning | 45: [12, inf] | cloning human ban | Human_cloning |
| 501. | greater | 45: [10, inf] | greater 's iraq | Islamic_State_of_Iraq_and_the_Levant |
| 502. | plant | 46: [10, inf], 50: [14, inf] | plant nuclear 's | Chernobyl_Nuclear_Power_Plant |
| 503. | generals | 46: [10, inf] | generals american 's | List_of_active_duty_United_States_four-star_officers |
| 504. | coming | 46: [12, inf] | coming 's iraq | 2003_invasion_of_Iraq |
| 505. | meets | 46: [12, inf] | meets iraq 's | Iraq_War |
| 506. | strategy | 46: [15, inf] | strategy iraq 's | U.S._kill_or_capture_strategy_in_Iraq |
| 507. | insurgency | 46: [11, inf] | insurgency american 's | Insurgency |
| 508. | elf | 46: [10, inf] | elf oil former | Elf_Aquitaine |
| 509. | botswana | 46: [10, inf] | botswana africa aids | HIV/AIDS_in_Botswana |
| 510. | church | 47: [11, inf] | church 's world | List_of_largest_church_buildings |
| 511. | aguilar | 47: [10, inf] | aguilar mexico envoy | Adolfo_Aguilar_Zínser |
| 512. | kifl | 47: [10, inf] | kifl village iraqi | Iraqi_revolt_of_1920 |
| 513. | thanksgiving | 48: [15, inf] | thanksgiving bush visit | List_of_international_presidential_trips_made_by_George_W._Bush |
| 514. | dinner | 48: [10, inf] | dinner bush iraq | Bush_shoeing_incident |
| 515. | clinton | 48: [12, inf] | clinton bush 's | Presidency_of_Bill_Clinton |
| 516. | samarra | 49: [10, inf] | samarra american says | Samarra |
| 517. | civilians | 49: [13, 6.5], 52: [10, inf] | civilians iraqi american | Casualties_of_the_Iraq_War |
| 518. | influence | 49: [10, inf] | influence 's iraq | Iraq |
| 519. | details | 49: [11, inf] | details 's iraq | Iraq |
| 520. | withdraw | 49: [11, inf] | withdraw 's iraq | Withdrawal_of_U.S._troops_from_Iraq_(2020–21) |
| 521. | jews | 49: [14, inf] | jews 's israel | Israeli_Jews |
| 522. | ministers | 49: [10, inf] | ministers 's iraq | Prime_Minister_of_Iraq |
| 523. | media | 49: [13, inf] | media 's news | News_media |
| 524. | veto | 49: [10, inf] | veto iraq resolution | War_Powers_Resolution |
| 525. | nuclear | 50: [15, inf] | nuclear north korea | North_Korea_and_weapons_of_mass_destruction |
| 526. | contracts | 50: [20, inf] | contracts iraq companies | Private_military_company |
| 527. | wall | 50: [13, inf] | wall 's says | Trump_wall |
| 528. | judge | 50: [11, inf] | judge 's court | United_States_district_court |
| 529. | halliburton | 50: [20, inf] | halliburton iraq 's | Halliburton |
| 530. | impact | 51: [10, inf] | impact 's iraq | Impact_of_the_COVID-19_pandemic |
| 531. | impose | 51: [10, inf] | impose north would | Gun_laws_in_North_Carolina |
| 532. | inquest | 51: [10, inf] | inquest diana death | Death_of_Diana,_Princess_of_Wales |
| 533. | immigration | 52: [10, inf] | immigration 's states | Immigration_to_the_United_States |
| 534. | toll | 52: [11, inf] | toll 's death | List_of_wars_and_anthropogenic_disasters_by_death_toll |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | powell | 6: [12, inf] | powell 's says | Sidney_Powell |
| 2. | path | 11: [16, inf] | path world 's | World_Trade_Center_station_(PATH) |
| 3. | hundred | 20: [32, inf] | hundred lives hamoodi | Allen_West_(politician) |
| 4. | lives | 20: [32, inf] | lives hundred hamoodi | Allen_West_(politician) |
| 5. | marine | 21: [14, inf], 23: [30, 15.0] | marine corporal sergeant | Corporal |
| 6. | st | 23: [10, inf] | st class private | Private_first_class |
