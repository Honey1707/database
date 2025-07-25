schema = {
    "movie": {
        "columns": {
            "available_globally": "NUMERIC",
            "id": "INTEGER",
            "runtime": "INTEGER",
            "locale": "TEXT",
            "original_title": "TEXT",
            "title": "TEXT",
            "release_date": "TEXT",
            "created_date": "TEXT",
            "modified_date": "TEXT",
        },
        "sample": [
            {
                "available_globally": 1,
                "id": 1,
                "runtime": 110,
                "locale": None,
                "original_title": None,
                "title": "Damsel",
                "release_date": "2024-03-08 13:30:00",
                "created_date": "2024-01-01 05:30:00",
                "modified_date": "2024-01-01 05:30:00",
            },
            {
                "available_globally": 1,
                "id": 2,
                "runtime": 107,
                "locale": None,
                "original_title": None,
                "title": "Lift",
                "release_date": "2024-01-12 13:30:00",
                "created_date": "2024-01-01 05:30:00",
                "modified_date": "2024-01-01 05:30:00",
            },
            {
                "available_globally": 1,
                "id": 3,
                "runtime": 146,
                "locale": None,
                "original_title": "La sociedad de la nieve",
                "title": "Society of the Snow",
                "release_date": "2024-01-04 13:30:00",
                "created_date": "2024-01-01 05:30:00",
                "modified_date": "2024-01-01 05:30:00",
            },
            {
                "available_globally": 1,
                "id": 4,
                "runtime": 104,
                "locale": None,
                "original_title": "Sous la Seine",
                "title": "Under Paris",
                "release_date": "2024-06-05 12:30:00",
                "created_date": "2024-01-01 05:30:00",
                "modified_date": "2024-01-01 05:30:00",
            },
            {
                "available_globally": 0,
                "id": 5,
                "runtime": 92,
                "locale": None,
                "original_title": None,
                "title": "The Super Mario Bros. Movie",
                "release_date": None,
                "created_date": "2024-01-01 05:30:00",
                "modified_date": "2024-01-01 05:30:00",
            },
        ],
        "description": "This table contains records of movies, storing key details such as unique identifiers, original and localized titles, runtime, release and localization information, global availability, and audit dates. It supports the management and cataloging of movies for content distribution and discovery across different regions.",
    },
    "season": {
        "columns": {
            "season_number": "INTEGER",
            "id": "INTEGER",
            "runtime": "INTEGER",
            "tv_show_id": "INTEGER",
            "original_title": "TEXT",
            "title": "TEXT",
            "release_date": "TEXT",
            "created_date": "TEXT",
            "modified_date": "TEXT",
        },
        "sample": [
            {
                "season_number": 1,
                "id": 9,
                "runtime": 394,
                "tv_show_id": 9,
                "original_title": "Berlín: Season 1",
                "title": "Berlin: Season 1",
                "release_date": "2023-12-29 13:30:00",
                "created_date": "2024-01-01 05:30:00",
                "modified_date": "2024-01-01 05:30:00",
            },
            {
                "season_number": 1,
                "id": 19,
                "runtime": 363,
                "tv_show_id": 17,
                "original_title": "Ni una más: Temporada 1",
                "title": "Raising Voices: Season 1",
                "release_date": "2024-05-31 12:30:00",
                "created_date": "2024-01-01 05:30:00",
                "modified_date": "2024-01-01 05:30:00",
            },
            {
                "season_number": 1,
                "id": 53,
                "runtime": 427,
                "tv_show_id": 44,
                "original_title": "忍びの家 House of Ninjas: シーズン1",
                "title": "House of Ninjas: Season 1",
                "release_date": "2024-02-15 13:30:00",
                "created_date": "2024-01-01 05:30:00",
                "modified_date": "2024-01-01 05:30:00",
            },
            {
                "season_number": 1,
                "id": 64,
                "runtime": 439,
                "tv_show_id": 52,
                "original_title": "हीरामंडी: द डायमंड बाज़ार: सीज़न 1",
                "title": "Heeramandi: The Diamond Bazaar: Season 1",
                "release_date": "2024-05-01 12:30:00",
                "created_date": "2024-01-01 05:30:00",
                "modified_date": "2024-01-01 05:30:00",
            },
            {
                "season_number": 1,
                "id": 65,
                "runtime": 352,
                "tv_show_id": 53,
                "original_title": "Kimler Geldi Kimler Geçti: 1. Sezon",
                "title": "Thank You, Next: Season 1",
                "release_date": "2024-05-09 12:30:00",
                "created_date": "2024-01-01 05:30:00",
                "modified_date": "2024-01-01 05:30:00",
            },
        ],
        "description": "This table stores information about individual television show seasons, including their season numbers, associated show identifiers, original and localized titles, runtime durations, and key release and modification dates. It supports content management and cataloging by linking each season to its parent TV show and tracking relevant metadata for media distribution platforms.",
    },
    "tv_show": {
        "columns": {
            "available_globally": "NUMERIC",
            "release_date": "NUMERIC",
            "id": "INTEGER",
            "locale": "TEXT",
            "original_title": "TEXT",
            "title": "TEXT",
            "created_date": "TEXT",
            "modified_date": "TEXT",
        },
        "sample": [
            {
                "available_globally": 1,
                "release_date": None,
                "id": 1,
                "locale": "en",
                "original_title": None,
                "title": "Fool Me Once",
                "created_date": "2024-01-01 05:30:00",
                "modified_date": "2024-01-01 05:30:00",
            },
            {
                "available_globally": 1,
                "release_date": None,
                "id": 2,
                "locale": "en",
                "original_title": None,
                "title": "Bridgerton",
                "created_date": "2024-01-01 05:30:00",
                "modified_date": "2024-01-01 05:30:00",
            },
            {
                "available_globally": 1,
                "release_date": None,
                "id": 3,
                "locale": "en",
                "original_title": None,
                "title": "Baby Reindeer",
                "created_date": "2024-01-01 05:30:00",
                "modified_date": "2024-01-01 05:30:00",
            },
            {
                "available_globally": 1,
                "release_date": None,
                "id": 4,
                "locale": "en",
                "original_title": None,
                "title": "The Gentlemen",
                "created_date": "2024-01-01 05:30:00",
                "modified_date": "2024-01-01 05:30:00",
            },
            {
                "available_globally": 1,
                "release_date": None,
                "id": 5,
                "locale": "en",
                "original_title": None,
                "title": "Avatar The Last Airbender",
                "created_date": "2024-01-01 05:30:00",
                "modified_date": "2024-01-01 05:30:00",
            },
        ],
        "description": "This table stores information about TV shows, including their original and localized titles, release dates, global availability status, and associated metadata such as creation and modification timestamps. It is used to manage and present TV show listings for audiences across different regions and locales within the platform.",
    },
    "view_summary": {
        "columns": {
            "cumulative_weeks_in_top10": "INTEGER",
            "hours_viewed": "INTEGER",
            "view_rank": "INTEGER",
            "views": "INTEGER",
            "id": "INTEGER",
            "movie_id": "INTEGER",
            "season_id": "INTEGER",
            "duration": "TEXT",
            "end_date": "TEXT",
            "start_date": "TEXT",
            "created_date": "TEXT",
            "modified_date": "TEXT",
        },
        "sample": [
            {
                "cumulative_weeks_in_top10": None,
                "hours_viewed": 263700000,
                "view_rank": None,
                "views": 143800000,
                "id": 1,
                "movie_id": 1,
                "season_id": None,
                "duration": "SEMI_ANNUALLY",
                "end_date": "2024-06-30 12:30:00",
                "start_date": "2024-01-01 13:30:00",
                "created_date": "2024-01-01 05:30:00",
                "modified_date": "2024-01-01 05:30:00",
            },
            {
                "cumulative_weeks_in_top10": None,
                "hours_viewed": 230800000,
                "view_rank": None,
                "views": 129400000,
                "id": 2,
                "movie_id": 2,
                "season_id": None,
                "duration": "SEMI_ANNUALLY",
                "end_date": "2024-06-30 12:30:00",
                "start_date": "2024-01-01 13:30:00",
                "created_date": "2024-01-01 05:30:00",
                "modified_date": "2024-01-01 05:30:00",
            },
            {
                "cumulative_weeks_in_top10": None,
                "hours_viewed": 252500000,
                "view_rank": None,
                "views": 103800000,
                "id": 3,
                "movie_id": 3,
                "season_id": None,
                "duration": "SEMI_ANNUALLY",
                "end_date": "2024-06-30 12:30:00",
                "start_date": "2024-01-01 13:30:00",
                "created_date": "2024-01-01 05:30:00",
                "modified_date": "2024-01-01 05:30:00",
            },
            {
                "cumulative_weeks_in_top10": None,
                "hours_viewed": 146800000,
                "view_rank": None,
                "views": 84700000,
                "id": 4,
                "movie_id": 4,
                "season_id": None,
                "duration": "SEMI_ANNUALLY",
                "end_date": "2024-06-30 12:30:00",
                "start_date": "2024-01-01 13:30:00",
                "created_date": "2024-01-01 05:30:00",
                "modified_date": "2024-01-01 05:30:00",
            },
            {
                "cumulative_weeks_in_top10": None,
                "hours_viewed": 123100000,
                "view_rank": None,
                "views": 80300000,
                "id": 5,
                "movie_id": 5,
                "season_id": None,
                "duration": "SEMI_ANNUALLY",
                "end_date": "2024-06-30 12:30:00",
                "start_date": "2024-01-01 13:30:00",
                "created_date": "2024-01-01 05:30:00",
                "modified_date": "2024-01-01 05:30:00",
            },
        ],
        "description": "This table tracks aggregated viewing performance metrics for movies and TV show seasons, such as cumulative weeks in the top 10, total hours viewed, overall view counts, and viewing rank within specified date ranges. It associates each summary with either a movie or season and provides timeframes and audit timestamps, supporting analytics and reporting on content popularity and engagement trends.",
    },
}
