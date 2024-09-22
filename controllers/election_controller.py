from flask import jsonify, request
from models.election_model import fetch_election_results, fetch_district_results, fetch_division_results

def get_election_results():
    results = fetch_election_results()
    if results is not None:
        return jsonify({'status': 'success', 'data': results})
    return jsonify({'status': 'error', 'message': 'Failed to fetch results'}), 500

def get_district_results():
    district = request.args.get('district')
    if district:
        results = fetch_district_results(district)
        if results:
            return jsonify({'status': 'success', 'data': results})
        return jsonify({'status': 'error', 'message': 'No results found for the specified district'}), 404
    return jsonify({'status': 'error', 'message': 'District parameter missing'}), 400

def get_division_results():
    district = request.args.get('district')
    division = request.args.get('division')
    if district and division:
        results = fetch_division_results(district, division)
        if results:
            return jsonify({'status': 'success', 'data': results})
        return jsonify({'status': 'error', 'message': 'No results found for the specified district and division'}), 404
    return jsonify({'status': 'error', 'message': 'District or division parameter missing'}), 400
