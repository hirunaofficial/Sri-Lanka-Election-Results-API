from flask import jsonify, request
from models.election_model import fetch_election_results, fetch_district_results, fetch_division_results

def get_election_results():
    results = fetch_election_results()
    return jsonify(results)

def get_district_results():
    district = request.args.get('district')
    if district:
        results = fetch_district_results(district)
        return jsonify(results)
    return jsonify({'error': 'District parameter missing'}), 400

def get_division_results():
    district = request.args.get('district')
    division = request.args.get('division')
    if district and division:
        results = fetch_division_results(district, division)
        return jsonify(results)
    return jsonify({'error': 'District or division parameter missing'}), 400