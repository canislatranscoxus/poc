'''
This examples show how a user can pay by bank transfer.
The process has the next steps:

1. ecommerce request to openpay a "pay reference".

2. User make a bank transfer using the "pay reference"

3. ecommerce receives a notification that user has paid.


'''
import json
from Charges import Charges


# Step 1. ecommerce request to openpay a "pay reference".

data = {
   "method"         : "bank_account",
   "amount"         : 100,
   "description"    : "Cargo con banco",
   "order_id"       : "Boid_004",
   "due_date"       : "2022-12-31T23:59:25-05:00",

   "customer"       : {
        "name"          : "Mickey",
        "last_name"     : "Mouse",
        "phone_number"  : "4423456723",
        "email"         : "mickey.mouse@disney.com"
   },

   "confirm"        : "false",
   "send_email"     : "false",
   "redirect_url"   : "http://www.basmatiyes.mx/payments/paid/Boid_001"

} 

charges = Charges()

response  = charges.request_bank_ref( data )
j = response.json()

# debug
print( '\n {}\n '.format( json.dumps( j, indent=3 ) ) )


reference = j[ 'id'      ]
amount    = j[ 'amount'  ]
concept   = j[ 'payment_method' ][ 'name' ]
clabe     = j[ 'payment_method' ]['clabe' ]
cie       = j[ 'payment_method' ][ 'agreement' ]

msg = '''\n El cliente deberá ingresar a su banca en linea y dentro del menú “Pagar” 
    seleccionar “De servicios”
    Ingresar el “Número de convenio CIE” (campo payment_method.agreement de la transacción).
    Ingrese los datos de registro para concluir con la operación:

    Referencia           : {}
    Monto exacto a pagar : {}
    Concepto             : {}
'''.format( cie, amount, concept )
print( msg )

msg = '''Deberá registrar la cuenta beneficiaria del pago con los siguientes datos:
        Nombre del banco destino : BBVA Bancomer
        Número de cuenta CLABE : {}
        Nombre de beneficiario : Basmatiyes

    Ingresar a la sección de transferencias o pagos a terceros y proporcionar los datos de la transferencia, monto y concepto del pago.
        Monto exacto a pagar :{}
        En el concepto de pago (numero de 20 dígitos ) : {}
        En la referencia : convenio CIE (1411217)

'''.format( clabe, amount, concept, reference )
print( msg )


# Step 2. User make a bank transfer using the "pay reference"
print( 'the user can go to her bank and pay' )

# Step 3. ecommerce receives a notification that user has paid.
print( 'we can have a view in Django Python that update shopping order as paid, ...' )
