# Keywords with the highest 'interestingness' in 2012

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
| 1. | taliban | 1: [13, inf], 51: [12, 12.0] | taliban afghan afghanistan | War_in_Afghanistan_(2001–present) |
| 2. | afghanistan | 1: [10, inf], 16: [21, inf], 34: [11, 5.5] | afghanistan afghan american | Afghan_Americans |
| 3. | minister | 1: [10, inf] | minister prime former | List_of_prime_ministers_of_India |
| 4. | two | 1: [12, inf] | two china killed | Kill_Bill:_Volume_2 |
| 5. | law | 1: [11, inf], 51: [11, 5.5] | law rights china | LGBT_rights_in_China |
| 6. | iran | 1: [20, inf], 31: [20, 5.0] | iran nuclear israel | Iran–Israel_proxy_conflict |
| 7. | official | 1: [10, inf], 7: [19, 6.33], 15: [10, 5.0], 27: [10, 5.0], 30: [10, inf], 36: [10, 5.0] | official china chinese | History_of_China |
| 8. | news | 1: [11, inf], 6: [15, 5.0] | news international iht | The_New_York_Times_International_Edition |
| 9. | day | 1: [14, inf] | day image india | List_of_Chief_guests_at_Delhi_Republic_Day_parade |
| 10. | security | 1: [13, inf], 44: [10, 5.0], 51: [13, 6.5] | security forces syria | Syrian_Armed_Forces |
| 11. | government | 1: [25, inf] | government syria syrian | Syrian_Interim_Government |
| 12. | russian | 1: [11, inf], 41: [10, inf] | russian russia putin | Opposition_to_Vladimir_Putin_in_Russia |
| 13. | egypt | 1: [12, inf], 4: [18, 6.0], 17: [14, 7.0] | egypt president military | President_of_Egypt |
| 14. | military | 1: [11, inf], 38: [23, 11.5] | military u.s. american | United_States_Armed_Forces |
| 15. | police | 1: [10, inf] | police officers afghan | Afghan_National_Police |
| 16. | say | 1: [13, inf] | say officials iran | COVID-19_pandemic_in_Iran |
| 17. | u.s. | 1: [13, inf] | u.s. united states | U.S._state |
| 18. | india | 1: [10, inf] | india indian day | Republic_Day_(India) |
| 19. | south | 1: [12, 12.0], 26: [13, inf], 47: [15, inf] | south korea north | North_Korea–South_Korea_relations |
| 20. | political | 1: [17, inf] | political president party | Political_party |
| 21. | china | 1: [22, inf] | china chinese party | Chinese_Communist_Party |
| 22. | country | 1: [12, inf], 24: [20, 6.67] | country government president | President_(government_title) |
| 23. | leader | 1: [14, inf], 13: [16, 5.33], 17: [10, 10.0] | leader president north | List_of_leaders_of_North_Korea |
| 24. | iraq | 1: [12, inf], 30: [15, 7.5] | iraq afghanistan iran | Afghans_in_Iran |
| 25. | iranian | 1: [11, inf], 19: [10, 5.0] | iranian iran nuclear | Nuclear_program_of_Iran |
| 26. | church | 1: [10, inf] | church catholic bishops | Bishops_in_the_Catholic_Church |
| 27. | support | 2: [10, inf], 33: [10, 10.0] | support president minister | President_of_India |
| 28. | dead | 2: [10, inf] | dead left people | Left_4_Dead |
| 29. | taiwan | 2: [12, inf] | taiwan china japan | Japan–Taiwan_relations |
| 30. | way | 3: [11, inf], 51: [11, inf] | way china could | China |
| 31. | costa | 3: [11, inf] | costa concordia cruise | Costa_Concordia |
| 32. | concordia | 3: [11, inf] | concordia costa cruise | Costa_Concordia |
| 33. | state | 3: [10, inf], 47: [12, 6.0] | state clinton secretary | Hillary_Clinton's_tenure_as_Secretary_of_State |
| 34. | human | 3: [12, inf] | human rights united | Universal_Declaration_of_Human_Rights |
| 35. | seek | 3: [11, inf] | seek president egypt | Egypt |
| 36. | central | 3: [10, inf] | central bank government | Central_bank |
| 37. | republic | 4: [10, inf] | republic congo day | Republic_of_the_Congo |
| 38. | genocide | 4: [11, inf] | genocide bill former | Rwandan_genocide |
| 39. | peace | 4: [12, 12.0], 46: [11, inf], 49: [10, 10.0] | peace syria talks | Vienna_peace_talks_for_Syria |
| 40. | arab | 4: [26, 5.2], 12: [10, 10.0], 27: [13, 6.5], 35: [10, inf], 37: [16, inf] | arab syria spring | Arab_Spring |
| 41. | league | 4: [11, inf] | league arab syria | Arab_League |
| 42. | hong | 4: [10, inf], 36: [12, inf] | hong kong chinese | Hong_Kong |
| 43. | kong | 4: [10, inf], 36: [10, inf] | kong hong chinese | Hong_Kong |
| 44. | davos | 4: [13, inf] | davos world even | Davos |
| 45. | tibetan | 4: [12, inf], 13: [24, 24.0] | tibetan china protest | 2008_Tibetan_unrest |
| 46. | bill | 4: [13, inf] | bill genocide would | Rwandan_genocide |
| 47. | leaders | 4: [14, 7.0], 35: [13, inf] | leaders china political | Politics_of_China |
| 48. | pollution | 4: [14, inf] | pollution air beijing | Pollution_in_China |
| 49. | cold | 5: [14, inf] | cold china winter | Cold_Winter |
| 50. | resolution | 5: [13, inf] | resolution syria united | List_of_United_Nations_resolutions_concerning_Syria |
| 51. | nato | 5: [11, 5.5], 7: [12, 12.0], 15: [10, inf] | nato afghan afghanistan | War_in_Afghanistan_(2001–present) |
| 52. | village | 5: [10, inf] | village chen chinese | Chen-style_taijiquan |
| 53. | israel | 6: [10, 10.0], 9: [17, 5.67], 22: [13, 13.0], 31: [19, 19.0], 39: [14, inf], 45: [10, 10.0] | israel iran israeli | Iran–Israel_relations |
| 54. | maldives | 6: [14, inf] | maldives president former | President_of_the_Maldives |
| 55. | judge | 6: [12, inf], 16: [10, inf] | judge former court | List_of_former_judges_of_the_Supreme_Court_of_India |
| 56. | star | 6: [11, inf] | star south chinese | Chinese_star_names |
| 57. | georgia | 7: [12, inf] | georgia president israeli | Foreign_relations_of_Israel |
| 58. | voters | 7: [12, inf] | voters elections election | 2020_United_States_elections |
| 59. | since | 7: [11, inf], 22: [11, 5.5] | since first president | George_Washington |
| 60. | attacks | 7: [13, inf], 14: [17, inf], 24: [12, 12.0], 33: [26, 26.0] | attacks afghan killed | War_in_Afghanistan_(2001–present) |
| 61. | anthony | 7: [16, inf] | anthony shadid syria | Anthony_Shadid |
| 62. | shadid | 7: [14, inf] | shadid anthony syria | Anthony_Shadid |
| 63. | apology | 8: [13, inf] | apology afghanistan american | Ashraf_Ghani |
| 64. | korans | 8: [11, inf] | korans burning afghanistan | Taliban |
| 65. | yemen | 8: [14, inf] | yemen president qaeda | Al-Qaeda_insurgency_in_Yemen |
| 66. | strauss-kahn | 8: [10, inf] | strauss-kahn dominique prostitution | Dominique_Strauss-Kahn |
| 67. | obama | 8: [12, inf], 28: [11, 5.5], 45: [33, 33.0] | obama president u.s. | Barack_Obama |
| 68. | journalists | 8: [14, inf] | journalists rights reporter | Reporters_Without_Borders |
| 69. | sunday | 8: [12, inf], 18: [10, 5.0] | sunday president elections | Election_day |
| 70. | tv | 9: [10, inf] | tv north british | Bodyguard_(British_TV_series) |
| 71. | academy | 9: [14, inf] | academy north korea | Korean_People's_Army |
| 72. | documentary | 9: [11, inf] | documentary life acid | Saving_Face_(2012_film) |
| 73. | us | 9: [10, inf] | us tell iht | Bangkok_Love_Story |
| 74. | things | 9: [11, inf] | things china change | Internet_of_things |
| 75. | tensions | 9: [12, inf] | tensions china chinese | China |
| 76. | six | 10: [10, inf] | six iran nuclear | Iran_nuclear_deal_framework |
| 77. | massacre | 11: [12, inf] | massacre syria united | 1982_Hama_massacre |
| 78. | budget | 11: [24, 12.0], 47: [10, inf] | budget cuts european | Tax_Cuts_and_Jobs_Act_of_2017 |
| 79. | convicted | 11: [10, inf], 35: [10, inf] | convicted prison years | List_of_American_federal_politicians_convicted_of_crimes |
| 80. | greece | 12: [10, inf] | greece euro greek | Greek_withdrawal_from_the_eurozone |
| 81. | jewish | 12: [14, inf] | jewish school attack | List_of_attacks_on_Jewish_institutions_in_the_United_States |
| 82. | council | 12: [15, inf] | council syria security | United_Nations_Security_Council_veto_power |
| 83. | toulouse | 12: [12, inf] | toulouse france killings | Toulouse_and_Montauban_shootings |
| 84. | race | 12: [10, inf] | race presidential egypt | 2012_Egyptian_presidential_election |
| 85. | merah | 12: [12, inf] | merah mohammed french | Mohammed_Merah |
| 86. | mohammed | 12: [10, inf] | mohammed merah french | Mohammed_Merah |
| 87. | woman | 13: [10, 5.0], 24: [11, inf] | woman women china | Women_in_China |
| 88. | britain | 13: [10, inf], 16: [12, 12.0] | britain british cameron | British_nationalism |
| 89. | exiles | 13: [12, inf] | exiles tibetan delhi | Central_Tibetan_Administration |
| 90. | brics | 13: [13, inf] | brics india delhi | 4th_BRICS_summit |
| 91. | might | 14: [10, inf] | might china u.s. | China–United_States_relations |
| 92. | legal | 14: [11, inf] | legal china chinese | Legalism_(Chinese_philosophy) |
| 93. | german | 14: [10, inf] | german germany president | President_of_Germany |
| 94. | reward | 14: [11, inf] | reward militant u.s. | Abdul_Rehman_Makki |
| 95. | militant | 14: [14, inf] | militant group attacks | List_of_Palestinian_suicide_attacks |
| 96. | ahead | 15: [10, inf] | ahead putin minister | Vladimir_Putin |
| 97. | bahrain | 15: [10, inf] | bahrain protesters grand | Bahrain_Grand_Prix |
| 98. | tsunami | 15: [11, inf] | tsunami japan earthquake | List_of_earthquakes_in_Japan |
| 99. | korean | 15: [11, inf] | korean north south | North_Korea–South_Korea_relations |
| 100. | launching | 15: [11, inf] | launching north korea | Korean_People's_Army |
| 101. | failure | 15: [11, inf] | failure government rocket | Proton_(rocket_family) |
| 102. | women | 16: [12, 6.0], 24: [22, 7.33], 32: [10, 10.0], 41: [24, 12.0], 45: [10, inf] | women india world | Women_in_India |
| 103. | chen | 17: [11, inf] | chen guangcheng china | Chen_Guangcheng |
| 104. | ferry | 18: [12, inf] | ferry papua guinea | New_Guinea_campaign |
| 105. | time | 18: [14, inf], 24: [11, 5.5] | time first president | President_of_East_Timor |
| 106. | clinton | 19: [14, 7.0], 44: [13, inf], 47: [11, inf] | clinton secretary state | Hillary_Clinton's_tenure_as_Secretary_of_State |
| 107. | iraqi | 19: [11, 5.5], 36: [10, inf] | iraqi iraq president | President_of_Iraq |
| 108. | eurovision | 21: [12, inf] | eurovision azerbaijan contest | Azerbaijan_in_the_Eurovision_Song_Contest |
| 109. | myanmar | 22: [11, 5.5], 28: [11, inf], 34: [12, inf] | myanmar suu aung | National_League_for_Democracy |
| 110. | readers | 22: [10, inf] | readers questions india | India |
| 111. | aung | 22: [10, inf] | aung myanmar suu | National_League_for_Democracy |
| 112. | san | 22: [10, inf] | san myanmar suu | Aung_San_Suu_Kyi |
| 113. | suu | 22: [11, inf] | suu myanmar aung | National_League_for_Democracy |
| 114. | kyi | 22: [10, inf] | kyi myanmar suu | National_League_for_Democracy |
| 115. | part | 23: [12, inf] | part u.s. china | China–United_States_relations |
| 116. | socialists | 24: [14, inf] | socialists france majority | Socialist_Party_(France) |
| 117. | led | 24: [12, inf] | led scandal two | Bofors_scandal |
| 118. | soldier | 24: [13, inf] | soldier afghan afghanistan | War_in_Afghanistan_(2001–present) |
| 119. | asylum | 25: [11, inf] | asylum assange ecuador | Julian_Assange |
| 120. | home | 26: [10, inf], 51: [18, inf] | home back family | Home_Alone_4:_Taking_Back_the_House |
| 121. | art | 27: [10, inf], 49: [17, 17.0] | art week india | Week |
| 122. | asia | 27: [10, inf], 31: [11, 5.5] | asia china obama | East_Asian_foreign_policy_of_the_Barack_Obama_administration |
| 123. | bollywood | 29: [15, inf] | bollywood india film | Bollywood |
| 124. | rebels | 29: [17, inf] | rebels syrian syria | Syrian_civil_war |
| 125. | capital | 29: [10, inf] | capital syrian syria | Syrian_civil_war |
| 126. | formula | 30: [10, inf] | formula grand prix | 2021_Formula_One_World_Championship |
| 127. | massive | 31: [11, inf] | massive india power | Nuclear_power_in_India |
| 128. | outage | 31: [10, inf] | outage india power | Power_outage |
| 129. | electrical | 31: [10, inf] | electrical india grid | Electrical_grid |
| 130. | blackouts | 31: [11, inf] | blackouts india power | 2012_India_blackouts |
| 131. | blackout | 31: [11, inf] | blackout india power | 2012_India_blackouts |
| 132. | sikh | 32: [12, inf] | sikh america wisconsin | Wisconsin_Sikh_temple_shooting |
| 133. | australia | 33: [10, inf] | australia minister prime | Prime_Minister_of_Australia |
| 134. | ecuador | 33: [11, inf] | ecuador assange wikileaks | Julian_Assange |
| 135. | assange | 33: [18, inf] | assange julian wikileaks | Indictment_and_arrest_of_Julian_Assange |
| 136. | embassy | 33: [11, inf] | embassy u.s. american | 1998_United_States_embassy_bombings |
| 137. | fighting | 34: [11, 11.0], 47: [16, inf] | fighting syria rebels | Belligerents_in_the_Syrian_Civil_War |
| 138. | plans | 34: [11, inf] | plans israel would | Trump_peace_plan |
| 139. | prince | 34: [10, inf] | prince harry british | Prince_Harry,_Duke_of_Sussex |
| 140. | convention | 35: [14, inf] | convention republican american | Republican_National_Convention |
| 141. | republican | 35: [11, inf] | republican romney former | Ronna_Romney |
| 142. | ambassador | 37: [14, inf] | ambassador u.s. american | Ambassadors_of_the_United_States |
| 143. | benghazi | 37: [10, inf] | benghazi libya attack | 2012_Benghazi_attack |
| 144. | video | 37: [15, inf], 52: [11, 5.5] | video american afghanistan | War_in_Afghanistan_(2001–present) |
| 145. | dutch | 37: [10, inf] | dutch marijuana euro | Drug_policy_of_the_Netherlands |
| 146. | anti-american | 37: [10, inf] | anti-american u.s. protests | George_Floyd_protests |
| 147. | decades | 38: [10, inf] | decades country two | 2000s |
| 148. | fashion | 38: [15, inf] | fashion iht today | Tony_Leung_Chiu-wai |
| 149. | including | 38: [10, inf] | including people killed | List_of_people_killed_for_being_transgender |
| 150. | drone | 39: [10, inf] | drone pakistan strikes | Drone_strikes_in_Pakistan |
| 151. | look | 40: [12, inf] | look world like | Cats_That_Look_Like_Hitler |
| 152. | currency | 40: [14, inf] | currency iran euro | International_status_and_usage_of_the_euro |
| 153. | turkey | 40: [12, inf], 44: [10, inf] | turkey syria syrian | Syria–Turkey_relations |
| 154. | gandhi | 40: [18, inf] | gandhi india rahul | Rahul_Gandhi |
| 155. | girl | 41: [10, inf] | girl pakistan taliban | Tehrik-i-Taliban_Pakistan |
| 156. | tuesday | 41: [13, 13.0], 48: [12, inf] | tuesday president government | President_of_the_United_States |
| 157. | authorities | 41: [10, inf] | authorities chinese syrian | Syrian_civil_war |
| 158. | use | 42: [12, inf] | use government nuclear | Nuclear_power_in_India |
| 159. | berlusconi | 43: [10, inf] | berlusconi silvio prime | Barbara_Berlusconi |
| 160. | advice | 44: [10, inf] | advice college students | University_College_London |
| 161. | merkel | 44: [11, inf] | merkel germany angela | Family_of_Angela_Merkel |
| 162. | affected | 44: [10, inf] | affected iran people | Persians |
| 163. | sandy | 44: [15, inf] | sandy hurricane affected | Hurricane_Sandy |
| 164. | likely | 45: [10, inf] | likely iran would | Iran |
| 165. | amid | 45: [13, inf] | amid china president | Vice_President_of_the_Republic_of_China |
| 166. | deal | 45: [14, inf] | deal north u.s. | Deal_or_No_Deal_(American_game_show) |
| 167. | western | 46: [11, inf] | western china syria | Syrian_civil_war |
| 168. | conference | 46: [17, inf] | conference women china | World_Conference_on_Women,_1995 |
| 169. | hamas | 46: [14, inf] | hamas gaza israel | 2012_Israeli_operation_in_the_Gaza_Strip |
| 170. | egyptian | 47: [10, inf] | egyptian egypt president | President_of_Egypt |
| 171. | media | 47: [10, inf] | media news murdoch | James_Murdoch |
| 172. | facebook | 47: [10, inf] | facebook india internet | Facebook,_Inc. |
| 173. | bishops | 47: [10, inf] | bishops church england | List_of_bishops_in_the_Church_of_England |
| 174. | congo | 47: [20, inf] | congo rebels goma | Goma |
| 175. | million | 47: [10, inf] | million india people | Demographics_of_India |
| 176. | kasab | 47: [10, inf] | kasab attacks india | Ajmal_Kasab |
| 177. | execution | 47: [16, inf] | execution gunman prisoners | Doyle_Hamm |
| 178. | gunman | 47: [12, inf] | gunman attacks shot | 2020_Vienna_attack |
| 179. | festival | 48: [10, inf] | festival day image | Mid-Autumn_Festival |
| 180. | veterans | 49: [13, inf] | veterans military affairs | United_States_Secretary_of_Veterans_Affairs |
| 181. | launch | 50: [11, inf] | launch north korea | North_Korea_and_weapons_of_mass_destruction |
| 182. | court | 50: [21, inf] | court supreme case | Supreme_Court_of_the_United_States |
| 183. | bus | 51: [10, inf] | bus delhi killed | 2012_Delhi_gang_rape_and_murder |
| 184. | rape | 51: [11, inf] | rape delhi victim | 2012_Delhi_gang_rape_and_murder |
| 185. | holidays | 51: [13, inf] | holidays christmas home | Christmas_and_holiday_season |
| 186. | christmas | 51: [15, inf] | christmas home holidays | Christmas_and_holiday_season |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | breast | 1: [10, inf] | breast implant scandal | Poly_Implant_Prothèse |
| 2. | football | 5: [10, inf] | football egypt violence | Port_Said_Stadium_riot |
| 3. | abu | 6: [13, inf], 16: [12, 12.0] | abu qatada may | Abu_Qatada |
| 4. | qatada | 6: [13, inf], 16: [11, inf] | qatada abu may | Abu_Qatada |
| 5. | emails | 11: [49, inf] | emails assad 's | Podesta_emails |
| 6. | toulouse | 12: [13, inf] | toulouse shootings shooting | Toulouse_and_Montauban_shootings |
| 7. | marriage | 19: [10, inf] | marriage gay 's | Same-sex_marriage_in_the_United_States |
| 8. | g | 20: [11, inf] | g summit nato | NATO_summit |
| 9. | houla | 22: [10, inf] | houla massacre syria | Houla_massacre |
| 10. | mont | 28: [10, inf] | mont blanc avalanche | Mont_Blanc |
| 11. | blanc | 28: [10, inf] | blanc mont avalanche | Mont_Blanc |
| 12. | shootings | 36: [13, inf] | shootings alps french | Annecy_shootings |
| 13. | alps | 36: [13, inf] | alps french shootings | Annecy_shootings |
| 14. | prize | 41: [13, inf] | prize peace nobel | Nobel_Peace_Prize |
| 15. | nobel | 41: [10, inf] | nobel peace prize | Nobel_Peace_Prize |
| 16. | abortion | 46: [11, inf] | abortion 's clinic | Abortion_clinic |
| 17. | tales | 47: [11, inf] | tales catalonia 's | List_of_fairy_tales |
