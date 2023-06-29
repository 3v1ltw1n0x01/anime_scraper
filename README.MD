# Anime API

This is an anime scraper that functions as an API using Flask. It offers various endpoints for accessing anime-related information.

## Prerequisites

- Python 3.x
- Flask

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/3v1ltw1n0x01/anime_scraper
   ```

Endpoints
---------

### Search Anime

Search for anime by name.

-   **URL:** `/search-anime/<string:name>`
-   **Method:** GET
-   **Parameters:**
    -   `name` (string): The name of the anime to search for.
-   **Returns:** The search result as JSON.

### Get Episodes

Get episodes of an anime.

-   **URL:** `/get-episodes/<string:s_id>`
-   **Method:** GET
-   **Parameters:**
    -   `s_id` (string): The ID of the anime series.
-   **Returns:** The episodes as JSON.

### Get Episode Download Link

Get the download link for an episode.

-   **URL:** `/get-episode-dl/<string:s_id>`
-   **Method:** GET
-   **Parameters:**
    -   `s_id` (string): The ID of the anime series.
-   **Returns:** The download link as JSON.

### Latest Episodes

Get the latest episodes of anime.

-   **URL:** `/latest-episodes`
-   **Method:** GET
-   **Returns:** The latest episodes as JSON.

### Fetch Seasonals

Fetch the seasonal anime.

-   **URL:** `/fetch-seasonals`
-   **Method:** GET
-   **Returns:** The seasonal anime as JSON.

### Get Anime Info

Get information about an anime.

-   **URL:** `/get-anime-info/<string:s_id>`
-   **Method:** GET
-   **Parameters:**
    -   `s_id` (string): The ID of the anime series.
-   **Returns:** The anime information as JSON.

Usage
-----

1.  Run the Flask application:

    bash

1.  ```
    python main.py
    ```

2.  Use a tool like cURL or Postman to make requests to the API endpoints.

License
-------

Copyright (c) 2023 3v1ltw1n0x01

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.