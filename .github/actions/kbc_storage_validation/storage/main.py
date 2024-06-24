import argparse
from storage_pull import StoragePull as Sp
from storage_diff import StorageDiff as Diff


class StorageDiff:
    def __init__(self, source_workdir, source_host, source_token, dest_workdir, dest_host, dest_token):
        src_sp = Sp(source_host, source_token, f"src_{source_workdir}_storage.json")
        dest_sp = Sp(dest_host, dest_token, f"dest_{dest_workdir}_storage.json")
        diff_file = Diff(src_sp.pull(), dest_sp.pull()).compare()


def check_parameters():
    parser = argparse.ArgumentParser(description='Generator storage diff')
    parser.add_argument('--source-workdir', type=str, required=True)
    parser.add_argument('--source-host', type=str, required=True)
    parser.add_argument('--source-token', type=str, required=True)
    parser.add_argument('--dest-workdir', type=str, required=True)
    parser.add_argument('--dest-host', type=str, required=True)
    parser.add_argument('--dest-token', type=str, required=True)

    # Check for empty strings
    args = parser.parse_args()
    for arg, value in vars(args).items():
        if value.strip() == "":
            parser.error(f"The argument {arg} cannot be an empty string")

    return parser.parse_args()


if __name__ == '__main__':
    args = check_parameters()
    print("token_here")
    print(args.source_token[2:8])
    print(args.dest_token[2:8])
    StorageDiff(
        source_workdir=args.source_workdir,
        source_host=args.source_host,
        source_token=args.source_token,
        dest_workdir=args.dest_workdir,
        dest_host=args.dest_host,
        dest_token=args.dest_token
    )
