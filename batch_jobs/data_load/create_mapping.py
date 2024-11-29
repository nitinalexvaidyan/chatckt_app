from elasticsearch import Elasticsearch

def create():
    # Connect to Elasticsearch
    es = Elasticsearch("http://localhost:9200")

    # Define the index name
    index_name = "cricket_matches"

    # Define the mapping
    mapping = {
        "settings": {
            "index.mapping.total_fields.limit": 2000
        },
        "mappings": {
            "properties": {
                "info": {
                    "properties": {
                        "balls_per_over": {
                            "type": "long"
                        },
                        "city": {
                            "type": "keyword"
                        },
                        "dates": {
                            "type": "date"
                        },
                        "event": {
                            "properties": {
                                "match_number": {
                                    "type": "long"
                                },
                                "name": {
                                    "type": "keyword"
                                },
                                "stage": {
                                    "type": "keyword"
                                }
                            }
                        },
                        "gender": {
                            "type": "keyword"
                        },
                        "match_type": {
                            "type": "keyword"
                        },
                        "match_type_number": {
                            "type": "long"
                        },
                        "officials": {
                            "properties": {
                                "match_referees": {
                                    "type": "keyword"
                                },
                                "reserve_umpires": {
                                    "type": "keyword"
                                },
                                "tv_umpires": {
                                    "type": "keyword"
                                },
                                "umpires": {
                                    "type": "keyword"
                                }
                            }
                        },
                        "outcome": {
                            "properties": {
                                "by": {
                                    "properties": {
                                        "wickets": {
                                            "type": "long"
                                        }
                                    }
                                },
                                "winner": {
                                    "type": "keyword"
                                }
                            }
                        },
                        "overs": {
                            "type": "long"
                        },
                        "player_of_match": {
                            "type": "keyword"
                        },
                        "season": {
                            "type": "text"
                        },
                        "team_type": {
                            "type": "keyword"
                        },
                        "teams": {
                            "type": "keyword"
                        },
                        "toss": {
                            "properties": {
                                "decision": {
                                    "type": "keyword"
                                },
                                "winner": {
                                    "type": "keyword"
                                }
                            }
                        },
                        "venue": {
                            "type": "keyword"
                        }
                    }
                },
                "innings": {
                    "type": "nested",
                    "properties": {
                        "overs": {
                            "type": "nested",
                            "properties": {
                                "deliveries": {
                                    "type": "nested",
                                    "properties": {
                                        "batter": {
                                            "type": "keyword"
                                        },
                                        "bowler": {
                                            "type": "keyword"
                                        },
                                        "extras": {
                                            "properties": {
                                                "byes": {
                                                    "type": "long"
                                                },
                                                "legbyes": {
                                                    "type": "long"
                                                },
                                                "noballs": {
                                                    "type": "long"
                                                },
                                                "wides": {
                                                    "type": "long"
                                                }
                                            }
                                        },
                                        "non_striker": {
                                            "type": "keyword"
                                        },
                                        "runs": {
                                            "properties": {
                                                "batter": {
                                                    "type": "long"
                                                },
                                                "extras": {
                                                    "type": "long"
                                                },
                                                "total": {
                                                    "type": "long"
                                                }
                                            }
                                        },
                                        "wickets": {
                                            "properties": {
                                                "fielders": {
                                                    "properties": {
                                                        "name": {
                                                            "type": "keyword"
                                                        }
                                                    }
                                                },
                                                "kind": {
                                                    "type": "keyword"
                                                },
                                                "player_out": {
                                                    "type": "keyword"
                                                }
                                            }
                                        }
                                    }
                                },
                                "over": {
                                    "type": "long"
                                }
                            }
                        },
                        "powerplays": {
                            "properties": {
                                "from": {
                                    "type": "float"
                                },
                                "to": {
                                    "type": "float"
                                },
                                "type": {
                                    "type": "text",
                                    "fields": {
                                        "keyword": {
                                            "type": "keyword",
                                            "ignore_above": 256
                                        }
                                    }
                                }
                            }
                        },
                        "target": {
                            "properties": {
                                "overs": {
                                    "type": "long"
                                },
                                "runs": {
                                    "type": "long"
                                }
                            }
                        },
                        "team": {
                            "type": "text",
                            "fields": {
                                "keyword": {
                                    "type": "keyword",
                                    "ignore_above": 256
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    # Create the index with the mapping
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name, body=mapping)
        print(f"Index '{index_name}' created with predefined mapping.")
    else:
        print(f"Index '{index_name}' already exists.")


if __name__ == "__main__":
    create()