# Keywords with the highest 'interestingness' in 2013

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
| 1. | group | 2: [10, inf], 19: [21, 5.25], 30: [12, inf] | group syrian attack | Use_of_chemical_weapons_in_the_Syrian_Civil_War |
| 2. | censorship | 2: [10, inf] | censorship china film | Film_censorship_in_China |
| 3. | newspaper | 2: [12, inf] | newspaper china chinese | List_of_newspapers_in_China |
| 4. | karzai | 2: [12, 6.0], 47: [14, inf] | karzai president hamid | Hamid_Karzai |
| 5. | chávez | 2: [11, inf], 10: [30, 10.0] | chávez hugo president | Death_of_Hugo_Chávez |
| 6. | held | 2: [13, 13.0], 16: [11, inf], 37: [11, 5.5], 47: [16, 5.33] | held american years | List_of_American_sportsperson-politicians |
| 7. | mali | 2: [11, inf] | mali french france | France–Mali_relations |
| 8. | arab | 3: [10, inf], 35: [10, inf] | arab emirates spring | United_Arab_Emirates |
| 9. | fighting | 3: [10, 5.0], 21: [14, inf] | fighting rebels syria | Belligerents_in_the_Syrian_Civil_War |
| 10. | forces | 3: [12, inf], 30: [10, inf], 50: [14, 14.0] | forces security government | Rhodesian_Security_Forces |
| 11. | prime | 3: [23, 5.75], 8: [13, inf] | prime minister former | List_of_prime_ministers_of_India |
| 12. | since | 3: [13, inf] | since first president | George_Washington |
| 13. | myanmar | 3: [12, inf], 12: [13, inf] | myanmar violence muslims | Persecution_of_Muslims_in_Myanmar |
| 14. | cameron | 3: [13, inf], 20: [12, inf] | cameron minister prime | David_Cameron |
| 15. | panetta | 3: [12, inf] | panetta defense secretary | Leon_Panetta |
| 16. | secretary | 3: [10, 5.0], 9: [11, inf], 21: [12, 12.0], 29: [14, 7.0], 35: [12, inf], 49: [10, 10.0] | secretary kerry state | John_Kerry |
| 17. | algerian | 3: [16, inf] | algerian hostage attack | In_Amenas_hostage_crisis |
| 18. | algeria | 3: [24, inf] | algeria hostage gas | In_Amenas_hostage_crisis |
| 19. | five | 4: [11, inf] | five years attack | Attack_on_Titan |
| 20. | -year-old | 4: [11, inf] | -year-old rape death | David_Carpenter |
| 21. | arts | 4: [10, inf] | arts week liberal | Liberal_arts_education |
| 22. | changes | 4: [10, inf] | changes china india | 2020_China–India_skirmishes |
| 23. | jaipur | 4: [15, inf] | jaipur literature festival | Jaipur_Literature_Festival |
| 24. | nuclear | 4: [17, inf], 14: [13, inf], 21: [11, 5.5] | nuclear iran north | Nuclear_program_of_Iran |
| 25. | south | 4: [10, inf], 7: [12, 6.0], 22: [12, 12.0], 26: [31, 15.5], 43: [14, inf] | south korea north | North_Korea–South_Korea_relations |
| 26. | fire | 4: [10, inf] | fire killed factory | Triangle_Shirtwaist_Factory_fire |
| 27. | protests | 4: [12, inf], 23: [18, 6.0] | protests government president | 2018–2021_Arab_protests |
| 28. | deadly | 4: [11, inf] | deadly people killed | Police_use_of_deadly_force_in_the_United_States |
| 29. | intelligence | 5: [10, inf], 28: [14, 7.0] | intelligence u.s. snowden | Edward_Snowden |
| 30. | allies | 5: [12, inf] | allies united states | Major_non-NATO_ally |
| 31. | bulgaria | 6: [10, inf] | bulgaria hezbollah european | 2012_Burgas_bus_bombing |
| 32. | ahmadinejad | 6: [10, inf] | ahmadinejad president mahmoud | Mahmoud_Ahmadinejad |
| 33. | berlusconi | 6: [10, inf], 31: [10, inf] | berlusconi silvio minister | Pier_Silvio_Berlusconi |
| 34. | year | 7: [11, 5.5], 25: [13, inf] | year last china | Chinese_New_Year |
| 35. | scotland | 7: [12, inf] | scotland yard britain | Scotland_Yard |
| 36. | foreign | 7: [11, inf], 36: [12, 6.0] | foreign minister syria | Ministry_of_Foreign_Affairs_and_Expatriates_(Syria) |
| 37. | pope | 7: [34, inf], 30: [15, 7.5] | pope francis vatican | Pope_Francis |
| 38. | benedict | 7: [21, inf] | benedict pope xvi | Resignation_of_Pope_Benedict_XVI |
| 39. | church | 7: [12, 12.0], 38: [13, inf] | church pope catholic | Catholic_Church |
| 40. | xvi | 7: [16, inf] | xvi pope benedict | Resignation_of_Pope_Benedict_XVI |
| 41. | korea | 7: [26, 13.0], 43: [10, 5.0], 47: [12, inf] | korea north south | North_Korea–South_Korea_relations |
| 42. | accused | 8: [11, inf] | accused rape case | Ajmer_rape_case |
| 43. | family | 8: [12, 6.0], 46: [10, 5.0], 50: [10, inf] | family china says | China |
| 44. | kerry | 9: [18, inf], 21: [22, 22.0], 29: [13, inf], 31: [11, 5.5], 44: [12, 6.0], 49: [14, inf] | kerry state secretary | John_Kerry |
| 45. | aid | 9: [12, 6.0], 41: [14, 7.0], 46: [22, inf] | aid syria syrian | Syrian_civil_war |
| 46. | cardinals | 10: [14, inf] | cardinals pope conclave | 2013_papal_conclave |
| 47. | filipino | 10: [10, inf] | filipino malaysian borneo | North_Borneo_dispute |
| 48. | sanctions | 10: [11, inf] | sanctions iran nuclear | Sanctions_against_Iran |
| 49. | river | 11: [15, 7.5], 18: [10, inf] | river china brahmaputra | Brahmaputra_River |
| 50. | rape | 11: [10, inf] | rape gang india | 2012_Delhi_gang_rape_and_murder |
| 51. | dead | 11: [12, inf], 46: [10, 5.0] | dead people least | List_of_rampage_killers |
| 52. | jail | 11: [10, inf] | jail court years | Supreme_Court_of_the_United_States |
| 53. | conclave | 11: [16, inf] | conclave pope vatican | 2013_papal_conclave |
| 54. | francis | 11: [17, inf] | francis pope vatican | Pope_Francis |
| 55. | visit | 11: [14, 14.0], 21: [10, 5.0], 23: [10, 5.0], 26: [25, inf], 30: [13, 13.0] | visit president obama | Barack_Obama |
| 56. | prison | 12: [15, 5.0], 17: [10, inf] | prison years former | Larry_Nassar |
| 57. | cyprus | 12: [22, inf] | cyprus bailout iht | List_of_largest_mergers_and_acquisitions |
| 58. | living | 12: [10, inf] | living people country | List_of_the_oldest_people_by_country |
| 59. | sri | 12: [10, inf] | sri lanka india | India–Sri_Lanka_relations |
| 60. | lanka | 12: [10, inf] | lanka sri government | Government_of_Sri_Lanka |
| 61. | even | 12: [11, 11.0], 44: [11, 11.0], 52: [11, inf] | even china syria | Syrian_civil_war |
| 62. | bill | 12: [11, inf] | bill parliament would | Fixed-term_Parliaments_Act_2011 |
| 63. | reported | 12: [10, inf] | reported killed least | Saudi_Arabian-led_intervention_in_Yemen |
| 64. | last | 13: [14, 7.0], 18: [15, 15.0], 25: [12, 6.0], 29: [11, inf] | last week year | ISO_week_date |
| 65. | berezovsky | 13: [13, inf] | berezovsky death boris | Boris_Berezovsky_(businessman) |
| 66. | hong | 13: [12, inf] | hong kong china | Hong_Kong |
| 67. | kong | 13: [12, inf] | kong hong china | Hong_Kong |
| 68. | election | 13: [12, 12.0], 24: [22, 7.33], 29: [10, inf], 31: [14, 7.0] | election vote president | List_of_United_States_presidential_elections_in_which_the_winner_lost_the_popular_vote |
| 69. | debt | 14: [10, inf] | debt daughter crisis | 2012–2013_Cypriot_financial_crisis |
| 70. | daughter | 14: [12, inf] | daughter death chinese | The_Chinese_Botanist's_Daughters |
| 71. | april | 14: [21, inf] | april iht quick | Indigenous_peoples_of_the_Americas |
| 72. | workers | 14: [12, inf] | workers china killed | 2014_Vietnam_anti-China_protests |
| 73. | thatcher | 15: [22, inf] | thatcher margaret british | Premiership_of_Margaret_Thatcher |
| 74. | margaret | 15: [13, inf] | margaret thatcher british | Premiership_of_Margaret_Thatcher |
| 75. | germany | 15: [10, inf] | germany merkel chancellor | Angela_Merkel |
| 76. | opposition | 15: [12, inf] | opposition syrian president | Syrian_opposition |
| 77. | boston | 16: [23, inf] | boston marathon attack | Boston_Marathon_bombing |
| 78. | marathon | 16: [14, inf] | marathon boston bombings | Boston_Marathon_bombing |
| 79. | show | 17: [10, inf], 37: [10, inf] | show china government | List_of_countries_by_system_of_government |
| 80. | cases | 17: [10, inf] | cases rape india | Rape_in_India |
| 81. | building | 17: [10, inf] | building collapse bangladesh | 2013_Dhaka_garment_factory_collapse |
| 82. | bomb | 18: [10, 5.0], 44: [12, inf] | bomb killed attack | 1993_World_Trade_Center_bombing |
| 83. | irish | 18: [12, inf] | irish woman abortion | Abortion_in_the_Republic_of_Ireland |
| 84. | trying | 18: [10, inf], 38: [10, 5.0] | trying china president | President_pro_tempore_of_the_United_States_Senate |
| 85. | putin | 19: [12, inf], 23: [14, inf], 29: [13, inf], 51: [13, 6.5] | putin president vladimir | Vladimir_Putin |
| 86. | embassy | 19: [10, inf] | embassy american u.s. | 1998_United_States_embassy_bombings |
| 87. | union | 20: [11, inf] | union european europe | European_Union |
| 88. | middle | 20: [10, inf] | middle east class | Middle_East |
| 89. | class | 20: [10, inf] | class middle poor | Middle_class |
| 90. | lebanon | 21: [11, inf] | lebanon syrian hezbollah | Hezbollah |
| 91. | soldier | 21: [10, inf] | soldier attack killed | 2020_Camp_Taji_attacks |
| 92. | plans | 22: [10, inf] | plans china israel | China–Israel_relations |
| 93. | time | 22: [10, inf] | time first president | President_of_East_Timor |
| 94. | charges | 23: [12, inf] | charges court former | Impeachment |
| 95. | children | 23: [11, 11.0], 43: [13, inf] | children india killed | Navy_Day_(India) |
| 96. | plant | 23: [10, inf] | plant nuclear fukushima | Fukushima_Daiichi_Nuclear_Power_Plant |
| 97. | according | 24: [10, inf], 39: [13, 6.5] | according china people | China |
| 98. | sudan | 24: [13, inf], 51: [16, inf] | sudan south president | Vice_President_of_South_Sudan |
| 99. | mandela | 24: [14, 7.0], 26: [47, 23.5], 49: [42, inf] | mandela nelson south | Presidency_of_Nelson_Mandela |
| 100. | broadcaster | 24: [12, inf] | broadcaster state government | Public_broadcasting |
| 101. | crimes | 24: [11, inf] | crimes court humanity | Crimes_against_humanity |
| 102. | obama | 25: [30, 7.5], 35: [28, 5.6], 43: [13, inf] | obama president syria | Barack_Obama |
| 103. | britain | 25: [11, 11.0], 35: [18, inf] | britain cameron minister | David_Cameron |
| 104. | nelson | 26: [22, 22.0], 49: [24, inf] | nelson mandela south | Nelson_Mandela_Bay_Metropolitan_Municipality |
| 105. | mr. | 26: [12, inf] | mr. president conversation | Abraham_Lincoln |
| 106. | senegal | 26: [14, inf] | senegal obama president | List_of_international_presidential_trips_made_by_Barack_Obama |
| 107. | talks | 29: [16, 16.0], 37: [25, inf], 39: [11, 5.5] | talks iran peace | List_of_Middle_East_peace_proposals |
| 108. | bangladesh | 29: [10, inf] | bangladesh factory building | 2013_Dhaka_garment_factory_collapse |
| 109. | peace | 29: [14, inf], 37: [11, inf] | peace talks kerry | 2013–2014_Israeli–Palestinian_peace_talks |
| 110. | effort | 30: [11, inf] | effort syria president | Syrian_civil_war |
| 111. | least | 30: [16, inf], 51: [10, 10.0] | least people killed | List_of_people_killed_for_being_transgender |
| 112. | biden | 30: [11, inf], 49: [23, inf] | biden president vice | Joe_Biden |
| 113. | train | 30: [12, inf] | train driver rodman | Dennis_Rodman |
| 114. | attack | 30: [15, inf] | attack killed police | 2016_shooting_of_Dallas_police_officers |
| 115. | mugabe | 31: [12, inf] | mugabe zimbabwe president | Robert_Mugabe |
| 116. | zimbabwe | 31: [12, inf] | zimbabwe mugabe election | Robert_Mugabe |
| 117. | photojournalist | 34: [10, inf] | photojournalist rape mumbai | Shakti_Mills_gang_rape |
| 118. | among | 35: [11, inf] | among chinese china | China |
| 119. | administration | 35: [14, inf] | administration obama u.s. | Presidency_of_Barack_Obama |
| 120. | plan | 35: [12, inf], 37: [16, 8.0], 50: [10, 5.0] | plan syria president | American-led_intervention_in_the_Syrian_Civil_War |
| 121. | efforts | 36: [10, inf], 40: [11, inf], 46: [17, 8.5] | efforts president u.s. | President_of_the_United_States |
| 122. | agreement | 37: [10, inf] | agreement iran talks | Joint_Comprehensive_Plan_of_Action |
| 123. | may | 37: [11, inf] | may china day | May_Day |
| 124. | deal | 37: [11, inf], 39: [10, 5.0] | deal iran nuclear | Iran_nuclear_deal_framework |
| 125. | tuesday | 37: [10, inf] | tuesday iran north | Oliver_North |
| 126. | raid | 38: [11, inf] | raid killed officials | Killing_of_Osama_bin_Laden |
| 127. | holocaust | 39: [10, inf] | holocaust president iran | International_Conference_to_Review_the_Global_Vision_of_the_Holocaust |
| 128. | human | 41: [15, inf], 43: [11, inf] | human rights u.n. | United_Nations_Human_Rights_Council |
| 129. | professor | 42: [10, inf] | professor university china | Renmin_University_of_China |
| 130. | communist | 42: [12, inf] | communist party china | Chinese_Communist_Party |
| 131. | mayor | 42: [11, inf] | mayor toronto police | Mayor_of_Toronto |
| 132. | beijing | 42: [16, inf], 49: [10, 10.0] | beijing china chinese | Beijing |
| 133. | case | 43: [12, inf] | case rape court | 2012_Delhi_gang_rape_and_murder |
| 134. | reporter | 43: [11, inf] | reporter detained news | Journalist |
| 135. | tacloban | 46: [14, inf] | tacloban typhoon philippine | Tacloban |
| 136. | next | 47: [10, inf] | next minister year | List_of_prime_ministers_of_India |
| 137. | north | 47: [14, inf], 49: [18, 9.0] | north korea south | North_Korea–South_Korea_relations |
| 138. | protesters | 48: [11, inf] | protesters president police | List_of_police_violence_incidents_during_George_Floyd_protests |
| 139. | army | 48: [10, inf] | army military rebels | Military_of_Chad |
| 140. | vice | 49: [12, inf] | vice president biden | Joe_Biden |
| 141. | r. | 49: [10, inf] | r. biden president | Joe_Biden |
| 142. | memories | 49: [14, inf] | memories mandela nelson | Makgatho_Mandela |
| 143. | johannesburg | 49: [13, inf] | johannesburg mandela nelson | Makgatho_Mandela |
| 144. | bureau | 49: [12, inf] | bureau chief memories | Chief_of_the_Secret_Intelligence_Service |
| 145. | warned | 51: [11, inf] | warned president korea | 2009_imprisonment_of_American_journalists_by_North_Korea |
| 146. | aircraft | 51: [10, inf] | aircraft china air | Air_China |
| 147. | diplomat | 51: [12, inf] | diplomat united indian | Indian_Foreign_Service |
| 148. | rodman | 51: [12, inf] | rodman north korea | Dennis_Rodman |
| 149. | prosecutor | 51: [10, inf] | prosecutor case charges | Prosecutor |
| 150. | christmas | 52: [15, inf] | christmas holiday liu | Kung_Fu_Panda_Holiday |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | algeria | 3: [19, inf] | algeria hostage crisis | In_Amenas_hostage_crisis |
| 2. | algerian | 3: [13, inf] | algerian hostage crisis | In_Amenas_hostage_crisis |
| 3. | benedict | 7: [17, inf] | benedict pope 's | Pope_Benedict_XVI |
| 4. | oscar | 7: [14, inf] | oscar pistorius murder | Oscar_Pistorius |
| 5. | pistorius | 7: [14, inf] | pistorius oscar murder | Oscar_Pistorius |
| 6. | francis | 11: [29, inf] | francis pope 's | Pope_Francis |
| 7. | bank | 12: [10, inf] | bank west 's | West_Bank |
| 8. | boris | 12: [11, inf] | boris berezovsky 's | Boris_Berezovsky_(businessman) |
| 9. | berezovsky | 12: [11, inf] | berezovsky boris death | Boris_Berezovsky_(businessman) |
| 10. | rudd | 26: [10, inf] | rudd kevin 's | Kevin_Rudd |
| 11. | crash | 30: [13, inf] | crash train spanish | List_of_rail_accidents_in_Spain |
| 12. | gibraltar | 32: [12, inf] | gibraltar spain row | Status_of_Gibraltar |
| 13. | miranda | 34: [23, inf] | miranda david detention | David_Miranda_(politician) |
| 14. | detention | 34: [15, inf] | detention miranda david | David_Miranda_(politician) |
| 15. | chemical | 34: [12, inf] | chemical weapons syria | Use_of_chemical_weapons_in_the_Syrian_Civil_War |
| 16. | weapons | 34: [10, inf] | weapons chemical syria | Use_of_chemical_weapons_in_the_Syrian_Civil_War |
| 17. | g | 36: [11, inf] | g summit tax | 45th_G7_summit |
| 18. | nuclear | 45: [13, inf] | nuclear iran deal | Iran_nuclear_deal_framework |
| 19. | typhoon | 45: [12, inf] | typhoon haiyan philippines | Typhoon_Haiyan |
| 20. | haiyan | 45: [12, inf] | haiyan typhoon philippines | Typhoon_Haiyan |
| 21. | indonesia | 47: [12, inf] | indonesia spying australia | Australia–Indonesia_spying_scandal |
| 22. | nelson | 49: [34, inf] | nelson mandela 's | Death_of_Nelson_Mandela |
| 23. | mandela | 49: [50, inf] | mandela nelson 's | Nelson_Mandela |
| 24. | memorial | 50: [13, inf] | memorial mandela nelson | Death_of_Nelson_Mandela |
| 25. | mikhail | 51: [10, inf] | mikhail khodorkovsky putin | Mikhail_Khodorkovsky |
| 26. | khodorkovsky | 51: [10, inf] | khodorkovsky mikhail putin | Mikhail_Khodorkovsky |
