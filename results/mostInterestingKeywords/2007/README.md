# Keywords with the highest 'interestingness' in 2007

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
| 1. | russian | 2: [11, inf], 29: [17, inf], 33: [13, 6.5] | russian russia putin | Opposition_to_Vladimir_Putin_in_Russia |
| 2. | russia | 2: [14, inf], 12: [11, inf], 17: [21, 5.25], 22: [15, 5.0], 28: [15, 5.0], 35: [12, 6.0], 41: [10, 5.0] | russia putin russian | Vladimir_Putin |
| 3. | oil | 2: [19, inf] | oil iraqi law | Iraq_oil_law_(2007) |
| 4. | leaders | 2: [18, 9.0], 42: [11, inf] | leaders iraq president | President_of_Iraq |
| 5. | political | 2: [15, 7.5], 8: [10, 10.0], 16: [11, inf] | political president iraq | President_of_Iraq |
| 6. | court | 2: [11, inf], 5: [10, 10.0], 9: [20, 6.67], 47: [12, 6.0], 51: [11, 5.5] | court pakistan musharraf | Pervez_Musharraf |
| 7. | iranian | 2: [10, inf] | iranian iran iraq | Iran–Iraq_War |
| 8. | state | 2: [13, 6.5], 24: [12, inf], 44: [16, 16.0] | state rice secretary | Condoleezza_Rice |
| 9. | rice | 2: [11, inf] | rice state secretary | Condoleezza_Rice |
| 10. | ban | 3: [11, 11.0], 12: [10, inf] | ban u.n. ki-moon | Ban_Ki-moon |
| 11. | meeting | 3: [10, 5.0], 10: [17, inf], 22: [14, 14.0], 32: [10, 10.0], 45: [11, 5.5], 48: [10, 5.0] | meeting president leaders | Asia-Pacific_Economic_Cooperation |
| 12. | french | 3: [20, 10.0], 16: [14, inf] | french sarkozy president | Nicolas_Sarkozy |
| 13. | british | 3: [10, inf], 21: [16, 8.0], 34: [11, inf], 36: [10, inf] | british britain iraq | Mandatory_Iraq |
| 14. | progress | 3: [11, inf] | progress iraq u.s. | 2003_invasion_of_Iraq |
| 15. | gates | 3: [12, 6.0], 16: [22, inf], 23: [14, inf], 45: [11, inf], 49: [16, inf] | gates defense secretary | Robert_Gates |
| 16. | sunni | 3: [10, inf], 8: [17, 5.67], 24: [14, 7.0], 26: [16, 16.0], 37: [12, 12.0] | sunni iraq iraqi | Iraqi_conflict_(2003–present) |
| 17. | china | 3: [23, 5.75], 32: [11, inf], 35: [18, 9.0], 45: [12, 6.0], 49: [25, 6.25] | china chinese today | China |
| 18. | nuclear | 3: [14, inf], 15: [19, 9.5], 22: [18, inf], 25: [16, 5.33] | nuclear iran north | Nuclear_program_of_Iran |
| 19. | north | 3: [11, inf], 28: [26, inf], 36: [12, 6.0], 40: [10, 5.0] | north korea nuclear | North_Korea_and_weapons_of_mass_destruction |
| 20. | talks | 3: [10, 5.0], 22: [19, 9.5], 25: [22, inf] | talks u.s. peace | Afghan_peace_process |
| 21. | test | 3: [10, inf] | test china space | Chinese_space_program |
| 22. | killing | 4: [19, 9.5], 16: [12, inf], 27: [10, 10.0], 52: [10, 10.0] | killing police least | Killing_of_George_Floyd |
| 23. | journalist | 4: [11, inf], 15: [12, 6.0] | journalist killed russian | List_of_journalists_killed_in_Russia |
| 24. | lebanon | 4: [17, 8.5], 13: [10, inf] | lebanon american officials | Lebanese_people |
| 25. | began | 4: [12, inf] | began today u.s. | Today_(American_TV_program) |
| 26. | beirut | 4: [11, inf] | beirut lebanon killed | 2020_Beirut_explosion |
| 27. | rape | 4: [11, inf], 8: [17, inf] | rape president charges | Jacob_Zuma |
| 28. | charges | 4: [15, 7.5], 38: [12, inf], 51: [11, 11.0] | charges president former | Jacob_Zuma |
| 29. | suicide | 4: [12, inf] | suicide bomber killed | Female_suicide_bomber |
| 30. | nato | 4: [11, inf] | nato afghan taliban | Taliban_insurgency |
| 31. | india | 4: [13, inf], 8: [14, inf] | india indian nuclear | India_and_weapons_of_mass_destruction |
| 32. | near | 5: [11, inf] | near killed iraqi | ISIL_insurgency_in_Iraq_(2017–present) |
| 33. | battle | 5: [12, 6.0], 20: [10, inf], 28: [17, inf] | battle forces killed | Killed_in_action |
| 34. | palestinian | 5: [12, inf], 17: [12, 12.0], 28: [21, 5.25] | palestinian hamas gaza | Hamas |
| 35. | chirac | 5: [10, inf] | chirac president jacques | Jacques_Chirac |
| 36. | indonesia | 6: [12, inf] | indonesia flu virus | Avian_influenza |
| 37. | part | 7: [10, inf] | part american iraq | Iraq |
| 38. | intelligence | 7: [24, 6.0], 49: [17, inf] | intelligence american iran | Iran–United_States_relations |
| 39. | trial | 7: [11, 5.5], 34: [15, inf] | trial court former | Nuremberg_trials |
| 40. | assertions | 7: [12, inf] | assertions american officials | American_Civil_War |
| 41. | together | 8: [11, inf] | together iraq minister | Iraq |
| 42. | peace | 8: [11, 5.5], 10: [11, inf], 36: [11, 5.5] | peace talks israeli | 2010–11_Israeli–Palestinian_peace_talks |
| 43. | since | 9: [10, inf] | since first iraq | Iraq |
| 44. | japan | 10: [15, 15.0], 29: [14, inf], 37: [12, 6.0] | japan minister prime | Prime_Minister_of_Japan |
| 45. | hamas | 10: [14, 14.0], 20: [17, 8.5], 48: [10, inf], 50: [11, 11.0] | hamas gaza palestinian | Hamas |
| 46. | across | 10: [10, inf] | across iraq american | Iraqi_Americans |
| 47. | zimbabwe | 11: [10, inf] | zimbabwe opposition mugabe | Robert_Mugabe |
| 48. | police | 11: [26, 13.0], 39: [10, inf], 45: [22, 7.33] | police officers british | List_of_British_police_officers_killed_in_the_line_of_duty |
| 49. | sanctions | 11: [10, inf], 38: [12, 6.0] | sanctions iran nuclear | Sanctions_against_Iran |
| 50. | party | 12: [10, inf] | party minister prime | Prime_Minister_of_the_United_Kingdom |
| 51. | secretary | 12: [17, 17.0], 16: [11, inf], 49: [14, inf] | secretary gates rice | Robert_Gates |
| 52. | return | 12: [10, 10.0], 42: [12, inf] | return pakistan prime | List_of_prime_ministers_of_Pakistan |
| 53. | children | 12: [10, 10.0], 50: [10, inf] | children workers two | Two-child_policy |
| 54. | jamaica | 12: [10, inf] | jamaica cricket coach | Courtney_Walsh |
| 55. | ki-moon | 12: [10, inf] | ki-moon u.n. ban | Ban_Ki-moon |
| 56. | cricket | 12: [14, inf] | cricket coach police | Bob_Woolmer |
| 57. | coach | 12: [13, inf] | coach cricket police | Bob_Woolmer |
| 58. | hong | 12: [12, inf] | hong kong china | Hong_Kong |
| 59. | kong | 12: [12, inf] | kong hong china | Hong_Kong |
| 60. | army | 13: [11, 5.5], 17: [10, inf] | army military israeli | Israel_Defense_Forces |
| 61. | arab | 13: [12, inf] | arab sunni israel | Arab_states–Israeli_alliance_against_Iran |
| 62. | shiite | 13: [13, 6.5], 24: [13, inf] | shiite iraq iraqi | Sons_of_Iraq |
| 63. | pelosi | 14: [11, inf] | pelosi syria house | Nancy_Pelosi |
| 64. | visit | 14: [12, inf], 19: [13, inf] | visit president bush | George_W._Bush |
| 65. | afghanistan | 15: [18, 9.0], 38: [10, inf] | afghanistan taliban afghan | War_in_Afghanistan_(2001–present) |
| 66. | korea | 15: [28, 7.0], 28: [20, 10.0], 35: [16, 5.33], 40: [10, 5.0], 49: [10, inf] | korea north south | North_Korea–South_Korea_relations |
| 67. | years | 15: [11, inf] | years two ago | All_Those_Years_Ago |
| 68. | ethiopia | 15: [12, inf] | ethiopia somalia ethiopian | Ogaden_War |
| 69. | /sub | 15: [16, inf] | /sub f + | System_F-sub |
| 70. | group | 15: [10, inf] | group american iraq | Iraqi_Americans |
| 71. | sudan | 16: [12, inf], 22: [10, inf], 36: [10, 5.0] | sudan darfur u.n. | War_in_Darfur |
| 72. | darfur | 16: [15, 7.5], 36: [18, 6.0], 40: [12, inf] | darfur sudan u.n. | War_in_Darfur |
| 73. | tobacco | 16: [14, inf] | tobacco ferrari sponsor | Marlboro_(cigarette) |
| 74. | yeltsin | 17: [10, inf] | yeltsin boris russia | Presidency_of_Boris_Yeltsin |
| 75. | debate | 17: [10, inf] | debate president bush | George_W._Bush |
| 76. | blair | 18: [11, inf], 26: [12, 6.0] | blair tony prime | Tony_Blair |
| 77. | least | 19: [10, inf] | least killed people | Persecution_of_Hazara_people_in_Quetta |
| 78. | pakistan | 19: [17, inf], 37: [18, 6.0], 50: [15, 7.5] | pakistan musharraf president | Pervez_Musharraf |
| 79. | brazil | 19: [17, 8.5], 29: [10, inf] | brazil president pope | List_of_dignitaries_at_the_funeral_of_Pope_John_Paul_II |
| 80. | race | 19: [17, inf], 29: [11, inf], 42: [11, inf], 52: [10, 10.0] | race – first | Canada's_Drag_Race |
| 81. | abortion | 19: [12, inf] | abortion pope catholic | Catholic_Church_and_abortion |
| 82. | vice | 19: [11, inf] | vice president cheney | Dick_Cheney |
| 83. | cheney | 19: [12, inf] | cheney vice president | Dick_Cheney |
| 84. | king | 19: [11, inf] | king saudi abdullah | Abdullah_of_Saudi_Arabia |
| 85. | palestinians | 20: [11, inf], 23: [10, 10.0] | palestinians palestinian gaza | State_of_Palestine |
| 86. | ambush | 20: [12, inf] | ambush soldiers american | Tongo_Tongo_ambush |
| 87. | wolfowitz | 20: [12, inf] | wolfowitz bank world | Paul_Wolfowitz |
| 88. | monaco | 21: [14, inf] | monaco tomorrow world | Arash_Amel |
| 89. | justice | 22: [12, inf] | justice chief pakistan | Chief_Justice_of_Pakistan |
| 90. | u.n. | 22: [11, inf], 26: [19, 9.5], 32: [20, 6.67], 38: [12, 6.0] | u.n. united nations | Headquarters_of_the_United_Nations |
| 91. | civilians | 22: [14, inf] | civilians killed iraq | Casualties_of_the_Iraq_War |
| 92. | labor | 22: [12, inf] | labor party minister | Israeli_Labor_Party |
| 93. | agency | 22: [10, inf] | agency iran nuclear | Nuclear_program_of_Iran |
| 94. | suspect | 22: [11, inf] | suspect british police | Prime_Suspect |
| 95. | putin | 23: [20, 20.0], 37: [12, 6.0], 48: [15, inf] | putin president russia | Vladimir_Putin |
| 96. | missile | 23: [17, 8.5], 32: [10, inf] | missile russia defense | Missile_defense |
| 97. | emissions | 23: [12, inf] | emissions climate global | Climate_change |
| 98. | people | 23: [13, 6.5], 37: [15, 15.0], 40: [15, inf] | people killed least | List_of_people_killed_for_being_transgender |
| 99. | militants | 24: [12, 12.0], 43: [10, inf] | militants american iraq | American-led_intervention_in_Iraq_(2014–present) |
| 100. | parliament | 24: [12, inf] | parliament president iraq | President_of_Iraq |
| 101. | power | 24: [13, inf], 29: [10, 5.0] | power president nuclear | Nuclear_power |
| 102. | troops | 25: [22, inf], 28: [14, 7.0], 36: [13, 6.5] | troops iraq u.s. | Withdrawal_of_U.S._troops_from_Iraq_(2020–21) |
| 103. | reactor | 25: [12, inf] | reactor north korea | North_Korea_and_weapons_of_mass_destruction |
| 104. | car | 26: [15, inf] | car baghdad bomb | List_of_mass_car_bombings |
| 105. | like | 26: [10, inf] | like f race | RuPaul's_Drag_Race |
| 106. | bbc | 27: [12, inf] | bbc gaza reporter | List_of_BBC_newsreaders_and_reporters |
| 107. | mosque | 27: [19, inf] | mosque pakistan killed | Sectarian_violence_in_Pakistan |
| 108. | doctors | 27: [10, inf] | doctors medical accident | Physician |
| 109. | mahmoud | 28: [10, inf] | mahmoud president abbas | Mahmoud_Abbas |
| 110. | abbas | 28: [14, inf] | abbas palestinian president | Mahmoud_Abbas |
| 111. | – | 29: [10, inf], 39: [10, inf] | – mclaren f | McLaren_F1 |
| 112. | diplomats | 29: [12, inf] | diplomats american iraq | American-led_intervention_in_Iraq_(2014–present) |
| 113. | earthquake | 29: [11, inf], 33: [11, inf] | earthquake japan peru | 2007_Peru_earthquake |
| 114. | taliban | 29: [12, 12.0], 35: [22, 22.0], 44: [10, inf] | taliban afghanistan afghan | War_in_Afghanistan_(2001–present) |
| 115. | mclaren | 29: [13, inf], 39: [10, inf] | mclaren hamilton – | Lewis_Hamilton |
| 116. | poll | 30: [12, inf] | poll global countries | Importance_of_religion_by_country |
| 117. | sub-saharan | 30: [10, inf] | sub-saharan africa poll | Africa |
| 118. | africa | 30: [12, inf], 51: [13, 13.0] | africa south african | South_Africa |
| 119. | shinzo | 30: [10, inf] | shinzo minister prime | Shinzo_Abe |
| 120. | abe | 30: [10, inf] | abe minister japan | Shinzo_Abe |
| 121. | toll | 31: [13, inf], 33: [10, 10.0] | toll death iraq | Casualties_of_the_Iraq_War |
| 122. | scandal | 31: [13, inf] | scandal spy mclaren | List_of_"-gate"_scandals |
| 123. | public | 31: [10, inf] | public american officials | Official |
| 124. | holocaust | 31: [14, inf] | holocaust survivors israel | Holocaust_survivors |
| 125. | survivors | 31: [12, inf] | survivors holocaust plan | Holocaust_survivors |
| 126. | security | 32: [13, inf] | security iraq baghdad | Attack_on_the_United_States_embassy_in_Baghdad |
| 127. | georgia | 32: [11, inf] | georgia missile russia | Georgia–Russia_relations |
| 128. | aid | 33: [12, inf] | aid u.s. president | United_States_foreign_aid |
| 129. | peru | 33: [14, inf], 38: [12, inf] | peru fujimori earthquake | Japanese_Peruvians |
| 130. | hurricane | 34: [20, 10.0], 36: [14, inf] | hurricane dean storm | Hurricane_Dean |
| 131. | cabinet | 35: [11, inf] | cabinet minister palestinian | Prime_Minister_of_the_Palestinian_National_Authority |
| 132. | answers | 35: [13, inf] | answers china american | Answers_for_Americans |
| 133. | hostages | 35: [13, inf] | hostages taliban south | 2007_South_Korean_hostage_crisis_in_Afghanistan |
| 134. | plot | 36: [16, inf] | plot british bomb | 2010_transatlantic_aircraft_bomb_plot |
| 135. | even | 36: [11, inf] | even american officials | Threatening_government_officials_of_the_United_States |
| 136. | felix | 36: [11, inf] | felix hurricane storm | Hurricane_Felix |
| 137. | trulli | 36: [10, inf] | trulli macao victory | EMPTY MATCHING |
| 138. | german | 36: [10, inf] | german germany police | Federal_Police_(Germany) |
| 139. | might | 37: [11, inf] | might u.s. president | Vice_President_of_the_United_States |
| 140. | terrorism | 38: [10, inf] | terrorism british britain | Terrorism_in_the_United_Kingdom |
| 141. | cases | 38: [15, inf] | cases court health | Lists_of_United_States_Supreme_Court_cases |
| 142. | help | 38: [12, inf] | help american iraq | American-led_intervention_in_Iraq_(2014–present) |
| 143. | term | 38: [11, inf] | term president chávez | Hugo_Chávez |
| 144. | musharraf | 38: [24, 6.0], 44: [14, inf], 50: [15, inf] | musharraf pakistan pervez | 1999_Pakistani_coup_d'état |
| 145. | blackwater | 38: [14, inf] | blackwater iraq security | Academi |
| 146. | guards | 38: [10, inf] | guards iraq u.s. | Republican_Guard_(Iraq) |
| 147. | fujimori | 38: [11, inf] | fujimori peru alberto | Alberto_Fujimori |
| 148. | climate | 39: [10, inf] | climate change global | Climate_change |
| 149. | change | 39: [10, inf] | change climate global | Climate_change |
| 150. | ahmadinejad | 39: [14, inf] | ahmadinejad iran president | Mahmoud_Ahmadinejad |
| 151. | crackdown | 39: [10, inf] | crackdown myanmar china | Myanmar |
| 152. | agreement | 40: [10, inf] | agreement north talks | Paris_Peace_Accords |
| 153. | meet | 40: [10, inf] | meet leaders talks | Josh_Talks |
| 154. | korean | 40: [16, inf] | korean south north | North_Korea–South_Korea_relations |
| 155. | arrested | 40: [10, inf] | arrested police british | Law_enforcement_in_the_United_Kingdom |
| 156. | crash | 40: [10, inf] | crash helicopter u.s. | 2020_Calabasas_helicopter_crash |
| 157. | nigeria | 41: [10, inf] | nigeria election africa | 2015_Nigerian_general_election |
| 158. | nobel | 41: [15, inf] | nobel prize work | Nobel_Prize_in_Literature |
| 159. | turkey | 41: [10, inf], 51: [20, 20.0] | turkey iraq turkish | Iraq–Turkey_relations |
| 160. | prize | 41: [12, inf] | prize nobel work | Nobel_Prize_in_Literature |
| 161. | european | 42: [10, inf] | european union europe | European_Union |
| 162. | benazir | 42: [10, inf] | benazir bhutto pakistan | Nusrat_Bhutto |
| 163. | bhutto | 42: [16, inf], 45: [16, 8.0], 52: [15, inf] | bhutto benazir pakistan | Nusrat_Bhutto |
| 164. | envoy | 46: [13, inf] | envoy u.n. myanmar | Myanmar |
| 165. | second | 48: [10, inf] | second day president | Not_My_Presidents_Day |
| 166. | weapons | 49: [12, inf] | weapons american iran | Iran_and_weapons_of_mass_destruction |
| 167. | motor | 49: [10, inf] | motor mclaren like | McLaren |
| 168. | bomber | 49: [10, inf] | bomber suicide kills | Female_suicide_bomber |
| 169. | zuma | 51: [12, inf] | zuma south africa | Jacob_Zuma |
| 170. | northern | 51: [10, inf] | northern iraq kurdish | Iraqi–Kurdish_conflict |
| 171. | workers | 52: [13, inf] | workers strike labor | Strike_action |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | woolmer | 12: [11, inf] | woolmer bob 's | Bob_Woolmer |
| 2. | virginia | 16: [11, inf] | virginia tech killer | Seung-Hui_Cho |
| 3. | bae | 23: [89, inf] | bae files inquiry | Al-Yamamah_arms_deal |
| 4. | files | 23: [78, inf] | files bae 's | BAE_Systems |
| 5. | gaza | 24: [12, inf], 43: [10, inf] | gaza hamas israeli | Gaza_War_(2008–2009) |
| 6. | hamas | 24: [13, inf] | hamas gaza fatah | Battle_of_Gaza_(2007) |
| 7. | found | 30: [10, inf] | found guilty dead | Death_of_Caylee_Anthony |
| 8. | g | 32: [20, inf] | g beijing special | Beijing |
| 9. | hello | 32: [21, inf] | hello beijing g | Hello_Kitty_Online |
| 10. | special | 32: [21, inf] | special beijing g | Beijing |
| 11. | beijing | 32: [24, inf] | beijing g special | Beijing |
| 12. | bhutto | 42: [11, 11.0], 52: [22, inf] | bhutto pakistan musharraf | Pervez_Musharraf |
| 13. | california | 43: [10, inf] | california wildfires boy | October_2007_California_wildfires |
| 14. | darfur | 43: [10, inf] | darfur talks peace | Darfur |
| 15. | zuma | 51: [11, inf] | zuma anc 's | Jacob_Zuma |
