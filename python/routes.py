from datatypes import Dataset, DatasetSchema

from flask import get_app, jsonify, make_response

# ----------------------------------------------------------------------------
@blueprint.route('/ilplatform/v1/datasets', methods=['POST'])
@login_required
def add_dataset():
    try:
        ds: Dataset = DatasetSchema().load(request.json)
    except Exception as e:
        return make_response(jsonify("Unable to load Dataset object from the given JSON"), 400)

    if ds is None or not ds.valid():
        return make_response(jsonify("Dataset must include a creator, job, and name."), 400)

    try:
        retval = get_app().methods().add_dataset(ds)
        if retval:
            json_retval = dict()
            for k in retval:
                json_retval[k] = DatasetSchema().dump(retval[k])
            response = make_response(jsonify(json_retval), 201)
        else:
            response = make_response(jsonify("Invalid request"), 400)
    except Exception as e:
        response = make_response(jsonify(e), 500)

    return response

# ----------------------------------------------------------------------------
@blueprint.route('/ilplatform/v1/datasets', methods=['GET'])
@login_required
def get_dataset(datasetid):
    body = request.json()
    id = body['id']
    try:
        retval = get_app().methods().get_datasets(id=id)
        if retval:
            # There should only be one dataset in retval
            for k in retval:
                json_retval = DatasetSchema().dump(retval[k])
                break
            response = make_response(jsonify(json_retval), 200)
        else:
            response = make_response(jsonify("Not found"), 404)
    except Exception as e:
        response = make_response(jsonify(e), 500)

    return response