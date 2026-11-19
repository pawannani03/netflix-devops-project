from flask import Flask, render_template, request

app = Flask(__name__)

movies = [
    {
        "title": "Stranger Things",
        "category": "Series",
        "year": 2022,
        "rating": "8.7",
        "description": "A group of friends discovers mysterious supernatural events.",
        "poster": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500"
    },
    {
        "title": "The Dark Knight",
        "category": "Action",
        "year": 2008,
        "rating": "9.0",
        "description": "Batman faces his greatest enemy in Gotham City.",
        "poster": "https://images.unsplash.com/photo-1509347528160-9a9e33742cdb?w=500"
    },
    {
        "title": "Interstellar",
        "category": "Sci-Fi",
        "year": 2014,
        "rating": "8.7",
        "description": "A journey through space to save humanity.",
        "poster": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=500"
    },
    {
        "title": "The Witcher",
        "category": "Series",
        "year": 2019,
        "rating": "8.0",
        "description": "A monster hunter navigates a dangerous fantasy world.",
        "poster": "https://images.unsplash.com/photo-1518709594023-6eab9bab7b23?w=500"
    },
    {
        "title": "Extraction",
        "category": "Action",
        "year": 2020,
        "rating": "6.8",
        "description": "A mercenary takes on a dangerous rescue mission.",
        "poster": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=500"
    },
    {
        "title": "The Space Journey",
        "category": "Sci-Fi",
        "year": 2024,
        "rating": "8.2",
        "description": "An adventure into the mysteries of the universe.",
        "poster": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=500"
    }
]


@app.route("/")
def home():
    search_query = request.args.get("search", "").strip()
    selected_category = request.args.get("category", "All")

    filtered_movies = movies

    if search_query:
        filtered_movies = [
            movie for movie in filtered_movies
            if search_query.lower() in movie["title"].lower()
        ]

    if selected_category != "All":
        filtered_movies = [
            movie for movie in filtered_movies
            if movie["category"] == selected_category
        ]

    categories = ["All", "Action", "Sci-Fi", "Series"]

    return render_template(
        "index.html",
        movies=filtered_movies,
        categories=categories,
        selected_category=selected_category,
        search_query=search_query
    )


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
