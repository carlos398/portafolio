def get(base_dict, nested_keys, default_value=None):
    """
    Get a nested value from dict if exist or return default value
    :param base_dict: dict, Dictionary to be checked. Ie, {"key": 'value'}
    :param nested_keys: list, dict keys to be validated on the dict. Ie, ["key", "sub_key"]
    :param default_value: any, The default value you whant to return if no has in dict. Ie "key"
    :return Object: Element found on the dict or the value of default_value. Ie, "sub_value" or None
    """

    key_exist, keys_value = keys_exists(base_dict, nested_keys, not_found_value=default_value)

    return keys_value


def keys_exists(validation_dict, nested_keys, not_found_value=None):
    """
    Validate nested attributes on dictionary
    Based on https://stackoverflow.com/questions/43491287/elegant-way-to-check-if-a-nested-key-exists-in-a-python-dict/43491315
    :param validation_dict: dict, Dictionary to be checked. Ie, {"key": {"sub_key": "sub_value"}}
    :param nested_keys: list, dict keys to be validated on the dict. Ie, ["key", "sub_key"]
    :param not_found_value: Value returned when no element is found on the dict. Ie, None or []
    :return Tuple:
        - boolean, Confirms if nested key is found. Ie, True
        - Element found on the dict or the value of not_found_value. Ie, "sub_value" or None

    Usage examples:

        > # success example
        > validation_dict = {"key": {"sub_key": "sub_value"}}
        > nested_keys = ["key", "sub_key"]
        > not_found_value = []
        > keys_exists(validation_dict, nested_keys, not_found_value)
        (True, 'sub_value')

        > # not found example
        > validation_dict = {"key": {"sub_key": "sub_value"}}
        > nested_keys = ["key", "sub_key_not_found"]
        > not_found_value = []
        > keys_exists(validation_dict, nested_keys, not_found_value)
        (False, [])

        > # empty dict example
        > validation_dict = {}
        > nested_keys = ["key", "sub_key_not_found"]
        > not_found_value = []
        > keys_exists(validation_dict, nested_keys, not_found_value)
        (False, [])

        > # empty key list example
        > validation_dict = {"key": {"sub_key": "sub_value"}}
        > nested_keys = []
        > not_found_value = []
        > keys_exists(validation_dict, nested_keys, not_found_value)
        (False, [])
    """

    if type(validation_dict) is not dict or not nested_keys:
        return False, not_found_value

    temp_validation_dict = validation_dict
    for key in nested_keys:
        try:
            temp_validation_dict = temp_validation_dict[key]
        except Exception:
            return False, not_found_value
    return True, temp_validation_dict





call_api_response = {
    'response': {
        'status_code': 200,
        'data': {
            'users': {
                'name': 'carlos',
                'bought': {
                    'carro': {
                        'modelo': '2001',
                        'color': 'red',
                        'tipo': 'camioneta'
                    },
                    'computador': {
                        'marca': 'lenovo',
                        'presio': 1300000
                    }
                } 
            }
        }
    },
    'error': None,

}


default_color = 'negro'
value = get(call_api_response, ['response', 'data', 'users', 'bought', 'carro', 'color'], default_color )
print(value)

value = get(call_api_response, ['response', 'data', 'users', 'bought', 'computador', 'color'], default_color )
print(value)


usuarios = [
  ['109878787', 'Mac G', 'Herrera A', 'mac@mail.com'],
  ['109898766', 'Carlos A', 'Reyes P', 'carlos@mail.com'],
  ['12312312', 'Jeronimo O', 'Granja O', 'jronimo@mail.com']
]

for usuario in usuarios:
      print(
      'cedula: {} Hola {} mucho gusto, te voy a enviar un email a esta direccion {}'.format(
       usuario[0], '{} {}'.format(usuario[1], usuario[2]), usuario[3]
      ) 

  )

print("metodo 2 ", "*"*50)

for usuario in usuarios:
      full_name = '{} {}'.format(usuario[1], usuario[2])

      print(
      'cedula: {cedula} Hola {full_name} mucho gusto, te voy a enviar un email a esta direccion {email}'.format(
        cedula=usuario[0],
        full_name=full_name,
        email=usuario[3]
      ) 
        )


print("metodo 3 ", "*"*50)


usuarios_v2 = [{
    'cedula': usuario[0],
    'full_name': '{} {}'.format(usuario[1], usuario[2]),
    'email': usuario[3]}
    for usuario in usuarios
]
for usuario in usuarios_v2:
  print(
      'cedula: {cedula} Hola {full_name} mucho gusto, te voy a enviar un email a esta direccion {email}'.format(
       **usuario
      ) 
  )


print("metodo 4 ", "*"*50)

for usuario in usuarios_v2:
      print(
      'cedula: {cedula} Hola {full_name} mucho gusto, te voy a enviar un email a esta direccion {email}'.format(
       **usuario
      ) 
  )


print("metodo 5 ", "*"*50)

usuarios_v3 = {
    usuario[0]: {
      'full_name': '{} {}'.format(usuario[1], usuario[2]),
      'email': usuario[3]
    }
    for usuario in usuarios
  }
