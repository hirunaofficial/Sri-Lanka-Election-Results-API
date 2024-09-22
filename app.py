from flask import Flask
from controllers.election_controller import get_overall_results, get_election_results, get_district_results, get_division_results

app = Flask(__name__)

@app.route('/api/overall', methods=['GET'])
def overall_results():
    return get_overall_results()

@app.route('/api/election', methods=['GET'])
def election_results():
    return get_election_results()

@app.route('/api/district', methods=['GET'])
def district_results():
    return get_district_results()

@app.route('/api/division', methods=['GET'])
def division_results():
    return get_division_results()

if __name__ == '__main__':
    app.run(debug=True)