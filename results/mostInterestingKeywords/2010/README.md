# Keywords with the highest 'interestingness' in 2010

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
| 1. | two | 1: [10, inf] | two killed officials | American_fatalities_and_injuries_of_the_2012_Benghazi_attack |
| 2. | prime | 1: [10, 5.0], 29: [10, inf] | prime minister government | Prime_minister |
| 3. | leader | 1: [20, 10.0], 4: [10, inf], 18: [20, 5.0], 31: [10, 10.0], 34: [17, 8.5], 50: [12, 6.0] | leader president minister | Minister-president |
| 4. | three | 1: [10, inf] | three killed officials | Threatening_government_officials_of_the_United_States |
| 5. | suicide | 1: [10, 5.0], 20: [10, inf] | suicide attack bomber | Suicide_attack |
| 6. | haiti | 2: [22, inf] | haiti earthquake aid | 2010_Haiti_earthquake |
| 7. | google | 2: [16, inf] | google china u.s. | Google_China |
| 8. | relief | 2: [11, inf] | relief aid haiti | 2010_Haiti_earthquake |
| 9. | elections | 3: [10, inf] | elections party iraq | Elections_in_Iraq |
| 10. | gates | 3: [12, inf], 10: [12, inf] | gates defense secretary | Robert_Gates |
| 11. | shiite | 5: [10, inf] | shiite iraq iraqi | Sons_of_Iraq |
| 12. | pakistan | 5: [13, 6.5], 39: [11, 11.0], 42: [11, inf] | pakistan u.s. taliban | Tehrik-i-Taliban_Pakistan |
| 13. | candidates | 5: [11, inf] | candidates election iraq | Elections_in_Iraq |
| 14. | clinton | 7: [16, 8.0], 48: [11, inf] | clinton state secretary | Hillary_Clinton's_tenure_as_Secretary_of_State |
| 15. | women | 7: [10, inf] | women rights afghan | Women_in_Afghanistan |
| 16. | vote | 9: [15, 15.0], 18: [11, inf], 37: [15, inf] | vote election minister | Prime_Minister_of_Spain |
| 17. | obama | 10: [11, inf] | obama president u.s. | Barack_Obama |
| 18. | report | 10: [11, 5.5], 50: [14, inf] | report says u.n. | Woodbury_matrix_identity |
| 19. | north | 12: [12, inf], 16: [24, 6.0] | north korea south | North_Korea–South_Korea_relations |
| 20. | korea | 12: [11, 11.0], 20: [11, 11.0], 31: [12, inf], 45: [16, 8.0] | korea north south | North_Korea–South_Korea_relations |
| 21. | polish | 14: [11, inf] | polish poland crash | Smolensk_air_disaster |
| 22. | iraqi | 16: [10, 5.0], 36: [11, inf] | iraqi iraq government | Iraqi_Kurdistan |
| 23. | nato | 16: [13, inf], 26: [11, 5.5], 46: [10, 5.0] | nato afghan afghanistan | War_in_Afghanistan_(2001–present) |
| 24. | jong-il | 18: [10, inf] | jong-il north korea | Kim_Jong-il |
| 25. | monaco | 19: [10, inf] | monaco schumacher grand | Michael_Schumacher |
| 26. | sanctions | 20: [14, inf], 23: [14, 7.0] | sanctions iran nuclear | Sanctions_against_Iran |
| 27. | europe | 20: [10, inf] | europe european u.s. | European_Union |
| 28. | base | 20: [16, inf] | base u.s. afghanistan | United_States_invasion_of_Afghanistan |
| 29. | accused | 21: [10, inf] | accused u.s. government | Zionist_Occupation_Government_conspiracy_theory |
| 30. | gang | 21: [10, inf] | gang leader jamaica | Shower_Posse |
| 31. | turkey | 22: [21, 10.5], 26: [11, inf] | turkey israel raid | Gaza_flotilla_raid |
| 32. | effort | 23: [12, 6.0], 26: [10, inf] | effort u.s. iran | Iran–United_States_relations |
| 33. | kyrgyz | 24: [10, inf] | kyrgyz president violence | Kyrgyz_Revolution_of_2010 |
| 34. | abuse | 25: [10, inf] | abuse pope church | Catholic_Church_sexual_abuse_cases |
| 35. | gas | 25: [14, inf] | gas police belarus | 2020–2021_Belarusian_protests |
| 36. | belarus | 25: [14, inf] | belarus russia gas | Belarus–Russia_relations |
| 37. | whaling | 25: [10, inf] | whaling japan japanese | Whaling_in_Japan |
| 38. | mcchrystal | 25: [13, inf] | mcchrystal gen. stanley | Stanley_A._McChrystal |
| 39. | church | 25: [10, inf] | church abuse pope | Catholic_Church_sexual_abuse_cases |
| 40. | japan | 27: [10, inf] | japan minister party | Liberal_Democratic_Party_(Japan) |
| 41. | uganda | 28: [13, inf] | uganda attacks bombings | 2010_Kampala_bombings |
| 42. | south | 31: [10, 5.0], 45: [11, inf] | south korea north | North_Korea–South_Korea_relations |
| 43. | election | 32: [17, 8.5], 44: [12, inf], 47: [11, 5.5] | election vote president | List_of_United_States_presidential_elections_in_which_the_winner_lost_the_popular_vote |
| 44. | ramadan | 32: [10, inf] | ramadan iraqi kashmir | India–Iraq_relations |
| 45. | former | 34: [14, inf] | former president minister | List_of_presidents_of_India |
| 46. | weekend | 34: [10, inf] | weekend killed grand | 1994_San_Marino_Grand_Prix |
| 47. | miners | 34: [10, inf] | miners trapped chile | 2010_Copiapó_mining_accident |
| 48. | states | 35: [11, inf] | states united u.s. | U.S._state |
| 49. | iran | 36: [12, inf] | iran nuclear sanctions | Sanctions_against_Iran |
| 50. | ferrari | 36: [10, inf] | ferrari team alonso | Scuderia_Ferrari |
| 51. | roma | 37: [14, inf] | roma france european | Romani_people |
| 52. | pope | 37: [12, inf] | pope abuse benedict | The_Two_Popes |
| 53. | sludge | 40: [10, inf] | sludge red hungary | Ajka_alumina_plant_accident |
| 54. | prize | 40: [11, inf], 49: [13, inf] | prize nobel peace | Nobel_Peace_Prize |
| 55. | european | 42: [10, inf] | european union europe | European_Union |
| 56. | cities | 42: [10, inf] | cities india attacks | 2008_Mumbai_attacks |
| 57. | results | 47: [10, inf] | results election president | Attempts_to_overturn_the_2020_United_States_presidential_election |
| 58. | view | 48: [11, inf] | view many reports | Mountain_View,_California |
| 59. | nobel | 49: [16, inf] | nobel prize china | Nobel_Prize_in_Literature |
| 60. | use | 51: [10, inf] | use north korea | North_Korea |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | earthquake | 2: [15, inf], 15: [10, 5.0] | earthquake haiti chile | 2010_Haiti_earthquake |
| 2. | haiti | 2: [32, inf] | haiti earthquake 's | 2010_Haiti_earthquake |
| 3. | dubai | 7: [14, inf] | dubai killing murder | Assassination_of_Mahmoud_Al-Mabhouh |
| 4. | moscow | 13: [13, inf] | moscow 's mayor | Mayor_of_Moscow |
| 5. | volcano | 15: [10, inf] | volcano iceland ash | Eyjafjallajökull |
| 6. | attack | 22: [14, inf], 47: [10, 10.0] | attack gaza flotilla | Gaza_flotilla_raid |
| 7. | g | 25: [11, inf] | g summit aid | Group_of_Eight |
| 8. | spy | 26: [23, inf] | spy russian ring | Illegals_Program |
| 9. | ring | 26: [16, inf] | ring russian spy | Illegals_Program |
| 10. | anna | 26: [10, inf] | anna chapman spy | Anna_Chapman |
| 11. | chapman | 26: [10, inf] | chapman anna spy | Anna_Chapman |
| 12. | taliban | 29: [10, 10.0], 47: [10, inf] | taliban us afghanistan | War_in_Afghanistan_(2001–present) |
| 13. | logs | 29: [18, inf], 42: [15, inf] | logs afghanistan iraq | Iraq_War_documents_leak |
| 14. | peace | 35: [12, inf], 49: [11, 5.5] | peace talks middle | List_of_Middle_East_peace_proposals |
| 15. | roma | 37: [10, inf] | roma france 's | A.S._Roma |
| 16. | korean | 47: [10, inf] | korean north south | North_Korea–South_Korea_relations |
| 17. | embassy | 47: [62, inf] | embassy us cables | United_States_diplomatic_cables_leak |
| 18. | cables | 47: [61, inf] | cables us embassy | United_States_diplomatic_cables_leak |
| 19. | iranian | 47: [15, inf] | iranian us embassy | Iranian_Embassy_siege |
| 20. | russia | 48: [11, inf] | russia us 's | Russia–United_States_relations |
| 21. | president | 48: [20, inf] | president 's cables | United_States_diplomatic_cables_leak |
| 22. | berlusconi | 48: [11, inf], 50: [12, 6.0] | berlusconi silvio 's | Pier_Silvio_Berlusconi |
| 23. | pakistan | 48: [40, inf] | pakistan us cables | United_States_diplomatic_cables_leak |
| 24. | nicolas | 48: [10, inf] | nicolas sarkozy 's | Nicolas_Sarkozy |
| 25. | army | 48: [11, inf] | army us pakistan | Pakistan_Army |
| 26. | karzai | 48: [11, inf] | karzai hamid us | Hamid_Karzai |
| 27. | putin | 48: [17, inf] | putin vladimir cables | Public_image_of_Vladimir_Putin |
| 28. | nobel | 49: [10, inf] | nobel prize peace | Nobel_Peace_Prize |
| 29. | prize | 49: [10, inf] | prize nobel peace | Nobel_Peace_Prize |
| 30. | kosovo | 49: [11, inf] | kosovo us cables | Contents_of_the_United_States_diplomatic_cables_leak_(Europe) |
