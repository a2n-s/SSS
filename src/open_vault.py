import argparse
import os

from shamir import recover_secret


def main():
    """
        ______________________________________________________TODO______________________________________________________

        Args:

        Return:
             ()_______________________________________________TODO______________________________________________________
    """
    parser = argparse.ArgumentParser("a parser to give names and priorities")
    parser.add_argument("--present", "-p", default=[], nargs="+", help="a list of names to reveal the code.")
    parser.add_argument("--name", "-n", default="secret", type=str,
                        help="the name of the secret (str) (default: 'secret')")

    args = parser.parse_args()

    identifiers = []
    keys = []
    holders = []

    for name in args.present:
        try:
            directory = os.path.join(name.lower(), args.name)
            with open(os.path.join(directory, "keys"), 'r') as file:
                print(file.readline().strip(), "is here.")
                for _ in range(int(file.readline().strip())):
                    identifiers.append(int(file.readline().strip()))
                    keys.append(int(file.readline().strip()))
                    holders.append(name)
        except FileNotFoundError as fne:
            print(f"{name} should not be here ({fne}) because this person is not part of the secret sharing!")
    print()

    shares = list(zip(identifiers, keys))
    for (id, key), name in zip(shares, holders):
        print(f"id: {id}, key: {key} from {name}")
    print()

    secret = recover_secret(shares)
    print(f"secret '{args.name}' recovery with {len(shares)} keys -> {secret}.")


if __name__ == "__main__":
    main()
