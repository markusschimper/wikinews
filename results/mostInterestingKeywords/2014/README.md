# Keywords with the highest 'interestingness' in 2014

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
| 1. | syrian | 2: [10, inf], 35: [13, 13.0] | syrian syria government | Syrian_Interim_Government |
| 2. | oil | 2: [11, inf], 49: [11, inf] | oil china south | South_China_Sea |
| 3. | foreign | 2: [10, inf] | foreign minister china | Foreign_Minister_of_the_People's_Republic_of_China |
| 4. | north | 2: [11, inf], 6: [16, 8.0], 17: [10, 5.0], 36: [11, inf] | north korea south | North_Korea–South_Korea_relations |
| 5. | including | 3: [12, inf] | including people killed | List_of_people_killed_for_being_transgender |
| 6. | human | 3: [10, 10.0], 12: [15, inf] | human rights united | Universal_Declaration_of_Human_Rights |
| 7. | least | 3: [10, inf], 31: [10, 10.0], 35: [13, 13.0] | least people killed | List_of_people_killed_for_being_transgender |
| 8. | olympics | 6: [11, inf] | olympics sochi winter | 2014_Winter_Olympics |
| 9. | round | 7: [11, inf] | round talks first | Polish_Round_Table_Agreement |
| 10. | many | 8: [13, 6.5], 17: [12, inf], 28: [11, 5.5], 48: [13, 6.5] | many china government | Politics_of_China |
| 11. | young | 8: [10, 10.0], 21: [15, inf] | young people hong | Hong_Jin-young |
| 12. | crimea | 9: [22, inf] | crimea russia ukraine | Annexation_of_Crimea_by_the_Russian_Federation |
| 13. | saturday | 10: [12, inf] | saturday people least | Saturday_Night_Massacre |
| 14. | john | 10: [11, inf], 28: [13, inf] | john kerry state | John_Kerry |
| 15. | women | 10: [18, inf], 39: [14, 7.0] | women rights sexual | Women's_rights |
| 16. | last | 10: [12, inf], 32: [12, 6.0], 49: [11, 5.5] | last week month | ISO_week_date |
| 17. | secretary | 10: [11, 5.5], 28: [14, inf] | secretary kerry state | John_Kerry |
| 18. | kerry | 10: [17, 8.5], 28: [19, inf] | kerry state secretary | John_Kerry |
| 19. | plane | 11: [18, 6.0], 29: [14, inf] | plane malaysia airlines | Malaysia_Airlines_Flight_370 |
| 20. | nuclear | 12: [13, inf], 45: [11, 11.0] | nuclear iran talks | Joint_Comprehensive_Plan_of_Action |
| 21. | run | 13: [10, inf] | run party president | Cory_Booker_2020_presidential_campaign |
| 22. | israel | 14: [14, inf], 28: [27, 5.4] | israel gaza israeli | Gaza–Israel_conflict |
| 23. | series | 14: [10, inf] | series china attacks | School_attacks_in_China |
| 24. | beijing | 15: [15, inf], 40: [20, 5.0] | beijing china hong | Time_in_China |
| 25. | girlfriend | 15: [10, inf] | girlfriend pistorius oscar | Trial_of_Oscar_Pistorius |
| 26. | top | 15: [15, inf], 24: [10, inf] | top china official | China |
| 27. | days | 16: [11, inf] | days two ukraine | Ukraine_International_Airlines_Flight_752 |
| 28. | sanctions | 16: [11, inf] | sanctions russia ukraine | International_sanctions_during_the_Ukrainian_crisis |
| 29. | ferry | 16: [18, inf] | ferry south korean | Sinking_of_MV_Sewol |
| 30. | sinking | 16: [11, inf] | sinking ferry south | Sinking_of_MV_Sewol |
| 31. | putin | 16: [16, 5.33], 49: [10, inf] | putin president russia | Vladimir_Putin |
| 32. | xinjiang | 18: [12, inf] | xinjiang region china | Xinjiang |
| 33. | train | 18: [12, inf] | train station kunming | 2014_Kunming_attack |
| 34. | vietnam | 19: [14, inf] | vietnam china chinese | China–Vietnam_relations |
| 35. | deal | 21: [10, inf] | deal iran nuclear | Iran_nuclear_deal_framework |
| 36. | possible | 21: [11, inf] | possible china iran | China–Iran_relations |
| 37. | law | 21: [10, 10.0], 43: [12, inf] | law china court | Chinese_law |
| 38. | thai | 21: [12, inf] | thai thailand military | Royal_Thai_Armed_Forces |
| 39. | thailand | 21: [10, inf] | thailand military thai | Royal_Thai_Armed_Forces |
| 40. | pakistan | 21: [11, inf], 41: [12, 12.0] | pakistan pakistani taliban | Tehrik-i-Taliban_Pakistan |
| 41. | pope | 21: [11, 11.0], 28: [10, inf], 33: [10, 10.0] | pope francis vatican | Pope_Francis |
| 42. | union | 22: [14, inf] | union european ukraine | Ukraine–European_Union_relations |
| 43. | plan | 23: [10, inf] | plan would government | United_States_federal_government_continuity_of_operations |
| 44. | sgt | 23: [15, inf] | sgt bergdahl bowe | Bowe_Bergdahl |
| 45. | assault | 24: [19, inf] | assault sexual militants | Harvey_Weinstein_sexual_abuse_cases |
| 46. | woman | 24: [10, 10.0], 26: [11, inf], 49: [15, 15.0] | woman death women | Trans_woman |
| 47. | mosul | 24: [13, inf] | mosul iraq militants | Battle_of_Mosul_(2016–17) |
| 48. | japan | 24: [14, inf] | japan china minister | China–Japan_relations |
| 49. | baghdad | 24: [16, inf], 26: [10, 5.0] | baghdad iraq iraqi | Baghdad |
| 50. | abdullah | 25: [12, inf] | abdullah afghan candidate | Abdullah_Abdullah |
| 51. | suspect | 25: [12, inf] | suspect killing benghazi | 2012_Benghazi_attack |
| 52. | benghazi | 25: [11, inf] | benghazi attack libya | 2012_Benghazi_attack |
| 53. | helped | 26: [11, inf] | helped president putin | Vladimir_Putin |
| 54. | french | 27: [10, inf], 30: [10, inf], 47: [11, 5.5] | french france president | President_of_France |
| 55. | home | 28: [11, inf], 49: [11, 11.0] | home china return | Mainland_Travel_Permit_for_Hong_Kong_and_Macao_Residents |
| 56. | troops | 28: [11, 5.5], 34: [11, 5.5], 38: [11, inf] | troops ukraine u.s. | Internal_Troops_of_Ukraine |
| 57. | gaza | 28: [23, inf] | gaza israel israeli | Gaza–Israel_conflict |
| 58. | shot | 29: [14, inf] | shot israeli killed | List_of_Israeli_assassinations |
| 59. | downing | 29: [13, inf] | downing ukraine russia | Russo-Ukrainian_War |
| 60. | malaysia | 29: [22, inf] | malaysia airlines flight | Malaysia_Airlines_Flight_370 |
| 61. | airlines | 29: [19, inf] | airlines malaysia flight | Malaysia_Airlines_Flight_370 |
| 62. | jet | 29: [21, inf] | jet malaysia search | Search_for_Malaysia_Airlines_Flight_370 |
| 63. | food | 30: [10, inf] | food china aid | Aid |
| 64. | site | 30: [21, 21.0], 44: [15, 15.0], 50: [10, inf] | site crash police | Germanwings_Flight_9525 |
| 65. | corruption | 31: [13, inf] | corruption china former | Corruption_in_China |
| 66. | head | 31: [11, inf] | head china former | Head_of_the_former_Chinese_imperial_clan |
| 67. | african | 32: [11, inf] | african south central | Central_Africa |
| 68. | premier | 32: [10, inf] | premier minister prime | Prime_minister |
| 69. | children | 32: [11, inf] | children killed china | 1994_Karamay_fire |
| 70. | convoy | 33: [13, inf] | convoy ukraine aid | Aid_Convoy |
| 71. | opposition | 33: [10, inf] | opposition leader government | Leader_of_the_Opposition_(India) |
| 72. | foley | 34: [12, inf] | foley james journalist | James_Foley_(journalist) |
| 73. | northern | 35: [10, inf] | northern iraq militants | Northern_Iraq_offensive_(June_2014) |
| 74. | europe | 35: [10, inf] | europe russia european | European_Russia |
| 75. | scotland | 37: [10, inf] | scotland independence vote | 2014_Scottish_independence_referendum |
| 76. | nearly | 37: [10, inf] | nearly two years | I'll_Be_Gone_in_the_Dark |
| 77. | arab | 37: [11, 5.5], 39: [10, inf], 47: [13, inf] | arab united spring | Arab_Spring |
| 78. | – | 38: [10, inf] | – general assembly | United_Nations_General_Assembly |
| 79. | general | 38: [20, inf] | general united nations | Secretary-General_of_the_United_Nations |
| 80. | assembly | 38: [19, inf] | assembly general united | United_Nations_General_Assembly |
| 81. | life | 39: [15, inf] | life china chinese | China_Life_Insurance_Company |
| 82. | reported | 39: [10, inf] | reported china news | Fox_News |
| 83. | protesters | 40: [38, 7.6], 47: [11, inf] | protesters hong kong | 2019–20_Hong_Kong_protests |
| 84. | demonstrations | 40: [18, inf] | demonstrations hong kong | 1967_Hong_Kong_riots |
| 85. | communist | 40: [13, inf] | communist party china | Chinese_Communist_Party |
| 86. | water | 40: [10, inf] | water china iraq | Iraq |
| 87. | kobani | 41: [10, inf] | kobani syrian islamic | Siege_of_Kobanî |
| 88. | nurse | 41: [13, inf] | nurse ebola spanish | Ebola_virus_cases_in_the_United_States |
| 89. | might | 41: [10, inf] | might china american | Chinese_Americans |
| 90. | toll | 42: [11, inf] | toll death killed | List_of_wars_by_death_toll |
| 91. | tunisia | 43: [10, inf] | tunisia arab country | Tunisia |
| 92. | soldier | 43: [10, inf] | soldier killed american | Soldier_(1998_American_film) |
| 93. | ottawa | 43: [10, inf] | ottawa gunman police | 2014_shootings_at_Parliament_Hill,_Ottawa |
| 94. | criticism | 44: [10, inf] | criticism president government | Criticism_of_the_Israeli_government |
| 95. | burkina | 44: [11, inf] | burkina faso president | List_of_heads_of_state_of_Burkina_Faso |
| 96. | faso | 44: [11, inf] | faso burkina president | COVID-19_pandemic_in_Burkina_Faso |
| 97. | camp | 48: [10, inf], 50: [10, inf] | camp hong kong | Pro-Beijing_camp_(Hong_Kong) |
| 98. | internet | 49: [10, inf] | internet chinese china | Internet_censorship_in_China |
| 99. | fight | 49: [11, inf] | fight state isis | Islamic_State_of_Iraq_and_the_Levant |
| 100. | iranian | 49: [10, inf] | iranian iran nuclear | Nuclear_program_of_Iran |
| 101. | typhoon | 49: [11, inf] | typhoon storm haiyan | Typhoon_Haiyan |
| 102. | senate | 50: [10, inf] | senate report committee | Senate_Intelligence_Committee_report_on_CIA_torture |
| 103. | c.i.a | 50: [22, inf] | c.i.a report torture | Senate_Intelligence_Committee_report_on_CIA_torture |
| 104. | climate | 50: [13, inf] | climate china change | Climate_change_in_China |
| 105. | sydney | 51: [11, inf] | sydney gunman cafe | Lindt_Cafe_siege |
| 106. | sony | 51: [14, inf] | sony north korea | Sony_Pictures_hack |
| 107. | cuba | 51: [31, inf] | cuba u.s. relations | Cuba–United_States_relations |
| 108. | relations | 51: [13, inf] | relations president china | China–United_States_relations |
| 109. | christmas | 52: [19, inf] | christmas international herald | Christmas |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | ukraine | 4: [10, inf], 8: [22, inf] | ukraine russia 's | Ukrainians_in_Russia |
| 2. | voices | 4: [15, inf] | voices brazil 's | Voice_acting |
| 3. | brazil | 4: [14, inf] | brazil 's voices | Voice_acting |
| 4. | manus | 8: [15, inf] | manus island asylum | Manus_Island |
| 5. | island | 8: [11, inf] | island manus asylum | Manus_Island |
| 6. | crimea | 9: [12, inf] | crimea ukraine russia | Russo-Ukrainian_War |
| 7. | flight | 11: [22, 5.5], 29: [14, inf] | flight mh malaysia | Malaysia_Airlines_Flight_370 |
| 8. | mh | 11: [27, 27.0], 29: [63, inf] | mh flight search | Malaysia_Airlines_Flight_370 |
| 9. | audit | 18: [13, inf] | audit commission says | Election_audit |
| 10. | cuts | 20: [10, inf] | cuts budget 's | Budget_Cuts |
| 11. | post-soviet | 24: [19, inf] | post-soviet world need | Post-Soviet_states |
| 12. | know | 24: [18, inf] | know need world | GMA3:_What_You_Need_To_Know |
| 13. | isis | 24: [16, inf], 32: [15, 15.0] | isis us iraq | Islamic_State_of_Iraq_and_the_Levant |
| 14. | iraq | 24: [24, inf], 32: [10, inf] | iraq us isis | Islamic_State_of_Iraq_and_the_Levant |
| 15. | malaysia | 29: [16, inf] | malaysia airlines mh | Malaysia_Airlines_Flight_370 |
| 16. | airlines | 29: [15, inf] | airlines malaysia mh | Malaysia_Airlines_Flight_17 |
| 17. | strikes | 32: [11, inf], 39: [13, 13.0] | strikes air isis | International_military_intervention_against_ISIL |
| 18. | ferguson | 33: [16, inf] | ferguson police brown | Shooting_of_Michael_Brown |
| 19. | james | 34: [10, inf] | james foley 's | James_Foley_(journalist) |
| 20. | foley | 34: [12, inf] | foley james us | James_Foley_(journalist) |
| 21. | pistorius | 37: [12, inf] | pistorius oscar trial | Trial_of_Oscar_Pistorius |
| 22. | ottawa | 43: [10, inf] | ottawa shooting soldier | 2014_shootings_at_Parliament_Hill,_Ottawa |
| 23. | sudan | 50: [10, inf] | sudan south 's | South_Sudan |
