from flask import abort

from app.errors.validate_json_error import ValidateJsonError
from app.models.account import Account

def account_controller(params):
    raw_account = params.get('raw_account')
    account = Account(raw_account=raw_account)

    try:
        account.validate_params(params)
        resolved_account = account.get_resolved_account()
        return resolved_account
    except ValidateJsonError:
        abort(500, 'JSON Schema is not valid')
    except:
        abort(500, 'Unknown error')
