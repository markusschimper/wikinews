# Keywords with the highest 'interestingness' in 2011

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
| 1. | australia | 1: [10, inf] | australia china swap | Central_bank_liquidity_swap |
| 2. | vote | 1: [10, inf], 37: [10, inf] | vote party prime | Prime_Minister_of_Spain |
| 3. | china | 1: [19, inf], 19: [18, 6.0] | china chinese u.s. | China |
| 4. | sudan | 1: [10, 5.0], 21: [13, 13.0], 45: [13, inf] | sudan south southern | South_Sudan |
| 5. | south | 1: [11, inf], 6: [11, 5.5], 20: [20, 5.0], 22: [11, 11.0], 27: [16, 8.0], 30: [12, 12.0], 43: [11, 5.5] | south korea north | North_Korea–South_Korea_relations |
| 6. | american | 1: [10, inf], 23: [10, 5.0] | american u.s. iraq | American-led_intervention_in_Iraq_(2014–present) |
| 7. | police | 1: [10, inf], 7: [21, 5.25], 35: [15, 5.0] | police officers two | Police_officer |
| 8. | southern | 1: [13, inf], 21: [15, inf] | southern sudan killed | South_Sudan |
| 9. | clinton | 2: [10, inf], 11: [11, 5.5], 48: [10, inf] | clinton secretary state | Hillary_Clinton's_tenure_as_Secretary_of_State |
| 10. | tunisia | 2: [14, inf] | tunisia government egypt | Politics_of_Egypt |
| 11. | months | 2: [12, inf], 38: [13, 13.0], 42: [11, 11.0] | months president government | President_of_the_United_States |
| 12. | french | 3: [10, inf], 51: [10, inf] | french france strauss-kahn | Dominique_Strauss-Kahn |
| 13. | set | 3: [11, inf], 17: [10, 5.0] | set fire tibetan | Self-immolation |
| 14. | international | 3: [11, inf], 14: [10, inf] | international court syria | Syria |
| 15. | suicide | 4: [10, 5.0], 8: [11, inf] | suicide bomber killed | Suicide_attack |
| 16. | airport | 4: [14, inf] | airport bomber suicide | Suicide_attack |
| 17. | mubarak | 4: [19, inf] | mubarak hosni president | Hosni_Mubarak |
| 18. | thousands | 4: [12, inf] | thousands tens protest | January_27,_2007_anti-war_protest |
| 19. | egyptians | 4: [11, inf] | egyptians egypt mubarak | Egyptian_revolution_of_2011 |
| 20. | hosni | 4: [13, inf] | hosni mubarak president | Hosni_Mubarak |
| 21. | caucasus | 4: [10, inf] | caucasus north russia | North_Caucasus |
| 22. | king | 5: [10, inf], 47: [13, 6.5] | king abdullah jordan | Abdullah_II_of_Jordan |
| 23. | diplomats | 5: [10, inf] | diplomats u.s. israel | Israel–United_States_relations |
| 24. | women | 6: [10, 10.0], 9: [10, inf], 37: [10, inf] | women afghan saudi | Women_in_Afghanistan |
| 25. | city | 6: [10, inf] | city forces government | Capital_city |
| 26. | google | 6: [10, inf] | google executive egypt | Google_Street_View |
| 27. | wikileaks | 6: [15, inf] | wikileaks founder cables | United_States_diplomatic_cables_leak |
| 28. | founder | 6: [10, inf] | founder wikileaks assange | Indictment_and_arrest_of_Julian_Assange |
| 29. | bomber | 6: [12, inf], 15: [11, inf] | bomber suicide police | Female_suicide_bomber |
| 30. | pressure | 6: [10, inf] | pressure president united | Thomas_Jefferson |
| 31. | trial | 6: [12, 6.0], 36: [12, inf], 47: [10, 10.0] | trial former mubarak | Hosni_Mubarak |
| 32. | berlusconi | 6: [14, 14.0], 45: [15, inf] | berlusconi prime minister | Silvio_Berlusconi |
| 33. | bahrain | 7: [37, inf] | bahrain protesters protests | Bahraini_uprising_of_2011 |
| 34. | earthquake | 8: [13, inf] | earthquake people japan | 2011_Tōhoku_earthquake_and_tsunami |
| 35. | official | 9: [10, inf], 21: [10, 10.0] | official american government | Official |
| 36. | refugee | 9: [11, inf] | refugee libya refugees | Refugees_of_Libya |
| 37. | afghanistan | 10: [10, 5.0], 16: [12, inf], 27: [17, 5.67] | afghanistan afghan taliban | Taliban |
| 38. | relief | 10: [10, inf] | relief japan would | Japanese_archipelago |
| 39. | biden | 10: [10, inf], 48: [16, inf] | biden vice president | Joe_Biden |
| 40. | near | 10: [15, inf], 28: [10, inf] | near killed border | Deaths_along_the_Bangladesh–India_border |
| 41. | tsunami | 10: [12, inf] | tsunami japan nuclear | 2011_Tōhoku_earthquake_and_tsunami |
| 42. | long | 11: [11, inf] | long reads libya | Libya |
| 43. | human | 11: [10, 10.0], 22: [10, inf] | human rights syria | Human_rights_in_Syria |
| 44. | danger | 11: [14, inf] | danger japan nuclear | Japanese_nuclear_weapon_program |
| 45. | fuel | 11: [11, inf] | fuel nuclear iran | Nuclear_program_of_Iran |
| 46. | food | 11: [11, inf] | food japan prices | 2007–2008_world_food_price_crisis |
| 47. | command | 12: [11, inf] | command libya nato | 2011_military_intervention_in_Libya |
| 48. | nato | 12: [12, inf], 19: [16, 8.0], 43: [10, inf] | nato afghan libya | 2011_military_intervention_in_Libya |
| 49. | questions | 12: [10, inf] | questions raised news | Raised_by_Wolves_(American_TV_series) |
| 50. | water | 12: [10, inf] | water japan plant | Fukushima_Daiichi_Nuclear_Power_Plant |
| 51. | gbagbo | 13: [10, inf] | gbagbo ivory coast | Laurent_Gbagbo |
| 52. | last | 14: [18, 9.0], 44: [11, inf] | last week year | ISO_week_date |
| 53. | school | 14: [10, inf] | school killing students | Barcelona_school_killing |
| 54. | belarus | 15: [12, inf] | belarus president lukashenko | Alexander_Lukashenko |
| 55. | royal | 16: [11, inf] | royal wedding prince | Wedding_of_Prince_William_and_Catherine_Middleton |
| 56. | wedding | 16: [11, inf] | wedding royal prince | Wedding_of_Prince_William_and_Catherine_Middleton |
| 57. | detainees | 17: [12, inf] | detainees guantánamo torture | Guantanamo_Bay_detention_camp |
| 58. | guantánamo | 17: [13, inf] | guantánamo bay detainees | List_of_Guantanamo_Bay_detainees |
| 59. | prison | 17: [17, inf] | prison sentenced years | List_of_longest_prison_sentences |
| 60. | threat | 17: [10, inf] | threat officials u.s. | Threatening_government_officials_of_the_United_States |
| 61. | air | 17: [15, 5.0], 30: [10, inf] | air libya nato | 2011_military_intervention_in_Libya |
| 62. | qaeda | 17: [10, inf] | qaeda laden officials | Osama_bin_Laden |
| 63. | found | 17: [10, inf] | found air former | United_States_Air_Force |
| 64. | osama | 18: [31, inf] | osama laden pakistan | Killing_of_Osama_bin_Laden |
| 65. | laden | 18: [73, inf] | laden osama pakistan | Killing_of_Osama_bin_Laden |
| 66. | raid | 18: [19, inf] | raid pakistan laden | Killing_of_Osama_bin_Laden |
| 67. | militants | 19: [11, 5.5], 33: [10, inf] | militants pakistan killed | Tehrik-i-Taliban_Pakistan |
| 68. | three | 19: [13, 6.5], 45: [10, inf] | three killed officials | Threatening_government_officials_of_the_United_States |
| 69. | queen | 20: [14, inf] | queen elizabeth ireland | Elizabeth_II |
| 70. | african | 20: [10, inf] | african union somalia | African_Union_Mission_to_Somalia |
| 71. | thursday | 20: [14, inf], 32: [10, 10.0], 38: [11, 5.5] | thursday president officials | The_President_Show |
| 72. | town | 21: [10, 5.0], 23: [10, inf] | town forces rebels | Cities_and_towns_during_the_Syrian_Civil_War |
| 73. | ratko | 21: [11, inf] | ratko mladic crimes | Ratko_Mladić |
| 74. | mladic | 21: [18, inf] | mladic ratko crimes | Ratko_Mladić |
| 75. | monaco | 21: [14, inf] | monaco grand prix | Monaco_Grand_Prix |
| 76. | e. | 22: [16, inf] | e. panetta defense | Leon_Panetta |
| 77. | coli | 22: [15, inf] | coli e. germany | 2011_Germany_E._coli_O104:H4_outbreak |
| 78. | health | 22: [10, inf] | health officials coli | Walkerton_E._coli_outbreak |
| 79. | anger | 22: [12, inf] | anger president government | President_of_the_United_States |
| 80. | boy | 22: [10, inf] | boy -year-old killed | Pretty_Boy_Floyd |
| 81. | france | 23: [11, inf] | france french president | President_of_France |
| 82. | rebel | 24: [11, inf], 34: [15, 7.5] | rebel libya rebels | List_of_active_rebel_groups |
| 83. | israeli | 25: [11, 11.0], 33: [10, inf] | israeli israel gaza | Gaza–Israel_conflict |
| 84. | flotilla | 26: [12, inf] | flotilla israel gaza | Gaza_flotilla_raid |
| 85. | pakistani | 27: [10, inf] | pakistani pakistan american | Pakistani_Americans |
| 86. | murdoch | 27: [18, inf] | murdoch hacking british | James_Murdoch |
| 87. | friday | 30: [15, 5.0], 38: [11, inf] | friday president protesters | Timeline_of_protests_against_Donald_Trump |
| 88. | report | 30: [12, inf], 44: [10, 10.0] | report united says | Say_Say_Say |
| 89. | chinese | 30: [10, inf] | chinese china officials | China |
| 90. | italy | 31: [10, inf] | italy minister berlusconi | Silvio_Berlusconi_prostitution_trial |
| 91. | cameron | 32: [10, inf] | cameron prime minister | David_Cameron |
| 92. | riots | 32: [12, inf] | riots people british | 2011_England_riots |
| 93. | britain | 32: [10, inf] | britain cameron british | British_nationalism |
| 94. | drone | 32: [10, inf] | drone pakistan strike | Drone_strikes_in_Pakistan |
| 95. | egypt | 33: [12, inf] | egypt mubarak military | Hosni_Mubarak |
| 96. | tripoli | 33: [14, inf] | tripoli rebels libya | First_Libyan_Civil_War |
| 97. | attacks | 33: [16, inf], 49: [11, 5.5] | attacks killed iraq | Iraqi_insurgency_(2011–2013) |
| 98. | / | 36: [15, inf] | / recalled attacks | September_11_attacks |
| 99. | vettel | 36: [10, inf] | vettel sebastian pole | Sebastian_Vettel |
| 100. | peace | 38: [10, inf] | peace president nobel | Nobel_Peace_Prize |
| 101. | bank | 38: [10, inf] | bank west israeli | Israeli_West_Bank_barrier |
| 102. | anwar | 39: [10, inf] | anwar al-awlaki yemen | Abdulrahman_al-Awlaki |
| 103. | button | 40: [12, inf] | button vettel jenson | Sebastian_Vettel |
| 104. | swap | 41: [10, inf] | swap australia israel | Better_Place_(company) |
| 105. | prisoners | 41: [17, inf] | prisoners political prison | Political_prisoner |
| 106. | turkey | 42: [11, inf], 51: [11, 5.5] | turkey turkish syria | Syria–Turkey_relations |
| 107. | victory | 45: [12, inf] | victory vettel sebastian | Sebastian_Vettel |
| 108. | army | 46: [16, inf] | army military forces | Military_police |
| 109. | veterans | 47: [10, inf] | veterans homeless law | Homeless_veterans_in_the_United_States |
| 110. | vice | 48: [13, inf], 51: [11, inf] | vice president biden | Joe_Biden |
| 111. | authorities | 48: [10, inf] | authorities china chinese | China |
| 112. | hospital | 49: [10, inf] | hospital killed attack | Kunduz_hospital_airstrike |
| 113. | clashes | 50: [10, inf] | clashes protesters forces | Clashes_at_the_Turkish_Ambassador's_Residence_in_Washington,_D.C. |
| 114. | iraqis | 50: [15, inf] | iraqis iraq american | Iraqis |
| 115. | panetta | 50: [11, inf] | panetta defense leon | Leon_Panetta |
| 116. | jong-il | 51: [17, inf] | jong-il north korea | Kim_Jong-il |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | embassy | 2: [11, inf] | embassy us cables | United_States_diplomatic_cables_leak |
| 2. | cables | 2: [11, inf] | cables us embassy | United_States_diplomatic_cables_leak |
| 3. | tunisia | 2: [11, inf], 42: [10, inf] | tunisia 's egypt | Egypt–Tunisia_relations |
| 4. | doc | 3: [10, inf] | doc duvalier 'baby | Jean-Claude_Duvalier |
| 5. | duvalier | 3: [11, inf] | duvalier doc 'baby | Jean-Claude_Duvalier |
| 6. | bahrain | 7: [19, inf], 11: [11, inf] | bahrain 's us | Bahrain–United_States_relations |
| 7. | curveball | 7: [10, inf] | curveball 's lies | Curveball_(informant) |
| 8. | christchurch | 8: [13, inf] | christchurch earthquake hit | 2011_Christchurch_earthquake |
| 9. | earthquake | 8: [16, inf], 10: [20, 6.67] | earthquake japan christchurch | 2011_Christchurch_earthquake |
| 10. | japan | 10: [33, inf] | japan nuclear 's | Nuclear_power_in_Japan |
| 11. | top | 10: [28, inf] | top women 's | Women_on_Top |
| 12. | nuclear | 10: [13, inf] | nuclear japan plant | Nuclear_power_in_Japan |
| 13. | tsunami | 10: [13, inf] | tsunami japan earthquake | 2011_Tōhoku_earthquake_and_tsunami |
| 14. | poland | 14: [11, inf] | poland 's power | Poland |
| 15. | guantánamo | 17: [27, inf] | guantánamo files bay | Guantanamo_Bay_files_leak |
| 16. | bay | 17: [23, inf] | bay guantánamo files | Guantanamo_Bay_files_leak |
| 17. | files | 17: [25, inf] | files guantánamo bay | Guantanamo_Bay_files_leak |
| 18. | ratko | 21: [16, inf] | ratko mladic hague | Ratko_Mladić |
| 19. | mladic | 21: [17, inf] | mladic ratko hague | Ratko_Mladić |
| 20. | coli | 22: [11, inf] | coli outbreak german | 2011_Germany_E._coli_O104:H4_outbreak |
| 21. | sarah | 23: [15, inf] | sarah palin emails | Sarah_Palin_email_hack |
| 22. | palin | 23: [15, inf] | palin sarah emails | Sarah_Palin_email_hack |
| 23. | emails | 23: [11, inf] | emails sarah palin | Sarah_Palin_email_hack |
| 24. | strauss-kahn | 26: [12, inf] | strauss-kahn dominique 's | Dominique_Strauss-Kahn |
| 25. | norway | 29: [10, inf] | norway attacks gunman | 2011_Norway_attacks |
| 26. | israel | 33: [11, inf] | israel gaza 's | Gaza–Israel_conflict |
| 27. | attack | 33: [10, inf] | attack 's nato | 2011_NATO_attack_in_Pakistan |
| 28. | anwar | 39: [13, inf] | anwar al-awlaki al-qaida | Anwar_al-Awlaki |
| 29. | al-awlaki | 39: [14, inf] | al-awlaki anwar yemen | Anwar_al-Awlaki |
| 30. | gilad | 41: [12, inf] | gilad shalit release | Gilad_Shalit |
| 31. | shalit | 41: [11, inf] | shalit gilad release | Gilad_Shalit |
| 32. | elections | 42: [10, inf] | elections 's party | Political_party_strength_in_U.S._states |
| 33. | tunisian | 42: [11, inf] | tunisian election elections | 2011_Tunisian_Constituent_Assembly_election |
| 34. | muammar | 42: [13, inf] | muammar gaddafi 's | Death_of_Muammar_Gaddafi |
| 35. | g | 44: [13, inf] | g summit 's | List_of_G20_summits |
| 36. | iran | 44: [12, inf] | iran 's us | Iran–United_States_relations |
| 37. | jong-il | 51: [21, inf] | jong-il north 's | Kim_Jong-il |
| 38. | north | 51: [19, inf] | north korea 's | North_Korea |
| 39. | korea | 51: [12, inf] | korea north 's | North_Korea |
