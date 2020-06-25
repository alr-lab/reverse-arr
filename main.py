import os
import sys
import typing


def main(pn: str, args: typing.List) -> None:
    """ Program's entrypoint

    Arguments:
    pn   -- Program name
    args -- Arguments passed to the program
    """
    if len(args) == 0:
        err(f"Usage: {pn} 42 1337 23", os.EX_USAGE)

    print(*reverse_array(args))


def err(msg: str, code: int = os.EX_OK) -> typing.NoReturn:
    """ Prints error message and exits program

    Arguments:
    msg  -- Error message
    code -- POSIX standard exit code for that error

    Prints the error message *msg* passed as an argument to *stderr* stream
    and exits the program with the proper POSIX standard exit code.
    """
    print(msg, file=sys.stderr)
    sys.exit(code)


def reverse_array(arr):
    """ Simple function to reverse an array

    Arguments:
    arr -- Array to be reversed
    """
    i = len(arr)
    res = []
    while i > 0:
        res.append(arr[i-1])
        i = i-1
    return res


if __name__ == '__main__':
    main(sys.argv[0], sys.argv[1:])
