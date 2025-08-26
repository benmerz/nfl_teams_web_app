import csv
import json

# Read CSV and convert to JSON
teams = []

with open('team_data.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        teams.append({
            'team_abbr': row['team_abbr'],
            'team_name': row['team_name'],
            'team_division': row['team_division'],
            'team_logo': row['team_logo_espn']
        })

with open('teams.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(teams, jsonfile, ensure_ascii=False, indent=2)
