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
                            "type": "text",
                            "fields": {
                                "keyword": {
                                    "type": "keyword",
                                    "ignore_above": 256
                                }
                            }
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
                                    "type": "text",
                                    "fields": {
                                        "keyword": {
                                            "type": "keyword",
                                            "ignore_above": 256
                                        }
                                    }
                                },
                                "stage": {
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
                        "gender": {
                            "type": "text",
                            "fields": {
                                "keyword": {
                                    "type": "keyword",
                                    "ignore_above": 256
                                }
                            }
                        },
                        "match_type": {
                            "type": "text",
                            "fields": {
                                "keyword": {
                                    "type": "keyword",
                                    "ignore_above": 256
                                }
                            }
                        },
                        "match_type_number": {
                            "type": "long"
                        },
                        "officials": {
                            "properties": {
                                "match_referees": {
                                    "type": "text",
                                    "fields": {
                                        "keyword": {
                                            "type": "keyword",
                                            "ignore_above": 256
                                        }
                                    }
                                },
                                "reserve_umpires": {
                                    "type": "text",
                                    "fields": {
                                        "keyword": {
                                            "type": "keyword",
                                            "ignore_above": 256
                                        }
                                    }
                                },
                                "tv_umpires": {
                                    "type": "text",
                                    "fields": {
                                        "keyword": {
                                            "type": "keyword",
                                            "ignore_above": 256
                                        }
                                    }
                                },
                                "umpires": {
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
                        "overs": {
                            "type": "long"
                        },
                        "player_of_match": {
                            "type": "text",
                            "fields": {
                                "keyword": {
                                    "type": "keyword",
                                    "ignore_above": 256
                                }
                            }
                        },
                        "season": {
                            "type": "text"
                        },
                        "team_type": {
                            "type": "text",
                            "fields": {
                                "keyword": {
                                    "type": "keyword",
                                    "ignore_above": 256
                                }
                            }
                        },
                        "teams": {
                            "type": "text",
                            "fields": {
                                "keyword": {
                                    "type": "keyword",
                                    "ignore_above": 256
                                }
                            }
                        },
                        "toss": {
                            "properties": {
                                "decision": {
                                    "type": "text",
                                    "fields": {
                                        "keyword": {
                                            "type": "keyword",
                                            "ignore_above": 256
                                        }
                                    }
                                },
                                "winner": {
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
                        "venue": {
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
                "innings": {
                    "properties": {
                        "overs": {
                            "properties": {
                                "deliveries": {
                                    "properties": {
                                        "batter": {
                                            "type": "text",
                                            "fields": {
                                                "keyword": {
                                                    "type": "keyword",
                                                    "ignore_above": 256
                                                }
                                            }
                                        },
                                        "bowler": {
                                            "type": "text",
                                            "fields": {
                                                "keyword": {
                                                    "type": "keyword",
                                                    "ignore_above": 256
                                                }
                                            }
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
                                            "type": "text",
                                            "fields": {
                                                "keyword": {
                                                    "type": "keyword",
                                                    "ignore_above": 256
                                                }
                                            }
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
                                                "kind": {
                                                    "type": "text",
                                                    "fields": {
                                                        "keyword": {
                                                            "type": "keyword",
                                                            "ignore_above": 256
                                                        }
                                                    }
                                                },
                                                "player_out": {
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