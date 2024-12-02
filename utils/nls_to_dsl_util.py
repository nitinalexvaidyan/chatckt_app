import openai
import os
from openai import OpenAI
import langchain.chat_models 
from langchain.chat_models import ChatOpenAI
import json
from langchain.prompts import ChatPromptTemplate
import json
import re



llm_model='gpt-4o-mini'
api_key=os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)
chat = ChatOpenAI(temperature=0.0, model=llm_model)


def get_table_info_text():
    table_info="""Table Description:

        This table contains ball-by-ball details of cricket matches, derived from JSON files downloaded from Cricsheet.com. The data has been imported into an Elasticsearch database for querying and analysis.
        Key Fields and Descriptions:
        Match-Level Information:

            dates: Dates on which the match was played. Usually a single date, but Test matches may span multiple dates.
            match_id: Unique identifier for each match.
            gender: Specifies whether the match was played by which gender [male, female].
            match_type: Type of match, possible values are [t20, mdm, odi, test, odm, it20].
            team_type: Type of teams involved, possible values are [international, club]
            teams: Names of the teams participating in the match.
            toss_winner: Team that won the toss.
            toss_decision: Toss winner's decision—whether to bat or bowl first.
            venue: Location where the match was played.
            city: City in which the venue is located.
            match_name: Name or title of the match.
            season: Season (year) in which the match was played, values are like 2023, 2023/24, 2022, 2022/23 etc
            match_referees: Names of the match referees.
            match_stage: stage of the match in tournament possible values are[final, semi final, 3rd place play-off, qualifier 1 qualifier 2, eliminator, knockout]
            reserve_umpires: Names of reserve umpires.
            tv_umpires: Names of TV umpires.
            umpires: Names of on-field umpires.
            winner: The team that won the match.
            winner_method: how the winner was decided possible value [d/l]
            winner_wickets: Number of wickets remaining when the winner achieved victory.
            winner_runs: Number of runs by which the winner won.
            total_overs: Total overs bowled in the match.
            player_of_match: Player awarded the "Player of the Match."
            balls_per_over: Number of balls in an over (e.g., 6 for standard cricket).
            target_runs: Target runs set for the chasing team.
            target_overs: Target overs set for the chasing team (if applicable).
            outcome: possible values [tie, draw, no result], if there is no winner
            venue: venue where match is played

        Innings and Ball-Level Information:

            innings_number: Number of the innings (1, 2, etc.).
            batting_team: The team batting in the current innings.
            bowling_team: The team bowling in the current innings.
            over_no: Over number within the innings.
            ball_no: Ball number within the over.
            batter: Name of the batsman for the ball.
            bowler: Name of the bowler for the ball.
            non_striker: Name of the non-striker for the ball.
            valid_ball: Boolean indicating if the ball was valid.
            runs_batter: Runs scored by the batsman on the given ball (not the total match score).
            runs_extras: Extra runs on the given ball (e.g., wides, no-balls).
            runs_total: Total runs on the given ball, including extras.
            byes: bye runs for the ball
            legbyes: legbye runs for the ball
            powerplay_over: true or false
            powerplay_type: possible values [mandatory]
            review_batter: batter who is batting for a review
            review_by: review is called by which team
            review_decision: possible values [struck down, upheld]
            review_type:[wicket]
            wicket_fielders: fielder who helped the wicket either by catch, run out etc
            wicket_kind: possible values [caught,run out,bowled,lbw,caught and bowled,stumped,retired hurt]

        Notes for Analysis:
        Summations:

            Use cardinality aggregation on ball-level data to derive match-level insights, including:
                Total Runs: Sum up all runs scored (runs_total).
                Wickets: Count the total dismissals in the match.
                Overs: Calculate the total overs bowled in the match based on over_no and balls_per_over.
                Example: To check if a player scored a century in a match, aggregate runs_batter at the match_id level.
                Number of Matches: Compute the count of distinct matches.

        Search Suggestions:

            Use wildcard searches for text fields like player names, teams, or venues to manage partial matches and variations.
            Simplify specific names to widely recognized short forms for wildcard searches.
                Examples:
                    Use *kohli* instead of virat kohli.
                    Use *dhoni* instead of MS Dhoni.
                    Use *tendulkar* instead of sachin tendulkar
                    Use *rohit sharma* for rohit sharma

        Note for Output:

            Provide step-by-step instructions to construct the query.
            For each step, ensure that the provided instructions are followed without any violations.
            Conclude with a single, complete dsl_query.

        This structure ensures efficient querying and aggregation for cricket analytics."""
    return table_info


def get_template_string():
    template_string = """Generate a DSL query for an Elasticsearch database based on the query enclosed within triple backticks, using the provided table information: {table_info}. 
                    Query: ```{query}```. 
                    For instance, if the query is "how many runs did captain cool score on 2023" the response should only include the corresponding JSON structure, formatted as shown in the example below:
                    ``{response1}``
                    """
    return template_string

def get_sample_response():
    response={
            "dsl_query": {
                "bool": {
                "must": [
                    {
                    "wildcard": {
                        "batter": "*dhoni*"
                    }
                    },
                    {
                    "range": {
                        "dates": {
                        "gte": "2023-01-01",
                        "lt": "2024-01-01"
                        }
                    }
                    }
                ],
                "aggs": {
                    "total_runs": {
                    "sum": {
                        "field": "runs_batter"
                    }
                    }
                }
                }
            }
            }
    return response

def extract_json_dict(content):
    response_dict = {"dsl_query":{}}
    match=re.search(r"```json(.*)```", content, re.DOTALL)
    if match:
        json_str = match.group(1).strip()
        try:
            parsed_dict = json.loads(json_str)
            if "dsl_query" in parsed_dict:
                response_dict["dsl_query"]= parsed_dict["dsl_query"]
                response_dict["status"]="success"
            else:
                response_dict["message"]="structure issue"
                response_dict["status"]="failed"
                response_dict["actual_response"]=json_str
        except json.JSONDecodeError:
            print("Error decoding JSON:", json_str)
            response_dict["status"]="failed"
            response_dict["message"]="error decoding"
            response_dict["actual_response"]=json_str
    else:
        response_dict["message"]="error decoding"
        response_dict["status"]="failed"
        response_dict["actual_response"]=json_str
    return response_dict

def get_rephrased_query(query):
    prompt_template = ChatPromptTemplate.from_template("Rephrase the query by replacing any nicknames with the player's actual name in the context of cricket. If no nicknames are present, return the query as it is. - query - {query}")
    question=prompt_template.format_messages(
                    query=format(query),
                    )
    query_response = chat(question)
    content = query_response.content
    if len(query.split(' '))+5 <  len(content.split(' ')):
        content = query
    else:
        if len(query.split(' ')) >  len(content.split(' '))+2:
            content = query
    return content

def get_dsl_query(query):
    query= get_rephrased_query(query).lower()
    template_string = get_template_string()
    table_info=get_table_info_text()
    response_sample = get_sample_response()
    prompt_template = ChatPromptTemplate.from_template(template_string)
    question = prompt_template.format_messages(
                        query=query,
                        table_info=table_info,
                        response1=response_sample)
    query_response = chat(question)
    resp_dict =extract_json_dict(query_response.content.lower())
    return resp_dict


def get_final_response(es_response,query):
    try:
        prompt_template = ChatPromptTemplate.from_template("""For the user's query, we attempted to retrieve relevant results from cricket sheet data.

                The query is query - {query}, and the corresponding response data is provided as:

                {es_response}  

            Instructions:

                For Non-Cricket small talk:
                    If the query is conversational, such as "Hi," "How are you?" or "What's the weather today?" respond naturally and appropriately without referencing the cricket data.

                For Cricket-Related Queries:
                    Analyze the response data provided within the triple backticks ({es_response}) to address the query.
                    Focus exclusively on the facts derived from the data. Do not mention technical terms like Elasticsearch, JSON, dictionary, etc.

                If No Relevant Information Is Found and is out of cricket context:
                    If the response data does not contain the information needed to answer the query, reply with `I don't know.`""")
        question = prompt_template.format_messages(
                            query=query,
                            es_response=es_response)
        query_response = chat(question)
        resp = query_response.content
    except:
        resp = "Not able to answer due to error"
    return resp




