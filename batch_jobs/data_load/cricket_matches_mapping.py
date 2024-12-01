from elasticsearch import Elasticsearch

def create():
    es_host = Elasticsearch("http://localhost:9200")
    index_name = "cricket_matches"
    mapping = {
        "mappings": {
            "properties": {
                "balls_per_over": {"type": "integer"},
                "city": {"type": "keyword"},
                "dates": {"type": "date", "format": "yyyy-MM-dd"},
                "match_id": {"type": "keyword"},
                "match_name": {"type": "keyword"},
                "match_stage": {"type": "keyword"},
                "gender": {"type": "keyword"},
                "match_type": {"type": "keyword"},
                "match_type_number": {"type": "integer"},
                "match_referees": {"type": "keyword"},
                "reserve_umpires": {"type": "keyword"},
                "tv_umpires": {"type": "keyword"},
                "umpires": {"type": "keyword"},
                "outcome": {"type": "keyword"},
                "winner": {"type": "keyword"},
                "winner_wickets": {"type": "integer"},
                "winner_runs": {"type": "integer"},
                "winner_method": {"type": "keyword"},
                "total_overs": {"type": "integer"},
                "player_of_match": {"type": "keyword"},
                "season": {"type": "keyword"},
                "team_type": {"type": "keyword"},
                "teams": {"type": "keyword"},
                "toss_winner": {"type": "keyword"},
                "toss_decision": {"type": "keyword"},
                "venue": {"type": "keyword"},
                "innings_number": {"type": "integer"},
                "batting_team": {"type": "keyword"},
                "bowling_team": {"type": "keyword"},
                "over_no": {"type": "integer"},
                "ball_no": {"type": "integer"},
                "valid_ball": {"type": "boolean"},
                "batter": {"type": "keyword"},
                "bowler": {"type": "keyword"},
                "byes": {"type": "integer"},
                "legbyes": {"type": "integer"},
                "noballs": {"type": "integer"},
                "wides": {"type": "integer"},
                "penalty": {"type": "integer"},
                "non_striker": {"type": "keyword"},
                "runs_batter": {"type": "integer"},
                "runs_extras": {"type": "integer"},
                "runs_total": {"type": "integer"},
                "wicket_fielders": {"type": "keyword"},
                "wicket_kind": {"type": "keyword"},
                "player_out": {"type": "keyword"},
                "powerplay_over": {"type": "boolean"},
                "powerplay_type": {"type": "keyword"},
                "target_overs": {"type": "integer"},
                "target_runs": {"type": "integer"},
                "followon": {"type": "boolean"},
                "innings_declared": {"type": "boolean"},
                "eliminator": {"type": "keyword"},
                "bowl_out": {"type": "keyword"},
                "review_by": {"type": "keyword"},
                "review_umpire": {"type": "keyword"},
                "review_batter": {"type": "keyword"},
                "review_decision": {"type": "keyword"},
                "review_type": {"type": "keyword"},
                "review_umpire_call": {"type": "boolean"}
            }
        }
    }

    if not es_host.indices.exists(index=index_name):
        es_host.indices.create(index=index_name, body=mapping)
        print(f"Index '{index_name}' created with predefined mapping.")
    else:
        print(f"Index '{index_name}' already exists.")


if __name__ == "__main__":
    create()