import functions as func
import pandas as pd
import json

week = 7
for i in range(1,week):
    func.weekly_rankings_update(week=i)

func.season_simulation(current_week=week, sims=10000)

# league = func.connect()
# pages = [{'name': team.owners[0]['firstName'], 'fantasy_name': team.team_name, 'path':'/'+team.owners[0]['firstName']} for team in league.teams]
# pages = pages + [{'name':'home', 'fantasy_name': '', 'path':''}]
# print(pages)

# conn = func.connect_db()
# ratings = pd.read_sql_query(f'select player, rating from summary_weekly where week = {1}', conn)#.to_dict('records')
# # print(json.dumps(ratings, indent=4), '\n\n')
# print(ratings)
# ratings = {item['player']:item['rating'] for item in ratings.to_dict('records')}
# print(ratings)


# weekly_stats = pd.read_sql(f'select week, player, round(rating/14,3) as [rating(logan)], score, score_against, outscore_league from summary_weekly where player like "Leeroy Jenkins%"', con=func.connect_db())

# # mask = weekly_stats['week'] == max(weekly_stats['week'])
# # print(mask)
# current_ratings = weekly_stats.loc[weekly_stats['week'] == max(weekly_stats['week']), ['player','rating(logan)']]
# print(current_ratings)


# league = func.connect()

# schedules = func.get_schedules()
# # print(schedules.to_dict('list'))

# # for item in schedules:
# #     print(item)

# current_opp = {item:schedules[item][week-1] for item in schedules}
# print(current_opp)

# print(func.get_opponent_scores())