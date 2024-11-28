from elasticsearch import Elasticsearch

def create():
    # Connect to Elasticsearch
    es = Elasticsearch("http://localhost:9200")

    # Define the index name
    index_name = "cricket_data"

    # Define the mapping
    mapping = {
      "cricket_matches" : {
        "mappings" : {
          "properties" : {
            "info" : {
              "properties" : {
                "balls_per_over" : {
                  "type" : "long"
                },
                "city" : {
                  "type" : "text",
                  "fields" : {
                    "keyword" : {
                      "type" : "keyword",
                      "ignore_above" : 256
                    }
                  }
                },
                "dates" : {
                  "type" : "date"
                },
                "event" : {
                  "properties" : {
                    "match_number" : {
                      "type" : "long"
                    },
                    "name" : {
                      "type" : "text",
                      "fields" : {
                        "keyword" : {
                          "type" : "keyword",
                          "ignore_above" : 256
                        }
                      }
                    },
                    "stage" : {
                      "type" : "text",
                      "fields" : {
                        "keyword" : {
                          "type" : "keyword",
                          "ignore_above" : 256
                        }
                      }
                    }
                  }
                },
                "gender" : {
                  "type" : "text",
                  "fields" : {
                    "keyword" : {
                      "type" : "keyword",
                      "ignore_above" : 256
                    }
                  }
                },
                "match_type" : {
                  "type" : "text",
                  "fields" : {
                    "keyword" : {
                      "type" : "keyword",
                      "ignore_above" : 256
                    }
                  }
                },
                "match_type_number" : {
                  "type" : "long"
                },
                "officials" : {
                  "properties" : {
                    "match_referees" : {
                      "type" : "text",
                      "fields" : {
                        "keyword" : {
                          "type" : "keyword",
                          "ignore_above" : 256
                        }
                      }
                    },
                    "reserve_umpires" : {
                      "type" : "text",
                      "fields" : {
                        "keyword" : {
                          "type" : "keyword",
                          "ignore_above" : 256
                        }
                      }
                    },
                    "tv_umpires" : {
                      "type" : "text",
                      "fields" : {
                        "keyword" : {
                          "type" : "keyword",
                          "ignore_above" : 256
                        }
                      }
                    },
                    "umpires" : {
                      "type" : "text",
                      "fields" : {
                        "keyword" : {
                          "type" : "keyword",
                          "ignore_above" : 256
                        }
                      }
                    }
                  }
                },
                "outcome" : {
                  "properties" : {
                    "by" : {
                      "properties" : {
                        "wickets" : {
                          "type" : "long"
                        }
                      }
                    },
                    "winner" : {
                      "type" : "text",
                      "fields" : {
                        "keyword" : {
                          "type" : "keyword",
                          "ignore_above" : 256
                        }
                      }
                    }
                  }
                },
                "overs" : {
                  "type" : "long"
                },
                "player_of_match" : {
                  "type" : "text",
                  "fields" : {
                    "keyword" : {
                      "type" : "keyword",
                      "ignore_above" : 256
                    }
                  }
                },
                "players" : {
                  "properties" : {
                    "Gloucestershire" : {
                      "type" : "text",
                      "fields" : {
                        "keyword" : {
                          "type" : "keyword",
                          "ignore_above" : 256
                        }
                      }
                    },
                    "India" : {
                      "type" : "text",
                      "fields" : {
                        "keyword" : {
                          "type" : "keyword",
                          "ignore_above" : 256
                        }
                      }
                    },
                    "Leinster Lightning" : {
                      "type" : "text",
                      "fields" : {
                        "keyword" : {
                          "type" : "keyword",
                          "ignore_above" : 256
                        }
                      }
                    },
                    "Munster Reds" : {
                      "type" : "text",
                      "fields" : {
                        "keyword" : {
                          "type" : "keyword",
                          "ignore_above" : 256
                        }
                      }
                    },
                    "Northamptonshire" : {
                      "type" : "text",
                      "fields" : {
                        "keyword" : {
                          "type" : "keyword",
                          "ignore_above" : 256
                        }
                      }
                    },
                    "Sri Lanka" : {
                      "type" : "text",
                      "fields" : {
                        "keyword" : {
                          "type" : "keyword",
                          "ignore_above" : 256
                        }
                      }
                    }
                  }
                },
                "registry" : {
                  "properties" : {
                    "people" : {
                      "properties" : {
                        "A Sidhu" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "AG Wharf" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "AM Rossington" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "AR Frost" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "B Kruger" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "BAC Howell" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "BAW Mendis" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "BC Broad" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "BF Calitz" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "BR Doctrove" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "BW Sanderson" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "C De Freitas" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "CDJ Dent" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "CJB McCullough" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "CK Kapugedera" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "D Lues" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "DA Cosker" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "DA Payne" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "DC Delany" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "DPMD Jayawardene" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "EAR de Silva" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "G Gambhir" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "G Hoey" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "G McCrea" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "GG White" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "GL van Buuren" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "Harbhajan Singh" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "IA Cockbain" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "IK Pathan" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "J Manley" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "J Neill" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "J Shaw" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "JJ Cobb" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "JMR Taylor" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "James Bracey" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "Jonathan Kennedy" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "KC Sangakkara" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "KMDN Kulasekara" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "L McCarthy" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "LA Procter" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "LPC Silva" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "M Frost" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "M Hawthorne" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "M Muralitharan" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "MG Silva" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "MM Patel" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "MS Dhoni" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "MSK Nandiweera" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "Miles Hammond" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "N Stapleton" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "ND Laegsgaard" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "NL Buck" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "O Riley" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "OG Metcalfe" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "PP Ojha" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "PR Stirling" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "R Black" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "RE Levi" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "RF Higgins" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "RG Sharma" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "RI Keogh" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "RJ Warren" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "S Lynch" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "S Modgil" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "SA Zaib" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "SJ Harbinson" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "SK Raina" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "ST Jayasuriya" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "T Thushara" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "TAI Taylor" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "TH Tector" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "TM Dilshan" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "TMJ Smith" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "V Kohli" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "WPUJC Vaas" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "Yuvraj Singh" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "Z Khan" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "Zubair Khan" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        }
                      }
                    }
                  }
                },
                "season" : {
                  "type" : "text"
                },
                "team_type" : {
                  "type" : "text",
                  "fields" : {
                    "keyword" : {
                      "type" : "keyword",
                      "ignore_above" : 256
                    }
                  }
                },
                "teams" : {
                  "type" : "text",
                  "fields" : {
                    "keyword" : {
                      "type" : "keyword",
                      "ignore_above" : 256
                    }
                  }
                },
                "toss" : {
                  "properties" : {
                    "decision" : {
                      "type" : "text",
                      "fields" : {
                        "keyword" : {
                          "type" : "keyword",
                          "ignore_above" : 256
                        }
                      }
                    },
                    "winner" : {
                      "type" : "text",
                      "fields" : {
                        "keyword" : {
                          "type" : "keyword",
                          "ignore_above" : 256
                        }
                      }
                    }
                  }
                },
                "venue" : {
                  "type" : "text",
                  "fields" : {
                    "keyword" : {
                      "type" : "keyword",
                      "ignore_above" : 256
                    }
                  }
                }
              }
            },
            "innings" : {
              "properties" : {
                "overs" : {
                  "properties" : {
                    "deliveries" : {
                      "properties" : {
                        "batter" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "bowler" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "extras" : {
                          "properties" : {
                            "byes" : {
                              "type" : "long"
                            },
                            "legbyes" : {
                              "type" : "long"
                            },
                            "noballs" : {
                              "type" : "long"
                            },
                            "wides" : {
                              "type" : "long"
                            }
                          }
                        },
                        "non_striker" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        },
                        "runs" : {
                          "properties" : {
                            "batter" : {
                              "type" : "long"
                            },
                            "extras" : {
                              "type" : "long"
                            },
                            "total" : {
                              "type" : "long"
                            }
                          }
                        },
                        "wickets" : {
                          "properties" : {
                            "fielders" : {
                              "properties" : {
                                "name" : {
                                  "type" : "text",
                                  "fields" : {
                                    "keyword" : {
                                      "type" : "keyword",
                                      "ignore_above" : 256
                                    }
                                  }
                                }
                              }
                            },
                            "kind" : {
                              "type" : "text",
                              "fields" : {
                                "keyword" : {
                                  "type" : "keyword",
                                  "ignore_above" : 256
                                }
                              }
                            },
                            "player_out" : {
                              "type" : "text",
                              "fields" : {
                                "keyword" : {
                                  "type" : "keyword",
                                  "ignore_above" : 256
                                }
                              }
                            }
                          }
                        }
                      }
                    },
                    "over" : {
                      "type" : "long"
                    }
                  }
                },
                "powerplays" : {
                  "properties" : {
                    "from" : {
                      "type" : "float"
                    },
                    "to" : {
                      "type" : "float"
                    },
                    "type" : {
                      "type" : "text",
                      "fields" : {
                        "keyword" : {
                          "type" : "keyword",
                          "ignore_above" : 256
                        }
                      }
                    }
                  }
                },
                "target" : {
                  "properties" : {
                    "overs" : {
                      "type" : "long"
                    },
                    "runs" : {
                      "type" : "long"
                    }
                  }
                },
                "team" : {
                  "type" : "text",
                  "fields" : {
                    "keyword" : {
                      "type" : "keyword",
                      "ignore_above" : 256
                    }
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