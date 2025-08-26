select team_abbr,team_name,team_division,team_logo_espn
from teams
where team_abbr not in ('LAR','OAK','STL','SD')
