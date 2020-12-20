import os
from time import sleep
import log
from mcl import CL


def main():
    uname = os.environ["UNAMES"]
    upass = os.environ["UPASSS"]
    secret = os.environ.get("SECRETS", CL.DEFAULT_SECRET)
    secret = CL.DEFAULT_SECRET if len(secret) < len(CL.DEFAULT_SECRET) else secret

    uname = uname.split(log.ARGS_SEPARATOR)
    upass = upass.split(log.ARGS_SEPARATOR)
    secret = secret.split(log.ARGS_SEPARATOR)
    log.i("all %s", len(uname))
    for index in range(0, len(uname)):
        if len(secret) != len(uname):
            cl = CL(uname[index], upass[index])
        else:
            cl = CL(uname[index], upass[index], secret[index])
        btype = CL.BANK_TYPE_DINGQI
        action = CL.BANK_ACTION_SAVE
        if not (cl.is_login() and cl.bank(1, btype=btype, action=action)):
            raise Exception("bank fail")
        else:
            log.i("success!")
        sleep(3)


if __name__ == "__main__":
    main()
