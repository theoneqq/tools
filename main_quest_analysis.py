import sys
import re
from itertools import islice

t1_file, t2_file = sys.argv[1], sys.argv[2]

t1_player_datas = {}
t2_player_ids = set()

with open(t1_file, 'rt') as f:
    for line in islice(f, 1, None):
        items = re.split('\t| ', line)
        player_id, event_name = int(items[0]), int(items[1])
        t1_player_datas[player_id] =  { 'player_id' : player_id, 'event_name' : event_name }

with open(t2_file, 'rt') as f:
    for line in f:
        t2_player_ids.add(int(line))

total_player_num = len(t1_player_datas)
t1_main_quests, t2_main_quests = {}, {}

for key in t1_player_datas:
    data = t1_player_datas[key]
    player_id, main_quest_id = data['player_id'], data['event_name']
    t1_main_quests[main_quest_id] = t1_main_quests.get(main_quest_id, 0) + 1
    if player_id in t2_player_ids:
        t2_main_quests[main_quest_id] = t2_main_quests.get(main_quest_id, 0) + 1


results = []
for main_quest_id in [ key for key in sorted(t1_main_quests.keys()) ]:
    t1_player_num = t1_main_quests[main_quest_id]
    t2_player_num = t2_main_quests.get(main_quest_id, 0)
    t1_ratio = t1_player_num / total_player_num
    t2_ratio = t2_player_num / total_player_num
    results.append([main_quest_id, t1_player_num, t2_player_num, t1_ratio, t2_ratio ])

with open('out.txt', 'wt') as f:
    f.write('id\tt1\tt2\tt1_ratio\tt2_ratio\n')
    for result in results:
        f.write('\t'.join([ str(s) for s in result ]))
        f.write('\n')
