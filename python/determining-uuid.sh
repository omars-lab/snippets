#!/bin/bash

python -c 'x = "9"*38; import json, uuid; u = uuid.uuid4().int; print(json.dumps({"i": str(int(x)), "u": str(u), "su": str(u>>2)}), end="");' | jq 'to_entries | [ .[] | { key: .key, value: [.value, (.value | length)] } ] | from_entries'

python -c "print(str(2**128))"
python -c "print(str(2**127))"
python -c "print(str(2**126))"

function determin_signed() {
  BIT=${1}
  echo --------------------------------------------------------------------------------
  python -c "print('           bits:  ', str(     ${BIT}      )                      )"
  python -c "print('unsigned digits:  ', len(str(((2**${BIT}))))                     )"
  python -c "print('   unsigned max:  ', str( ( (2**${BIT}) ) )                      )"
  python -c "print('   unsigned min: ',  str(        0        )                      )"
  python -c "print('  signed digits:  ', len(str(((2**${BIT}) ) - ( 2**(${BIT}-1) ))))"
  python -c "print('     signed max:  ', str( ( (2**${BIT}) ) - ( 2**(${BIT}-1) ) )  )"
  python -c "print('     signed min: ',  str(               0 - ( 2**(${BIT}-1) ) )  )"
  echo --------------------------------------------------------------------------------
}

# python -c "import uuid; print(str((uuid.uuid4().int >> 1) - (2**126)))"

determin_signed 128
determin_signed 127
determin_signed 126

# https://docs.snowflake.com/en/sql-reference/data-types-numeric.html

# --------------------------------------------------------------------------------
#            bits:   127
# unsigned digits:   39
#    unsigned max:   170141183460469231731687303715884105728
#    unsigned min:  0
#   signed digits:   38
#      signed max:   85070591730234615865843651857942052864
#      signed min:  -85070591730234615865843651857942052864
# --------------------------------------------------------------------------------

# python -c 'import uuid; print(str( (uuid.uuid4().int >> 1) - (2**126) ).replace("-",""), end="")' | wc

# uuid.uuid4().int >> 1) - (2**126)