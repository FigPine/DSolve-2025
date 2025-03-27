# from flask import Flask, request, jsonify
# import sqlite3
# from datetime import datetime
# from math import radians, sin, cos, sqrt, atan2

# app = Flask(__name__)

# # Initialize database
# def init_db():
#     conn = sqlite3.connect('rides.db')
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS rides
#                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                   user_id INTEGER,
#                   start_lat REAL,
#                   start_lng REAL,
#                   end_lat REAL,
#                   end_lng REAL,
#                   start_time TEXT,
#                   end_time TEXT,
#                   fare REAL)''')
#     conn.commit()
#     conn.close()

# init_db()

# # Calculate distance between coordinates
# def haversine(lat1, lng1, lat2, lng2):
#     R = 6371  # Earth radius in km
#     dLat = radians(lat2 - lat1)
#     dLng = radians(lng2 - lng1)
#     a = (sin(dLat/2) ** 2) + (cos(radians(lat1)) * cos(radians(lat2)) * (sin(dLng/2) ** 2))
#     return R * 2 * atan2(sqrt(a), sqrt(1 - a))

# # API: Start ride
# @app.route('/api/start_ride', methods=['POST'])
# def start_ride():
#     data = request.json
#     conn = sqlite3.connect('rides.db')
#     c = conn.cursor()
#     c.execute('''INSERT INTO rides (user_id, start_lat, start_lng, start_time)
#                  VALUES (?, ?, ?, ?)''',
#               (data['user_id'], data['lat'], data['lng'], datetime.now().isoformat()))
#     ride_id = c.lastrowid
#     conn.commit()
#     conn.close()
#     return jsonify({"ride_id": ride_id})

# # API: End ride
# @app.route('/api/end_ride', methods=['POST'])
# def end_ride():
#     data = request.json
#     conn = sqlite3.connect('rides.db')
#     c = conn.cursor()
#     c.execute('''SELECT start_lat, start_lng FROM rides WHERE id=?''', (data['ride_id'],))
#     start_lat, start_lng = c.fetchone()
#     distance = haversine(start_lat, start_lng, data['lat'], data['lng'])
#     fare = round(distance * 10, 2)  # ₹10 per km
#     c.execute('''UPDATE rides SET end_lat=?, end_lng=?, end_time=?, fare=? WHERE id=?''',
#               (data['lat'], data['lng'], datetime.now().isoformat(), fare, data['ride_id']))
#     conn.commit()
#     conn.close()
#     return jsonify({"fare": fare, "distance": distance})

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import sqlite3
# from datetime import datetime
# from math import radians, sin, cos, sqrt, atan2

# app = Flask(__name__)
# CORS(app)

# # Initialize database
# def init_db():
#     conn = sqlite3.connect('rides.db')
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS rides
#                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                   user_id INTEGER,
#                   start_lat REAL,
#                   start_lng REAL,
#                   end_lat REAL,
#                   end_lng REAL,
#                   start_time TEXT,
#                   end_time TEXT,
#                   fare REAL)''')
#     conn.commit()
#     conn.close()

# init_db()

# # Calculate distance between coordinates
# def haversine(lat1, lng1, lat2, lng2):
#     R = 6371  # Earth radius in km
#     dLat = radians(lat2 - lat1)
#     dLng = radians(lng2 - lng1)
#     a = (sin(dLat/2) ** 2) + (cos(radians(lat1)) * cos(radians(lat2)) * (sin(dLng/2) ** 2)
#     return R * 2 * atan2(sqrt(a), sqrt(1 - a))

# @app.route('/api/start_ride', methods=['POST', 'OPTIONS'])
# def start_ride():
#     if request.method == 'OPTIONS':
#         return jsonify({"status": "ok"}), 200
        
#     data = request.get_json()
#     conn = sqlite3.connect('rides.db')
#     c = conn.cursor()
#     c.execute('''INSERT INTO rides (user_id, start_lat, start_lng, start_time)
#                  VALUES (?, ?, ?, ?)''',
#               (data['user_id'], data['lat'], data['lng'], datetime.now().isoformat()))
#     ride_id = c.lastrowid
#     conn.commit()
#     conn.close()
#     return jsonify({"ride_id": ride_id})

# @app.route('/api/end_ride', methods=['POST', 'OPTIONS'])
# def end_ride():
#     if request.method == 'OPTIONS':
#         return jsonify({"status": "ok"}), 200
        
#     data = request.get_json()
#     conn = sqlite3.connect('rides.db')
#     c = conn.cursor()
#     c.execute('''SELECT start_lat, start_lng FROM rides WHERE id=?''', (data['ride_id'],))
#     start_lat, start_lng = c.fetchone()
#     distance = haversine(start_lat, start_lng, data['lat'], data['lng'])
#     fare = round(distance * 10, 2)  # ₹10 per km
#     c.execute('''UPDATE rides SET end_lat=?, end_lng=?, end_time=?, fare=? WHERE id=?''',
#               (data['lat'], data['lng'], datetime.now().isoformat(), fare, data['ride_id']))
#     conn.commit()
#     conn.close()
#     return jsonify({"fare": fare, "distance": distance})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)


from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3
from datetime import datetime
from math import radians, sin, cos, sqrt, atan2

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize database
def init_db():
    conn = sqlite3.connect('rides.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS rides
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER,
                  start_lat REAL,
                  start_lng REAL,
                  end_lat REAL,
                  end_lng REAL,
                  start_time TEXT,
                  end_time TEXT,
                  fare REAL)''')
    conn.commit()
    conn.close()

init_db()

# Fixed haversine function with proper parentheses
def haversine(lat1, lng1, lat2, lng2):
    R = 6371  # Earth radius in km
    dLat = radians(lat2 - lat1)
    dLng = radians(lng2 - lng1)
    a = (sin(dLat/2) ** 2) + (cos(radians(lat1))) * cos(radians(lat2)) * (sin(dLng/2) ** 2)
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))

@app.route('/api/start_ride', methods=['POST', 'OPTIONS'])
def start_ride():
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200
        
    data = request.get_json()
    
    # Case-sensitive field check
    if 'lat' not in data or 'lng' not in data:
        return jsonify({"error": "Use lowercase 'lat' and 'lng'"}), 400
        
    conn = sqlite3.connect('rides.db')
    c = conn.cursor()
    c.execute('''INSERT INTO rides (user_id, start_lat, start_lng, start_time)
                 VALUES (?, ?, ?, ?)''',
              (data['user_id'], data['lat'], data['lng'], datetime.now().isoformat()))
    ride_id = c.lastrowid
    conn.commit()
    conn.close()
    return jsonify({"ride_id": ride_id})

@app.route('/api/end_ride', methods=['POST', 'OPTIONS'])
def end_ride():
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200
        
    data = request.get_json()
    conn = sqlite3.connect('rides.db')
    c = conn.cursor()
    
    try:
        c.execute('''SELECT start_lat, start_lng FROM rides WHERE id=?''', (data['ride_id'],))
        start_lat, start_lng = c.fetchone()
        
        # Case-sensitive field check
        if 'lat' not in data or 'lng' not in data:
            return jsonify({"error": "Use lowercase 'lat' and 'lng'"}), 400
            
        distance = haversine(start_lat, start_lng, data['lat'], data['lng'])
        fare = round(distance * 10, 2)  # ₹10 per km
        
        c.execute('''UPDATE rides SET end_lat=?, end_lng=?, end_time=?, fare=? WHERE id=?''',
                  (data['lat'], data['lng'], datetime.now().isoformat(), fare, data['ride_id']))
        conn.commit()
        return jsonify({"fare": fare, "distance": distance})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        conn.close()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/fare")
def fare():
    return render_template("fare.html")

@app.route("/gps")
def gps():
    return render_template("gps.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)