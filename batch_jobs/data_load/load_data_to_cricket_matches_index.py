import os
import json
import cricket_matches_mapping
from elasticsearch import Elasticsearch, helpers, exceptions

# Elasticsearch configuration
ES_HOST = "http://localhost:9200"  # Change to your ES endpoint if different
INDEX_NAME = "cricket_matches"  # Change to your preferred index name
DATA_FOLDER = "/home/ubuntu/chatckt_app/batch_jobs/test/all_matches_json_data"  # Change to the folder containing your JSON files

def to_lowercase(data):
    if isinstance(data, dict):
        return {key: to_lowercase(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [to_lowercase(item) for item in data]
    elif isinstance(data, str):
        return data.lower()
    return data

def load_data_into_index(folder_path):
    match_cnt = 0
    files_data = []
    es = Elasticsearch(ES_HOST)
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                match_cnt += 1
                print(f"Processing Match No: {match_cnt}")
                data = json.load(file)
                files_data.append(data)
                if match_cnt % 10 == 0:
                    process_and_load_data_to_es(es, files_data, match_cnt)
                    files_data = []
                    print(f"Matches {match_cnt-9} - {match_cnt} loaded into index")


    process_and_load_data_to_es(es, files_data, match_cnt)
    print(f"Matches till {match_cnt} loaded into index")
    print(f"Data load completed.\n Total matches loaded: {match_cnt}")


def process_and_load_data_to_es(es, matches_batch_data, match_cnt):
    try:
        batch_result = []
        match_count = (int(match_cnt/10) - 1) * 10
        for one_match in matches_batch_data:
            # ___ match info fields ___
            match_count += 1
            _match_info = one_match["info"]
            balls_per_over = _match_info.get("balls_per_over")
            city = _match_info.get("city")
            dates = _match_info["dates"]
            match_id = match_count
            match_name = _match_info.get("event", {}).get("name")
            match_stage = _match_info.get("event", {}).get("stage")
            gender = _match_info["gender"]
            match_type = _match_info["match_type"]
            match_type_number = _match_info.get("match_type_number")
            match_referees = _match_info.get("officials", {}).get("match_referees")
            reserve_umpires = _match_info.get("officials", {}).get("reserve_umpires")
            tv_umpires = _match_info.get("officials", {}).get("tv_umpires")
            umpires = _match_info.get("officials", {}).get("umpires")
            outcome = _match_info["outcome"].get("result")
            winner = _match_info["outcome"].get("winner")
            winner_wickets = _match_info["outcome"].get("by", {}).get("wickets")
            winner_runs = _match_info["outcome"].get("by", {}).get("runs")
            winner_method = _match_info["outcome"].get("method")
            total_overs = _match_info.get("overs")
            player_of_match = _match_info.get("player_of_match")
            season = _match_info.get("season")
            team_type = _match_info["team_type"]
            teams = _match_info["teams"]
            toss_winner =  _match_info["toss"]["winner"]
            toss_decision = _match_info["toss"]["decision"]
            venue = _match_info["venue"]

            #  ___ innings info ___
            innings_data = one_match["innings"]
            innings_cnt = 0
            for _innings in innings_data:
                innings_cnt += 1
                innings_number = innings_cnt
                batting_team = _innings["team"]
                bowling_team = [team for team in teams if team != batting_team][0]
                # forfeited case
                for _over in _innings.get("overs", []):
                    over_no = _over["over"] + 1
                    ball_cnt = 0
                    for _ball in _over["deliveries"]:
                        ball_cnt += 1
                        ball_no = ball_cnt
                        batter = _ball["batter"]
                        bowler = _ball["bowler"]
                        non_striker = _ball["non_striker"]

                        runs_batter = _ball["runs"]["batter"]
                        runs_extras = _ball["runs"]["extras"]
                        runs_total = _ball["runs"]["total"]

                        byes =  _ball.get("extras", {}).get("byes")
                        legbyes = _ball.get("extras", {}).get("legbyes")
                        noballs = _ball.get("extras", {}).get("noballs")
                        wides = _ball.get("extras", {}).get("wides")
                        penalty = _ball.get("extras", {}).get("penality")

                        valid_ball = True
                        if _ball.get("extras"):
                            valid_ball = False

                        wicket_fielders = []
                        wicket_kind = None
                        player_out = None
                        wickets = _ball.get("wickets")
                        if wickets:
                            wk_fielders = wickets[0].get("fielders", [])
                            for _fld in wk_fielders:
                                wicket_fielders.append(_fld.get("name") or ( "substitute" if _fld.get("substitute") else None))
                            wicket_kind = wickets[0].get("kind")
                            player_out = wickets[0].get("player_out")

                        review_by = _ball.get("review", {}).get("by")
                        review_umpire = _ball.get("review", {}).get("umpire")
                        review_batter = _ball.get("review", {}).get("batter")
                        review_decision = _ball.get("review", {}).get("decision")
                        review_type = _ball.get("review", {}).get("type")
                        review_umpire_call = _ball.get("review", {}).get("umpires_call")

                        powerplay_over = False
                        powerplay_type = None
                        for _pwr_ply in _innings.get("powerplays", []):
                            pwr_ply_from = str(_pwr_ply["from"]).split(".")[0]
                            pwr_ply_to = str(_pwr_ply["to"]).split(".")[0]
                            pwr_ply_type = _pwr_ply["type"]
                            if int(pwr_ply_from) <= over_no-1 <= int(pwr_ply_to):
                                powerplay_over = True
                                powerplay_type = pwr_ply_type
                        target_overs = None
                        target_runs = None
                        if _innings.get("target"):
                            target_overs = _innings["target"]["overs"]
                            target_runs = _innings["target"]["runs"]

                        innings_declared = _innings.get("declared")
                        followon = None
                        eliminator = None
                        bowl_out = None

                        one_doc = {
                            "dates": dates,
                            "match_id": match_id,
                            "gender": gender,
                            "match_type": match_type,
                            "team_type": team_type,
                            "teams": teams,
                            "toss_winner": toss_winner,
                            "toss_decision": toss_decision,
                            "venue": venue,
                            "innings_number": innings_number,
                            "batting_team": batting_team,
                            "bowling_team": bowling_team,
                            "over_no": over_no,
                            "ball_no": ball_no,
                            "batter": batter,
                            "bowler": bowler,
                            "non_striker": non_striker,
                            "runs_batter": runs_batter,
                            "runs_extras": runs_extras,
                            "runs_total": runs_total,
                            "valid_ball": valid_ball
                        }

                        if match_name:
                            one_doc["match_name"] = match_name
                        if balls_per_over:
                            one_doc["balls_per_over"] = balls_per_over
                        if city:
                            one_doc["city"] = city
                        if match_stage:
                            one_doc["match_stage"] = match_stage
                        if match_type_number:
                            one_doc["match_type_number"] = match_type_number
                        if match_referees:
                            one_doc["match_referees"] = match_referees
                        if reserve_umpires:
                            one_doc["reserve_umpires"] = reserve_umpires
                        if tv_umpires:
                            one_doc["tv_umpires"] = tv_umpires
                        if umpires:
                            one_doc["umpires"] = umpires
                        if outcome:
                            one_doc["outcome"] = outcome
                        if winner:
                            one_doc["winner"] = winner
                        if winner_wickets:
                            one_doc["winner_wickets"] = winner_wickets
                        if winner_runs:
                            one_doc["winner_runs"] = winner_runs
                        if winner_method:
                            one_doc["winner_method"] = winner_method
                        if total_overs:
                            one_doc["total_overs"] = total_overs
                        if player_of_match:
                            one_doc["player_of_match"] = player_of_match
                        if season:
                            one_doc["season"] = season
                        if byes:
                            one_doc["byes"] = byes
                        if legbyes:
                            one_doc["legbyes"] = legbyes
                        if noballs:
                            one_doc["noballs"] = noballs
                        if wides:
                            one_doc["wides"] = wides
                        if penalty:
                            one_doc["penalty"] = penalty
                        if wicket_fielders:
                            one_doc["wicket_fielders"] = wicket_fielders
                        if wicket_kind:
                            one_doc["wicket_kind"] = wicket_kind
                        if player_out:
                            one_doc["player_out"] = player_out
                        if review_by:
                            one_doc["review_by"] = review_by
                        if review_umpire:
                            one_doc["review_umpire"] = review_umpire
                        if review_batter:
                            one_doc["review_batter"] = review_batter
                        if review_decision:
                            one_doc["review_decision"] = review_decision
                        if review_type:
                            one_doc["review_type"] = review_type
                        if review_umpire_call:
                            one_doc["review_umpire_call"] = review_umpire_call
                        if powerplay_over:
                            one_doc["powerplay_over"] = powerplay_over
                        if powerplay_type:
                            one_doc["powerplay_type"] = powerplay_type
                        if target_overs:
                            one_doc["target_overs"] = target_overs
                        if target_runs:
                            one_doc["target_runs"] = target_runs
                        if innings_declared:
                            one_doc["innings_declared"] = innings_declared
                        if followon:
                            one_doc["followon"] = followon
                        if eliminator:
                            one_doc["eliminator"] = eliminator
                        if bowl_out:
                            one_doc["bowl_out"] = bowl_out

                        lowered_doc = to_lowercase(one_doc)
                        # print(f"One Ball Doc:{lowered_doc}")
                        batch_result.append(lowered_doc)
        actions = []
        for each_doc in batch_result:
            # es.index(index=INDEX_NAME, document=each_doc)
            actions.append({"_index": INDEX_NAME, "_source": each_doc})
        helpers.bulk(es, actions)

    except exceptions.RequestError as e:
        print("Error: >>> ", e.info)


def main():
    cricket_matches_mapping.create()
    load_data_into_index(DATA_FOLDER)


if __name__ == "__main__":
    main()
    print("Data load complete. Hurray !!! !!! ... ...")
