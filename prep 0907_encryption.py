letter = "A"
shift = 8
offset = 32

ordletter = ord(letter) # find the ordinal value # 65
shiftedord = ordletter + (ordletter - offset + shift) % 95
encrypted = chr(shiftedord)
print(encrypted)


def encrypt(char, shift):

    #letter = "z"

    #shift = 8

    offset = 32

    ordletter = ord(char) # find the ordinal value # 65

    shiftedord = offset + (ordletter - offset + shift ) % 95

    encrypted = chr(shiftedord)

    return encrypted

def encrypt_sentence(sentence, shift, task):
    if task.lower() == "e":
        print("Encrypting.... ")
    elif task.lower() == "d":
        print("Decrypting...")
        shift = 0 - shift
    else:
        print("Invalid option")
        return ""
    
    encrypted_sentence = ""

    for c in sentence:
        encrypted_letter = encrypt(c, shift)
        encrypted_sentence = encrypted_sentence + encrypted_letter

    return encrypted_sentence

msg = input("What do you want to say? ")
numshift = input("What is the shift value? ")
option = input("Enter (e) to encrypt, or (d) to decrypt? ")
output = encrypt_sentence(msg, int(numshift), option)
print(output)


sentence = '''eOaVW\Ub]\H.Us}!uwo.bsqv.w".s|rw|u.w#".!s"so!qv.o|r.sr$qo#w}|oz.~o!#|s!"vw~".w|.#vs.Qvw|s"s.qw#ws".}t.bwo|xw|.o|r.avs|)vs|:.#vs.ca.$|w%s!"w#(."owr.}|.T!wro(.6as~.D7:.t}zz}&w|u."q!$#w|(.t!}{.Q}|u!s"".}%s!.w#".q}zzop}!o#w}|.&w#v.s|#w#ws".ozzsusrz(.zw|ysr.#}.Qvw|o5".{wzw#o!(<'''
