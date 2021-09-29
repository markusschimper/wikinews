# Keywords with the highest 'interestingness' in 2018

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
| 1. | abuse | 3: [11, inf] | abuse pope sexual | Catholic_Church_sexual_abuse_cases |
| 2. | australia | 4: [10, inf], 12: [14, inf] | australia australian minister | Prime_Minister_of_Australia |
| 3. | pakistan | 4: [11, inf] | pakistan khan u.s. | Ayub_Khan_(general) |
| 4. | world | 5: [18, inf] | world trump cup | 2026_FIFA_World_Cup |
| 5. | africa | 7: [15, inf] | africa south president | President_of_South_Africa |
| 6. | ramaphosa | 7: [11, inf] | ramaphosa south president | Cyril_Ramaphosa |
| 7. | times | 8: [11, inf] | times york canada | The_New_York_Times |
| 8. | saudi | 9: [10, inf] | saudi arabia prince | Crown_Prince_of_Saudi_Arabia |
| 9. | prince | 9: [11, inf], 17: [10, inf], 20: [13, 13.0] | prince saudi crown | Crown_Prince_of_Saudi_Arabia |
| 10. | meeting | 10: [12, inf] | meeting trump president | Donald_Trump |
| 11. | political | 10: [18, 6.0], 22: [16, inf] | political president minister | Minister_President_of_Prussia |
| 12. | court | 11: [12, inf], 29: [11, 5.5] | court supreme government | Supreme_Court_of_the_United_States |
| 13. | afghan | 11: [11, inf] | afghan taliban attack | Taliban_insurgency |
| 14. | mr. | 12: [14, inf], 19: [12, 12.0] | mr. trump president | Donald_Trump |
| 15. | taliban | 13: [10, inf] | taliban afghan afghanistan | War_in_Afghanistan_(2001–present) |
| 16. | skripal | 13: [10, inf] | skripal sergei agent | Poisoning_of_Sergei_and_Yulia_Skripal |
| 17. | brazil | 14: [11, inf] | brazil president former | President_of_Brazil |
| 18. | lula | 14: [11, inf] | lula brazil president | Luiz_Inácio_Lula_da_Silva |
| 19. | prison | 14: [10, inf], 17: [12, inf] | prison years sentenced | List_of_longest_prison_sentences |
| 20. | may | 15: [14, inf] | may minister trump | Ivanka_Trump |
| 21. | deaths | 15: [11, inf] | deaths officials near | Journal_of_Near-Death_Studies |
| 22. | cuba | 16: [13, inf] | cuba president diplomats | Havana_syndrome |
| 23. | driver | 17: [10, inf] | driver killed police | List_of_British_police_officers_killed_in_the_line_of_duty |
| 24. | baby | 17: [10, inf] | baby child first | Grogu |
| 25. | sentenced | 17: [10, inf] | sentenced prison years | List_of_longest_prison_sentences |
| 26. | americans | 19: [10, inf] | americans u.s. trump | Donald_Trump |
| 27. | wedding | 20: [11, inf] | wedding markle royal | Wedding_of_Prince_Harry_and_Meghan_Markle |
| 28. | ireland | 21: [19, inf] | ireland abortion irish | Abortion_in_the_Republic_of_Ireland |
| 29. | abortion | 21: [22, inf] | abortion ireland ban | Abortion_law |
| 30. | myanmar | 22: [13, inf] | myanmar rohingya ethnic | Rohingya_genocide |
| 31. | migrants | 24: [11, inf] | migrants asylum migrant | Migrant_worker |
| 32. | united | 24: [18, inf], 26: [15, 5.0], 28: [11, 5.5] | united states nations | Member_states_of_the_United_Nations |
| 33. | erdogan | 25: [13, inf] | erdogan president turkey | Recep_Tayyip_Erdoğan |
| 34. | cave | 26: [13, inf] | cave soccer boys | Tham_Luang_cave_rescue |
| 35. | coach | 26: [10, inf] | coach cave boys | Tham_Luang_cave_rescue |
| 36. | boys | 26: [10, inf] | boys cave coach | Tham_Luang_cave_rescue |
| 37. | novichok | 27: [10, inf] | novichok nerve agent | Novichok_agent |
| 38. | nerve | 27: [10, inf] | nerve agent spy | Nerve_agent |
| 39. | agent | 27: [10, inf] | agent nerve spy | Nerve_agent |
| 40. | toronto | 30: [12, inf] | toronto canada police | Toronto_Police_Service |
| 41. | imran | 30: [10, inf] | imran pakistan khan | Imran_Khan |
| 42. | khan | 30: [15, inf] | khan pakistan imran | Imran_Khan |
| 43. | dam | 30: [13, inf] | dam laos people | Dams_and_reservoirs_in_Laos |
| 44. | markle | 20: [19, 19.0] | markle meghan prince | Wedding_of_Prince_Harry_and_Meghan_Markle |
| 45. | military | 4: [18, 18.0], 28: [13, 13.0] | military trump president | Donald_Trump |
| 46. | nuclear | 10: [16, 8.0], 17: [16, 16.0], 19: [21, 5.25] | nuclear north iran | Nuclear_program_of_Iran |
| 47. | jong-un | 10: [15, 15.0], 21: [11, 5.5] | jong-un north korea | Kim_Jong-un |
| 48. | visit | 13: [10, 5.0], 28: [15, 15.0] | visit trump president | Donald_Trump |
| 49. | meghan | 20: [15, 15.0] | meghan markle prince | Wedding_of_Prince_Harry_and_Meghan_Markle |
| 50. | chinese | 15: [14, 14.0] | chinese china beijing | Beijing |
| 51. | leaders | 17: [13, 13.0] | leaders trump president | Donald_Trump |
| 52. | deadly | 30: [13, 13.0] | deadly attack least | 2020_Aden_attacks |
| 53. | nato | 28: [25, 12.5] | nato trump president | Donald_Trump |
| 54. | prime | 11: [22, 5.5], 18: [12, 12.0] | prime minister may | Prime_minister |
| 55. | royal | 20: [12, 12.0] | royal prince markle | Wedding_of_Prince_Harry_and_Meghan_Markle |
| 56. | canada | 2: [10, 10.0], 15: [11, 11.0], 22: [11, 5.5] | canada letter trump | Trump_tariffs |
| 57. | death | 15: [11, 11.0], 30: [12, 6.0] | death killing toll | List_of_wars_and_anthropogenic_disasters_by_death_toll |
| 58. | hundreds | 17: [11, 11.0] | hundreds thousands killed | Hundred_Thousand_Martyrs_of_Tbilisi |
| 59. | deal | 19: [15, 5.0], 26: [11, 11.0] | deal iran trump | United_States_withdrawal_from_the_Joint_Comprehensive_Plan_of_Action |
| 60. | army | 4: [10, 10.0] | army military afghan | Afghan_National_Army |
| 61. | found | 5: [10, 10.0] | found government police | Metropolitan_Police_Department_of_the_District_of_Columbia |
| 62. | spy | 10: [10, 10.0] | spy russian former | Illegals_Program |
| 63. | five | 12: [10, 10.0] | five years killed | AFI's_100_Years...100_Movie_Quotes |
| 64. | return | 12: [10, 10.0] | return north korea | North_Korea |
| 65. | harry | 20: [10, 10.0] | harry markle prince | Wedding_of_Prince_Harry_and_Meghan_Markle |
| 66. | foreign | 23: [10, 10.0] | foreign trump china | Foreign_policy_of_the_Donald_Trump_administration |
| 67. | historic | 24: [10, 10.0] | historic north meeting | North_Sandwich_Meeting_House |
| 68. | security | 24: [10, 10.0] | security forces military | Military_police |
| 69. | refugee | 25: [10, 10.0] | refugee agency u.n. | United_Nations_High_Commissioner_for_Refugees |
| 70. | mexico | 26: [10, 10.0] | mexico trump u.s. | Trump_wall |
| 71. | interview | 28: [10, 10.0] | interview trump president | Donald_Trump |
| 72. | minister | 11: [33, 8.25], 18: [18, 9.0] | minister prime party | Prime_Minister_of_the_United_Kingdom |
| 73. | iran | 17: [17, 8.5] | iran trump nuclear | United_States_withdrawal_from_the_Joint_Comprehensive_Plan_of_Action |
| 74. | police | 19: [17, 8.5] | police killed officers | List_of_law_enforcement_officers_killed_in_the_line_of_duty_in_the_United_States |
| 75. | spain | 22: [16, 8.0] | spain catalan minister | Catalan_declaration_of_independence |
| 76. | crash | 15: [15, 7.5] | crash bus plane | Humboldt_Broncos_bus_crash |
| 77. | gaza | 20: [22, 7.33] | gaza israel israeli | Gaza–Israel_conflict |
| 78. | officials | 15: [14, 7.0], 29: [13, 6.5] | officials say north | 2018_Hawaii_false_missile_alert |
| 79. | trump-kim | 24: [14, 7.0] | trump-kim meeting korea | 2018_North_Korea–United_States_Singapore_Summit |
| 80. | weapons | 9: [13, 6.5], 15: [10, 5.0] | weapons chemical syria | Syria_chemical_weapons_program |
| 81. | trump | 28: [80, 6.15] | trump president north | Donald_Trump |
| 82. | europe | 13: [12, 6.0], 26: [10, 5.0] | europe trump italy | Foreign_policy_of_the_Donald_Trump_administration |
| 83. | two | 21: [12, 6.0] | two years president | Vice_President_of_the_United_States |
| 84. | pompeo | 21: [12, 6.0] | pompeo state secretary | Mike_Pompeo |
| 85. | peace | 24: [12, 6.0] | peace south talks | 2013–2014_Israeli–Palestinian_peace_talks |
| 86. | wave | 30: [12, 6.0] | wave heat country | Heat_wave |
| 87. | china | 18: [17, 5.67] | china xi chinese | Xi_Jinping |
| 88. | britain | 28: [17, 5.67] | britain may trump | List_of_conspiracy_theories_promoted_by_Donald_Trump |
| 89. | election | 4: [10, 5.0], 9: [11, 5.5] | election president vote | List_of_United_States_presidential_elections_in_which_the_winner_lost_the_popular_vote |
| 90. | south | 5: [22, 5.5] | south korea north | North_Korea–South_Korea_relations |
| 91. | dozens | 8: [11, 5.5] | dozens killed people | The_Dozens |
| 92. | protest | 18: [11, 5.5] | protest thousands president | Protests_against_Donald_Trump |
| 93. | country | 26: [22, 5.5] | country president leader | President_of_the_Republic_of_China |
| 94. | took | 28: [11, 5.5] | took president country | President_of_the_United_States |
| 95. | says | 2: [10, 5.0] | says president trump | Donald_Trump |
| 96. | group | 2: [10, 5.0] | group says isis | Islamic_State_of_Iraq_and_the_Levant |
| 97. | peru | 3: [10, 5.0] | peru pope abuse | Pope_Benedict_XVI |
| 98. | turkey | 4: [15, 5.0] | turkey erdogan president | Recep_Tayyip_Erdoğan |
| 99. | hong | 6: [10, 5.0] | hong kong china | Hong_Kong |
| 100. | kong | 6: [10, 5.0] | kong hong china | Hong_Kong |
| 101. | gay | 6: [10, 5.0] | gay police toronto | 2010–2017_Toronto_serial_homicides |
| 102. | states | 7: [10, 5.0] | states united trump | Donald_Trump |
| 103. | charges | 7: [10, 5.0] | charges court former | Impeachment |
| 104. | netanyahu | 7: [10, 5.0] | netanyahu prime minister | Sara_Netanyahu |
| 105. | bus | 8: [10, 5.0] | bus crash killing | Swift_Current_Broncos_bus_crash |
| 106. | girls | 12: [10, 5.0] | girls boko haram | Boko_Haram |
| 107. | north | 15: [10, 5.0] | north korea south | North_Korea–South_Korea_relations |
| 108. | state | 24: [10, 5.0] | state islamic secretary | Islamic_State_of_Iraq_and_the_Levant |
| 109. | cup | 24: [10, 5.0] | cup world soccer | FIFA_World_Cup |
| 110. | even | 25: [10, 5.0] | even trump china | China–United_States_trade_war |
| 111. | former | 26: [10, 5.0] | former president minister | List_of_presidents_of_India |
| 112. | heat | 30: [10, 5.0] | heat wave temperatures | List_of_heat_waves |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | gaza | 20: [10, inf] | gaza israel violence | Gaza–Israel_conflict |
| 2. | weinstein | 21: [10, inf] | weinstein harvey 's | Harvey_Weinstein |
| 3. | g | 23: [10, inf] | g trump 's | John_G._Trump |
| 4. | hurricane | 37: [12, inf] | hurricane florence maria | Hurricane_Maria |
| 5. | florence | 37: [17, inf] | florence hurricane carolina | Hurricane_Florence |
| 6. | tsunami | 40: [10, inf] | tsunami indonesia death | 2018_Sunda_Strait_tsunami |
| 7. | says | 41: [10, inf] | says 's trump | Donald_Trump |
| 8. | first | 45: [10, inf] | first world 's | First_World |
| 9. | strasbourg | 50: [11, inf] | strasbourg shooting suspect | 2018_Strasbourg_attack |
