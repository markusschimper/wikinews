# Keywords with the highest 'interestingness' in 2009

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
| 1. | cease-fire | 2: [13, inf] | cease-fire gaza israel | Gaza–Israel_clashes_(May_2019) |
| 2. | mexico | 2: [10, inf] | mexico state violence | Violence_against_women_in_Mexico |
| 3. | european | 2: [10, inf] | european union europe | European_Union |
| 4. | president | 3: [11, inf] | president obama leader | Barack_Obama |
| 5. | iran | 3: [10, inf] | iran nuclear president | Nuclear_program_of_Iran |
| 6. | chechen | 3: [10, inf] | chechen rights killed | Second_Chechen_War |
| 7. | election | 5: [30, inf] | election presidential iran | 2009_Iranian_presidential_election |
| 8. | base | 6: [12, inf], 8: [10, inf] | base u.s. american | United_States |
| 9. | chávez | 7: [13, inf] | chávez president hugo | Hugo_Chávez |
| 10. | women | 7: [12, inf] | women indian iraq | History_of_women_in_the_Indian_subcontinent |
| 11. | japan | 8: [10, inf], 13: [11, inf] | japan korea party | Koreans_in_Japan |
| 12. | trial | 8: [21, inf], 27: [10, inf] | trial former leader | Impeachment_trial_of_Donald_Trump |
| 13. | muntader | 8: [12, inf] | muntader al-zaidi iraqi | Muntadhar_al-Zaidi |
| 14. | netanyahu | 8: [10, inf] | netanyahu israel benjamin | Sara_Netanyahu |
| 15. | elections | 10: [10, 5.0], 34: [11, inf] | elections president party | 2002_United_States_House_of_Representatives_elections |
| 16. | may | 10: [13, inf] | may officials iran | Iran–Contra_affair |
| 17. | team | 10: [11, inf] | team – f | Mercedes-Benz_in_Formula_One |
| 18. | spam | 10: [10, inf] | spam cellular sign | Youmail |
| 19. | clinton | 13: [10, inf], 32: [28, inf] | clinton state secretary | Hillary_Clinton's_tenure_as_Secretary_of_State |
| 20. | sports | 13: [11, inf] | sports formula global | 2021_Formula_2_Championship |
| 21. | attack | 14: [12, 6.0], 43: [12, 6.0], 50: [10, inf] | attack killed pakistan | Sectarian_violence_in_Pakistan |
| 22. | militants | 14: [11, inf] | militants pakistan taliban | Tehrik-i-Taliban_Pakistan |
| 23. | pirates | 15: [11, inf] | pirates ship somali | Piracy_off_the_coast_of_Somalia |
| 24. | south | 17: [12, inf], 42: [15, 15.0] | south korea north | North_Korea–South_Korea_relations |
| 25. | pakistani | 18: [15, inf] | pakistani taliban pakistan | Tehrik-i-Taliban_Pakistan |
| 26. | iraqi | 19: [11, 5.5], 30: [11, inf] | iraqi iraq american | Iraqi_Americans |
| 27. | vote | 20: [10, inf] | vote election president | List_of_United_States_presidential_elections_in_which_the_winner_lost_the_popular_vote |
| 28. | leave | 20: [10, inf] | leave iraq north | Iraq |
| 29. | city | 21: [11, 11.0], 52: [13, inf] | city killed police | List_of_law_enforcement_officers_killed_in_the_line_of_duty_in_the_United_States |
| 30. | defense | 22: [11, inf] | defense gates secretary | Robert_Gates |
| 31. | gates | 22: [14, inf] | gates defense secretary | Robert_Gates |
| 32. | secretary | 22: [10, inf] | secretary clinton state | Hillary_Clinton's_tenure_as_Secretary_of_State |
| 33. | army | 23: [11, 11.0], 50: [11, inf] | army pakistani taliban | Tehrik-i-Taliban_Pakistan |
| 34. | plane | 23: [10, inf] | plane crash air | Air_India_Express_Flight_1344 |
| 35. | brown | 23: [15, inf] | brown minister prime | Gordon_Brown |
| 36. | recovered | 23: [10, inf] | recovered bodies air | Air_France_Flight_447 |
| 37. | silverstone | 25: [10, inf] | silverstone paddock last | Development_history_of_Silverstone_Circuit |
| 38. | often | 27: [11, inf] | often china government | Government_of_China |
| 39. | honduras | 27: [16, inf], 39: [12, inf] | honduras president ousted | Manuel_Zelaya |
| 40. | gaza | 27: [10, inf] | gaza israel israeli | Gaza–Israel_conflict |
| 41. | protesters | 28: [12, inf] | protesters iran iranian | 2019–2020_Iranian_protests |
| 42. | korean | 29: [12, inf] | korean north south | North_Korea–South_Korea_relations |
| 43. | indonesia | 29: [12, inf] | indonesia people indonesian | Chinese_Indonesians |
| 44. | biden | 30: [16, inf] | biden president vice | Joe_Biden |
| 45. | journalists | 32: [14, inf] | journalists korea north | 2009_imprisonment_of_American_journalists_by_North_Korea |
| 46. | hillary | 32: [10, inf] | hillary clinton rodham | Hillary_Clinton |
| 47. | rodham | 32: [10, inf] | rodham clinton hillary | Tony_Rodham |
| 48. | schumacher | 33: [10, inf] | schumacher michael formula | Michael_Schumacher |
| 49. | myanmar | 33: [11, inf] | myanmar leader aung | Aung_San_Suu_Kyi |
| 50. | questions | 34: [12, inf] | questions john burns | Steve_Burns |
| 51. | attacks | 34: [14, 7.0], 37: [10, inf], 44: [10, inf], 52: [10, 10.0] | attacks iraq killed | Iraqi_insurgency_(2011–2013) |
| 52. | obama | 36: [11, inf] | obama president u.s. | Barack_Obama |
| 53. | oil | 36: [10, inf] | oil iraq fields | Rumaila_oil_field |
| 54. | protests | 36: [11, inf] | protests iran china | 2017–2018_Iranian_protests |
| 55. | raid | 37: [13, inf] | raid police afghan | Night_raids_in_Afghanistan |
| 56. | reporter | 37: [14, inf] | reporter iran times | The_New_York_Times |
| 57. | sanctions | 39: [12, inf] | sanctions iran nuclear | Sanctions_against_Iran |
| 58. | nobel | 41: [10, inf] | nobel peace prize | Nobel_Peace_Prize |
| 59. | deal | 42: [11, inf], 48: [10, 5.0] | deal iran russia | Iran_nuclear_deal_framework |
| 60. | couple | 44: [13, inf] | couple pirates british | Pirates_of_the_Caribbean:_Dead_Men_Tell_No_Tales |
| 61. | abu | 44: [14, inf] | abu dhabi philippines | Abu_Dhabi_International_Airport |
| 62. | dhabi | 44: [14, inf] | dhabi abu emirates | Emirate_of_Abu_Dhabi |
| 63. | brazil | 48: [12, inf] | brazil air france | Brazilian_Air_Force |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | us | 2: [10, inf], 38: [12, 6.0] | us afghanistan says | War_in_Afghanistan_(2001–present) |
| 2. | zimbabwe | 7: [11, inf] | zimbabwe tsvangirai 's | Morgan_Tsvangirai |
| 3. | president | 10: [11, inf] | president 's former | Living_presidents_of_the_United_States |
| 4. | cricket | 10: [32, inf] | cricket attack sri | 2009_attack_on_the_Sri_Lanka_national_cricket_team |
| 5. | team | 10: [17, inf] | team cricket sri | Sri_Lanka_national_cricket_team |
| 6. | josef | 12: [25, inf] | josef fritzl trial | Fritzl_case |
| 7. | italy | 15: [22, inf] | italy earthquake 's | List_of_earthquakes_in_Italy |
| 8. | swine | 17: [18, inf], 29: [28, 5.6] | swine flu cases | 2009_swine_flu_pandemic |
| 9. | flu | 17: [19, inf], 29: [28, 5.6] | flu swine cases | Swine_influenza |
| 10. | nuclear | 22: [11, inf] | nuclear iran north | Nuclear_program_of_Iran |
| 11. | crash | 23: [11, inf] | crash plane air | Air_India_Express_Flight_1344 |
| 12. | g | 39: [13, inf] | g summit police | Group_of_Eight |
| 13. | plant | 39: [11, inf] | plant nuclear iran | Bushehr_Nuclear_Power_Plant |
| 14. | tsunami | 40: [12, inf] | tsunami samoa dead | 2009_Samoa_earthquake_and_tsunami |
| 15. | samoa | 40: [10, inf] | samoa tsunami dead | 2009_Samoa_earthquake_and_tsunami |
| 16. | lisbon | 40: [10, inf] | lisbon treaty irish | Treaty_of_Lisbon |
