from flask import Flask
import wit_anime as wit


app = Flask(__name__)


@app.route("/search-anime/<string:name>", methods=["GET"])
def search_anime(name):
    result = wit.search_anime(name)
    return result


@app.route("/get-episodes/<string:s_id>", methods=["GET"])
def get_episodes(s_id):
    result = wit.get_episodes(s_id)
    return result


@app.route("/get-episode-dl/<string:s_id>", methods=["GET"])
def get_episode_dl(s_id):
    result = wit.get_episode_dl(s_id)
    return result


@app.route("/latest-episodes", methods=["GET"])
def latest_episodes():
    result = wit.latest_episodes()
    return result


@app.route("/fetch-seasonals", methods=["GET"])
def fetch_seasonals():
    result = wit.fetch_seasonals()
    return result


@app.route("/get-anime-info/<string:s_id>", methods=["GET"])
def get_anime_info(s_id):
    result = wit.get_anime_info(s_id)
    return result


if __name__ == "__main__":
    app.run("0.0.0.0")
