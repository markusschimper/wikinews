# Keywords with the highest 'interestingness' in 2020

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
| 1. | missile | 2: [21, inf] | missile iran military | List_of_military_equipment_manufactured_in_Iran |
| 2. | britain | 2: [10, 10.0], 5: [18, inf], 15: [10, 10.0] | britain johnson u.k. | Woody_Johnson |
| 3. | tehran | 2: [10, inf] | tehran iran missile | Iranian_missile_tests |
| 4. | animals | 2: [10, inf] | animals coronavirus australia | COVID-19_pandemic_by_country_and_territory |
| 5. | plane | 2: [15, inf] | plane crash iran | Iran_Air_Flight_277 |
| 6. | ukrainian | 2: [11, inf] | ukrainian iran plane | Ukraine_International_Airlines_Flight_752 |
| 7. | ukraine | 2: [10, inf] | ukraine president zelensky | Volodymyr_Zelensky |
| 8. | near | 2: [10, inf] | near country attack | 2021_Tillabéri_attacks |
| 9. | prince | 2: [14, inf] | prince harry meghan | Meghan,_Duchess_of_Sussex |
| 10. | harry | 2: [13, inf] | harry meghan prince | Wedding_of_Prince_Harry_and_Meghan_Markle |
| 11. | royal | 2: [10, inf] | royal prince harry | Prince_Harry,_Duke_of_Sussex |
| 12. | meghan | 2: [11, inf] | meghan harry prince | Meghan,_Duchess_of_Sussex |
| 13. | hong | 3: [10, 10.0], 21: [13, inf], 27: [17, 5.67] | hong kong china | Hong_Kong |
| 14. | kong | 3: [10, 10.0], 21: [13, inf], 27: [17, 5.67] | kong hong china | Hong_Kong |
| 15. | women | 3: [14, inf] | women president violence | Violence_against_women |
| 16. | executives | 4: [10, inf] | executives dam charges | Mariana_dam_disaster |
| 17. | coronavirus | 4: [30, inf] | coronavirus pandemic china | COVID-19_pandemic |
| 18. | outbreak | 4: [15, inf] | outbreak coronavirus china | COVID-19_pandemic_in_mainland_China |
| 19. | wuhan | 4: [10, inf] | wuhan coronavirus china | COVID-19_pandemic_in_mainland_China |
| 20. | modi | 5: [10, inf] | modi india minister | Narendra_Modi |
| 21. | european | 5: [11, inf], 23: [10, 5.0] | european union e.u | European_Union |
| 22. | union | 5: [11, inf] | union european brexit | Brexit |
| 23. | brexit | 5: [16, inf] | brexit britain european | Brexit |
| 24. | took | 6: [10, inf] | took coronavirus country | COVID-19_pandemic_cases |
| 25. | hospital | 6: [10, inf] | hospital coronavirus medical | Canberra_Coronavirus_Field_Hospital |
| 26. | epidemic | 6: [15, inf] | epidemic coronavirus china | COVID-19_pandemic_in_mainland_China |
| 27. | killed | 6: [12, 6.0], 39: [10, inf] | killed people least | List_of_people_killed_for_being_transgender |
| 28. | ship | 6: [14, inf] | ship cruise japan | COVID-19_pandemic_on_cruise_ships |
| 29. | accused | 7: [14, inf] | accused president government | Student_government_president |
| 30. | might | 7: [10, inf] | might coronavirus election | 2020_United_States_presidential_election |
| 31. | afghan | 8: [11, inf] | afghan taliban peace | Afghan_peace_process |
| 32. | talks | 8: [11, inf] | talks afghan peace | Afghan_peace_process |
| 33. | least | 8: [11, 11.0], 26: [11, 5.5], 43: [10, inf] | least people coronavirus | COVID-19_pandemic |
| 34. | korea | 8: [18, 6.0], 16: [15, 15.0], 30: [10, inf] | korea south north | North_Korea–South_Korea_relations |
| 35. | politics | 9: [12, inf] | politics much could | You_Could_Have_It_So_Much_Better |
| 36. | questions | 9: [10, inf] | questions coronavirus government | COVID-19_pandemic_in_the_United_Kingdom |
| 37. | delhi | 9: [13, inf] | delhi police india | Delhi_Police |
| 38. | migrants | 9: [10, inf] | migrants coronavirus migrant | Indian_migrant_workers_during_the_COVID-19_pandemic |
| 39. | iraq | 11: [12, inf] | iraq iran u.s. | Iran–Iraq_War |
| 40. | spread | 11: [11, inf] | spread coronavirus virus | Misinformation_related_to_the_COVID-19_pandemic |
| 41. | lockdown | 13: [16, 8.0], 28: [10, inf] | lockdown coronavirus virus | COVID-19_lockdown_in_Italy |
| 42. | killing | 13: [15, inf] | killing iran people | Assassination_of_Qasem_Soleimani |
| 43. | japan | 13: [13, inf], 35: [10, inf] | japan coronavirus country | COVID-19_pandemic_by_country_and_territory |
| 44. | leaders | 13: [10, 10.0], 16: [10, inf], 29: [10, 5.0] | leaders president coronavirus | Families_First_Coronavirus_Response_Act |
| 45. | use | 14: [15, inf] | use coronavirus trump | Families_First_Coronavirus_Response_Act |
| 46. | town | 14: [11, inf] | town residents police | The_Residents |
| 47. | court | 14: [11, inf], 24: [13, inf] | court government supreme | Supreme_Court_of_the_United_States |
| 48. | detained | 14: [10, inf] | detained hong kong | 2019–20_Hong_Kong_protests |
| 49. | first | 15: [16, inf], 25: [11, 11.0], 30: [11, inf], 35: [12, inf] | first coronavirus virus | Coronavirus |
| 50. | abuse | 15: [10, inf] | abuse sexual children | Child_sexual_abuse |
| 51. | cease-fire | 15: [10, inf] | cease-fire peace yemen | Saudi_Arabian-led_intervention_in_Yemen |
| 52. | yemen | 15: [10, inf] | yemen saudi u.n. | Saudi_Arabian-led_intervention_in_Yemen |
| 53. | last | 16: [10, inf], 32: [11, 11.0] | last year coronavirus | Coronavirus |
| 54. | north | 16: [15, inf] | north korea south | North_Korea–South_Korea_relations |
| 55. | american | 17: [10, inf], 35: [12, inf], 40: [11, 5.5] | american u.s. trump | Donald_Trump_Jr. |
| 56. | germany | 20: [13, 13.0], 23: [10, inf], 26: [11, 11.0], 40: [10, 5.0] | germany german coronavirus | COVID-19_pandemic_in_Germany |
| 57. | deal | 20: [10, inf] | deal taliban peace | Afghan_peace_process |
| 58. | leader | 21: [14, inf], 33: [10, 5.0] | leader president opposition | Leader_of_the_Opposition_(India) |
| 59. | europe | 21: [10, inf], 24: [10, 10.0] | europe coronavirus cases | COVID-19_pandemic_in_Europe |
| 60. | forces | 21: [16, inf] | forces u.s. security | United_States_Armed_Forces |
| 61. | food | 22: [10, inf] | food coronavirus people | Impact_of_the_COVID-19_pandemic_on_the_food_industry |
| 62. | girl | 23: [11, inf] | girl -year-old german | Milli_Vanilli |
| 63. | floyd | 23: [11, inf] | floyd george killing | Killing_of_George_Floyd |
| 64. | british | 23: [13, inf], 25: [10, 5.0] | british johnson coronavirus | Boris_Johnson |
| 65. | statue | 24: [13, inf] | statue trump protests | George_Floyd_protests_in_Washington,_D.C. |
| 66. | infections | 24: [12, inf] | infections coronavirus cases | COVID-19_pandemic_in_Luxembourg |
| 67. | mass | 24: [10, inf] | mass coronavirus people | COVID-19_pandemic |
| 68. | pilot | 25: [12, inf] | pilot crash air | Dunbeath_air_crash |
| 69. | security | 25: [10, inf] | security hong kong | Hong_Kong_national_security_law |
| 70. | july | 26: [10, inf] | july coronavirus u.s. | COVID-19_pandemic_in_the_United_States |
| 71. | military | 26: [11, inf] | military u.s. iran | Armed_Forces_of_the_Islamic_Republic_of_Iran |
| 72. | base | 26: [10, inf] | base military attack | Camp_Chapman_attack |
| 73. | residents | 26: [13, inf] | residents coronavirus home | Stay-at-home_order |
| 74. | bolsonaro | 28: [12, inf] | bolsonaro brazil president | Jair_Bolsonaro |
| 75. | beirut | 32: [35, inf] | beirut blast lebanon | 2020_Beirut_explosion |
| 76. | explosion | 32: [14, inf] | explosion beirut lebanon | 2020_Beirut_explosion |
| 77. | blast | 32: [19, inf] | blast beirut lebanon | 2020_Beirut_explosion |
| 78. | become | 35: [10, inf] | become coronavirus country | COVID-19_pandemic_by_country_and_territory |
| 79. | abe | 35: [10, inf] | abe japan shinzo | Akie_Abe |
| 80. | set | 36: [10, inf] | set coronavirus country | COVID-19_pandemic_in_Georgia_(country) |
| 81. | camp | 37: [12, inf] | camp auschwitz refugee | Auschwitz_concentration_camp |
| 82. | russia | 38: [10, inf] | russia putin russian | Opposition_to_Vladimir_Putin_in_Russia |
| 83. | families | 39: [10, inf] | families home coronavirus | Families_First_Coronavirus_Response_Act |
| 84. | system | 40: [10, inf] | system health coronavirus | COVID-19_pandemic_by_country_and_territory |
| 85. | positive | 40: [14, inf] | positive coronavirus tested | COVID-19_pandemic_in_Italy |
| 86. | harris | 41: [11, inf] | harris kamala canada | Family_of_Kamala_Harris |
| 87. | scientists | 42: [11, inf] | scientists coronavirus vaccine | COVID-19_vaccine |
| 88. | presidential | 43: [10, inf] | presidential election president | United_States_presidential_election |
| 89. | move | 43: [11, inf] | move coronavirus u.s. | COVID-19_pandemic_in_the_United_States |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | crash | 2: [10, inf] | crash plane iran | Iran_Air_Flight_277 |
| 2. | pandemic | 9: [10, inf] | pandemic coronavirus us | COVID-19_pandemic_in_the_United_States |
| 3. | march | 10: [10, inf] | march coronavirus glance | Timeline_of_the_COVID-19_pandemic_in_March_2020 |
| 4. | april | 14: [19, inf] | april coronavirus glance | Timeline_of_the_COVID-19_pandemic_in_April_2020 |
| 5. | law | 27: [11, inf] | law hong kong | Hong_Kong_national_security_law |
| 6. | beirut | 32: [28, inf] | beirut explosion blast | 2020_Beirut_explosion |
| 7. | explosion | 32: [15, inf] | explosion beirut lebanon | 2020_Beirut_explosion |
